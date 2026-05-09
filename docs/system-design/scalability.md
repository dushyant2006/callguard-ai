# System Design: Scalability & Resiliency

## Scalability Strategy

The architecture is designed to scale horizontally across multiple dimensions.

1. **API Gateway (Stateless)**: The FastAPI service is completely stateless (session state is in Redis, persistence in Postgres). It can be scaled infinitely behind a load balancer (e.g., Nginx or AWS ALB) using Kubernetes ReplicaSets.
2. **AI Workers (Asynchronous)**: Call ingestion is asynchronous. High volumes of incoming calls won't block the API. Instead, they accumulate in Kafka topics. We can scale the AI engine consumers independently based on consumer lag metrics (tracked via Prometheus).
3. **Database (Relational & Vector)**: PostgreSQL handles heavy writes. To scale, we can introduce PgBouncer for connection pooling and read-replicas for heavy analytic queries from the dashboard.

## Failure Handling & Resiliency

To prevent cascading failures and ensure enterprise-grade reliability, we employ the following strategies:

### 1. Dead-Letter Queues (DLQ)
If the AI Engine fails to process a transcript (e.g., due to an OpenAI API timeout), the message is retried 3 times with exponential backoff. If it fails permanently, it is routed to a `call-events-dlq` Kafka topic. A separate cron job or analyst can review DLQ events.

### 2. Graceful AI Degradation (Fallback Model)
If the primary GenAI provider (e.g., OpenAI) goes down, the system automatically falls back to a deterministic, rule-based baseline model. 
- *Rule-based model*: Checks the caller ID against the PostgreSQL blocklist and scans the transcript for exact-match regex phrases. 
This ensures the platform still protects users even during a massive AI provider outage.

### 3. Circuit Breakers
We use circuit breaker logic for external API calls (e.g., telephony providers, OpenAI). If the external service has a 5xx error rate above 50% for 30 seconds, the circuit opens, immediately routing requests to the fallback mechanism without waiting for timeouts.

### 4. Idempotent Processing
Kafka guarantees at-least-once delivery. Therefore, our AI workers use the `call_id` to ensure idempotent database writes, preventing duplicate risk score records if an event is processed twice during a network partition.
