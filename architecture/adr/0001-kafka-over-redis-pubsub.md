# Architecture Decision Record: Kafka over Redis Pub/Sub

## Status
Accepted

## Context
We need a robust, event-driven messaging system to handle high-throughput call ingestion, AI analysis processing, and alert broadcasting. The system must support asynchronous workflows, retry mechanisms, and decouple our microservices. The primary candidates for the local and production environments were Apache Kafka and Redis Pub/Sub.

## Decision
We decided to use **Apache Kafka** as the primary event streaming system, with Redis acting only as a fallback and state/cache layer.

## Consequences
### Positive
- **Durability**: Kafka persists events to disk, allowing consumers to replay missed events if a service goes down or a bug is deployed. Redis Pub/Sub is fire-and-forget; if a consumer is offline, the message is lost.
- **Consumer Groups**: Kafka natively supports consumer groups, enabling horizontal scaling of our `ai-engine` workers. Multiple AI workers can pull from the same topic partition without duplicating work.
- **Dead-Letter Queues (DLQ)**: Kafka's robust ecosystem makes implementing retry and DLQ patterns straightforward, which is critical for resilient AI failure handling.

### Negative
- **Operational Complexity**: Kafka requires Zookeeper (or KRaft) and uses more memory and CPU compared to Redis. This makes local Docker Compose heavier.
- **Learning Curve**: Kafka configuration (offsets, partitions, acks) is significantly more complex than Redis.

## Mitigation
To ease local development, we provide a lightweight fallback mode in the architecture using Redis Pub/Sub for reviewers who cannot run Kafka locally, while keeping the production architecture Kafka-first.
