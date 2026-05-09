import json
from confluent_kafka import Producer
from app.core.config import settings

class KafkaProducerService:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': settings.KAFKA_BROKER_URL,
            'client.id': 'api-gateway-producer'
        })

    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    def publish_event(self, topic: str, event_data: dict):
        try:
            self.producer.produce(
                topic, 
                json.dumps(event_data).encode('utf-8'),
                callback=self.delivery_report
            )
            self.producer.poll(0) # trigger callbacks
        except Exception as e:
            print(f"Failed to publish event: {e}")
            # In a real app we might fallback to Redis or store in DB for retry

producer_service = KafkaProducerService()
