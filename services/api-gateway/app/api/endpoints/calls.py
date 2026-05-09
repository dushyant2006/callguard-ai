from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from pydantic import BaseModel

router = APIRouter()

class CallIngestSchema(BaseModel):
    phone_number: str
    duration: int = 0
    transcript: str = ""

@router.post("/ingest")
def ingest_call(payload: CallIngestSchema, db: Session = Depends(get_db)):
    # 1. Look up caller reputation
    # 2. Save initial call record to DB
    # 3. Publish event to Kafka for AI processing
    
    # Placeholder for Kafka producer
    _event = {
        "event_type": "call_ingested",
        "phone_number": payload.phone_number,
        "transcript": payload.transcript
    }
    
    return {"status": "ingested", "message": "Call sent to AI Engine for processing"}
