import random
from app.core.config import settings

class AIEnginePipeline:
    def __init__(self):
        self.use_mock = settings.USE_MOCK_AI

    def _retrieve_rag_context(self, transcript: str) -> list[str]:
        # Placeholder for pgvector retrieval logic
        # SELECT * FROM known_scam_scripts ORDER BY embedding <=> query_embedding LIMIT 3;
        return ["Similar pattern found: IRS Gift Card Scam"]

    def _run_fraud_agent(self, transcript: str, rag_context: list[str]) -> float:
        if self.use_mock:
            # Deterministic fallback logic
            if "gift card" in transcript.lower() or "bank account" in transcript.lower():
                return 0.95
            return round(random.uniform(0.1, 0.4), 2)
        # Call LangChain/OpenAI here
        return 0.5

    def _run_explanation_agent(self, transcript: str, risk_score: float) -> dict:
        if risk_score > 0.8:
            return {"classification": "Scam", "reasoning": "Detected urgent request for financial information (gift cards)."}
        return {"classification": "Legit", "reasoning": "Standard conversational patterns detected."}

    def process_call(self, call_data: dict) -> dict:
        transcript = call_data.get("transcript", "")
        
        # Multi-Agent Pipeline
        rag_context = self._retrieve_rag_context(transcript)
        risk_score = self._run_fraud_agent(transcript, rag_context)
        explanation = self._run_explanation_agent(transcript, risk_score)
        
        return {
            "call_id": call_data.get("phone_number"),
            "risk_score": risk_score,
            **explanation
        }
