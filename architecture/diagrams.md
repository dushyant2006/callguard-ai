# Architecture Diagrams

These diagrams illustrate the enterprise event-driven architecture of the CallGuard AI platform.

## High-Level Architecture

```mermaid
graph TD
    subgraph Frontend Layer
        UI[Next.js App Router]
        WS_Client[WebSocket Client]
    end

    subgraph API Layer
        API[FastAPI Gateway]
        Auth[JWT Auth Guard]
        API --> Auth
    end

    subgraph Messaging Layer
        KAFKA[Apache Kafka]
        REDIS[Redis Pub/Sub & Cache]
    end

    subgraph Worker & AI Layer
        AI[AI Engine - Celery/Kafka Consumer]
        NOTIFY[Notification WebSocket Service]
    end

    subgraph Data Layer
        DB[(PostgreSQL + pgvector)]
    end

    UI -->|REST / HTTP| API
    UI -->|wss://| NOTIFY

    API -->|Write/Read| DB
    API -->|Publish Event| KAFKA
    
    KAFKA -->|Consume| AI
    KAFKA -->|Consume| NOTIFY
    
    AI -->|Retrieve/Store| DB
```

## AI Multi-Agent Pipeline

```mermaid
graph LR
    Incoming[Transcript Ingestion] --> Router[Agent Router]
    
    Router -->|RAG Retrieval| VectorDB[(pgvector Scam DB)]
    VectorDB --> RAG[RAG Fraud Context]
    
    Router --> FraudAgent[Fraud Classifier Agent]
    Router --> SummaryAgent[Transcript Summarizer Agent]
    
    FraudAgent --> XAI[Explainability Agent]
    RAG --> XAI
    
    SummaryAgent --> ActionAgent[Action Recommendation Agent]
    XAI --> ActionAgent
    
    ActionAgent --> Result[Final Risk Profile Output]
```

## Kafka Event Flow

```mermaid
sequenceDiagram
    participant API as API Gateway
    participant K as Kafka `call-events`
    participant AI as AI Engine Worker
    participant K2 as Kafka `alert-events`
    participant WS as Notification Service
    participant FE as Next.js Dashboard

    API->>K: publish {call_id, status: 'ingested'}
    K->>AI: consume event
    AI->>AI: Run ML/GenAI Pipeline
    AI->>K2: publish {call_id, risk_score: 95, action: 'BLOCK'}
    K2->>WS: consume event
    WS->>FE: WebSocket push {alert: 'Scam Detected'}
```
