from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db.session import engine, Base
from app.core.config import settings
from app.api.endpoints import auth, calls

# In a real app we'd use Alembic, but for this fast MVP scaffold we can do this:
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(calls.router, prefix=f"{settings.API_V1_STR}/calls", tags=["calls"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "api-gateway"}
