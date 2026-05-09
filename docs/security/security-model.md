# Security Model

CallGuard AI employs a defense-in-depth security strategy.

## Authentication & Authorization
- **JWT Lifecycles**: We use short-lived access tokens (15 minutes) and long-lived HTTP-only refresh tokens (7 days). This mitigates XSS attacks stealing session tokens.
- **RBAC**: Endpoints are protected via role-based access control. Users can only access their own call histories. Analysts and Admins have elevated privileges to view global metrics and DLQs.

## Data Protection
- **No Hardcoded Secrets**: All secrets (API keys, DB passwords, JWT signing keys) are injected via environment variables.
- **SQL Injection Prevention**: We strictly use SQLAlchemy ORM parameter binding; raw string interpolation in SQL queries is banned.
- **Pydantic Validation**: Every incoming API request payload is strictly typed and validated by Pydantic, preventing Malicious Payload attacks.

## API Protection & Rate Limiting
- **Rate Limiting**: Redis is used to implement a Sliding Window rate limiter (e.g., max 100 requests / minute / IP) to prevent DDoS and brute-force login attempts.
- **Security Headers**: The FastAPI backend injects standard security headers (`Strict-Transport-Security`, `X-Content-Type-Options`, `Content-Security-Policy`).

## AI Prompt Guardrails
To prevent prompt injection from malicious caller transcripts:
1. Transcripts are sanitized (HTML/Markdown stripped).
2. The GenAI prompt uses explicit system delimiters (e.g., `---BEGIN TRANSCRIPT---`) to separate instructions from user data.
3. Output is validated against a Pydantic schema to ensure the AI does not hallucinate arbitrary JSON structures.
