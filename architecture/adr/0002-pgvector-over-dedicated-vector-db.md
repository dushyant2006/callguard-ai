# Architecture Decision Record: pgvector over Dedicated Vector DB

## Status
Accepted

## Context
The AI engine implements Retrieval-Augmented Generation (RAG) to compare incoming call transcripts against known scam scripts, phishing phrases, and historical fraud patterns. We need a vector database to store and query these embeddings using cosine similarity. Options included `pgvector` (a PostgreSQL extension), Pinecone, Qdrant, or Weaviate.

## Decision
We decided to use **PostgreSQL with the `pgvector` extension** rather than a standalone or cloud-hosted dedicated vector database.

## Consequences
### Positive
- **Infrastructure Simplicity**: By using `pgvector`, we keep our relational data (users, call logs, feedback) and vector data (scam scripts, call embeddings) in the same database instance. This reduces infrastructure sprawl.
- **ACID Compliance**: We can perform atomic transactions across relational tables and vector tables (e.g., saving a call record and its vector embedding simultaneously).
- **Cost & Local Dev**: Completely free and easy to run locally in a single Docker container, unlike proprietary cloud vector DBs.

### Negative
- **Performance at Extreme Scale**: Dedicated vector databases often use highly optimized algorithms (like custom HNSW implementations) out of the box that might perform faster than `pgvector` at the multi-billion vector scale.

## Mitigation
`pgvector` now supports HNSW indexes, which significantly closes the performance gap. Given that our dataset of known scam scripts will likely be in the millions (not billions) of rows, `pgvector` offers the best tradeoff between operational simplicity and performance.
