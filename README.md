# CallGuard AI — Intelligent Call Screening & Fraud Prevention Platform

![CallGuard AI Banner](https://via.placeholder.com/1200x300.png?text=CallGuard+AI+%E2%80%94+Enterprise+Fraud+Prevention)

[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![Kafka](https://img.shields.io/badge/Kafka-Event%20Driven-red.svg)](https://kafka.apache.org/)

## 📖 Project Vision

CallGuard AI is an enterprise-grade, event-driven intelligent platform designed to screen incoming calls in real-time, detect fraud, and protect users from scams, telemarketing, and phishing attempts. 

By leveraging a robust **Multi-Agent Generative AI pipeline** and a highly scalable **Kafka-based event-streaming architecture**, CallGuard AI analyzes call transcripts on the fly. It provides rich explainability, real-time risk scoring, and actionable safety guidance for users, all delivered via a high-performance Next.js enterprise dashboard.

## ✨ Key Features

- **Real-Time Event Streaming:** Built on Apache Kafka for asynchronous, highly resilient call event processing.
- **Multi-Agent AI Pipeline:** Dedicated agents for Fraud Detection, Summarization, and Action Recommendation.
- **Retrieval-Augmented Generation (RAG):** Powered by `pgvector` to cross-reference calls against known scam patterns.
- **Explainable AI (XAI):** Provides transparent reasoning chains, confidence scores, and suspicious phrase highlighting.
- **Real-Time WebSockets:** Instantly pushes risk alerts and live call updates to the browser.
- **Enterprise Observability:** Instrumented with Prometheus, Grafana, and structured logging.
- **Cloud-Native & Modular:** Microservice-ready boundaries prepared for Kubernetes orchestration.

## 🏗️ Architecture

CallGuard AI follows an event-driven microservices architecture optimized for scalability and fault tolerance.

### High-Level Event Flow

![Architecture Flow](https://via.placeholder.com/800x400.png?text=Event+Driven+Architecture+Diagram)

*See the `architecture/` directory for detailed Mermaid diagrams and Architecture Decision Records (ADRs).*

### Tech Stack

- **Frontend:** Next.js 14 (App Router), TypeScript, Tailwind CSS, shadcn/ui, Zustand, TanStack Query
- **API Gateway:** FastAPI, Python 3.12, Pydantic v2
- **AI Engine:** Python, LangChain, OpenAI/Mock Fallback, Celery Workers
- **Event Bus:** Apache Kafka
- **Database Layer:** PostgreSQL + `pgvector` + Alembic
- **Cache & Pub/Sub:** Redis
- **DevOps:** Docker, Docker Compose, GitHub Actions
- **Observability:** Prometheus, Grafana

## 🚀 Quick Start (Local Deployment)

We use Docker Compose to orchestrate the entire platform locally.

### Prerequisites
- Docker & Docker Compose
- Node.js 20.x (for local UI dev if not using Docker)
- Python 3.12 (for local backend dev)

### 1. Clone & Configure
```bash
git clone https://github.com/yourusername/callguard-ai.git
cd callguard-ai
cp .env.example .env
```
*Edit `.env` to add your optional OpenAI API key. The system will use a mock fallback if omitted.*

### 2. Boot the Infrastructure
```bash
docker-compose up -d --build
```

### 3. Access the Services
- **Enterprise Dashboard:** http://localhost:3000
- **API Swagger Docs:** http://localhost:8000/docs
- **Grafana Observability:** http://localhost:3001
- **Prometheus:** http://localhost:9090

## 📂 Repository Structure

```text
call-screening-ai/
├── architecture/      # Diagrams, ADRs (Architecture Decision Records)
├── docs/              # System design, Security, MLOps
├── infra/             # Docker configs, Kubernetes manifests, Monitoring
├── services/          
│   ├── api-gateway/   # FastAPI REST Gateway
│   ├── ai-engine/     # Multi-Agent pipeline & RAG
│   ├── notifications/ # WebSocket Server
│   └── frontend/      # Next.js Application
└── scripts/           # DB setup, DB seeding, Load testing
```

## 🛡️ Security

Security is embedded into the core design:
- **Authentication:** JWT with refresh token rotation.
- **Authorization:** Granular RBAC (User vs. Admin roles).
- **Secrets:** Strict 12-factor app compliance (no hardcoded secrets).
- **Data:** SQL injection prevention via ORM, sanitized API outputs.

*Read more in `docs/security/security-model.md`*

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for guidelines on conventional commits, branch management, and PR reviews.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
