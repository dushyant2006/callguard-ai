import json
import time
from confluent_kafka import Consumer, KafkaError
from app.core.config import settings
from app.services.ai_pipeline import AIEnginePipeline

class CallEventConsumer:
    def __init__(self):
        self.consumer = Consumer({
            'bootstrap.servers': settings.KAFKA_BROKER_URL,
            'group.id': 'ai-engine-group',
            'auto.offset.reset': 'earliest'
        })
        self.pipeline = AIEnginePipeline()
        self.topic = 'call-events'
        self.dlq_topic = 'call-events-dlq'

    def start(self):
        self.consumer.subscribe([self.topic])
        print(f"Started consuming from {self.topic}...")
        
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(f"Consumer error: {msg.error()}")
                        break
                
                event_data = json.loads(msg.value().decode('utf-8'))
                self.process_event(event_data)
                
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()

    def process_event(self, event_data: dict):
        MAX_RETRIES = 3
        for attempt in range(MAX_RETRIES):
            try:
                print(f"Processing event: {event_data['phone_number']}")
                result = self.pipeline.process_call(event_data)
                print(f"Result: {result}")
                # Publish to alert-events topic
                # ...
                break # Success
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2 ** attempt) # Exponential backoff
        else:
            print(f"Max retries reached. Sending to DLQ: {event_data}")
            # Send to DLQ logic here
