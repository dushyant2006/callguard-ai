from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user") # user, analyst, admin
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    calls = relationship("CallRecord", back_populates="user")

class CallerProfile(Base):
    __tablename__ = "caller_profiles"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    reputation_score = Column(Integer, default=50) # 0-100 (100 = safe)
    category = Column(String, default="unknown") # safe, unknown, spam, scam, robocall
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CallRecord(Base):
    __tablename__ = "call_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    caller_id = Column(Integer, ForeignKey("caller_profiles.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    duration = Column(Integer, default=0)
    status = Column(String, default="pending") # pending, allowed, blocked, flagged
    transcript = Column(Text, nullable=True)
    
    user = relationship("User", back_populates="calls")
    caller = relationship("CallerProfile")
    analysis = relationship("RiskAnalysis", back_populates="call", uselist=False)

class RiskAnalysis(Base):
    __tablename__ = "risk_analysis"
    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(Integer, ForeignKey("call_records.id"), unique=True)
    ai_model_version = Column(String)
    risk_score = Column(Float, default=0.0) # 0.0 to 1.0 (1.0 = high risk)
    classification = Column(String) # scam, spam, legit
    intent_summary = Column(Text)
    reasoning = Column(Text)
    confidence = Column(Float)
    
    call = relationship("CallRecord", back_populates="analysis")
