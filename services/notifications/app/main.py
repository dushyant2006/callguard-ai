import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from confluent_kafka import Consumer, KafkaError

app = FastAPI(title="CallGuard AI - Notifications Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                pass

manager = ConnectionManager()

async def consume_kafka_alerts():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'notification-service-group',
        'auto.offset.reset': 'latest'
    })
    consumer.subscribe(['alert-events'])
    
    while True:
        await asyncio.sleep(0.1) # Yield to event loop
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        if msg.error():
            continue
            
        event_data = msg.value().decode('utf-8')
        await manager.broadcast(event_data)

@app.on_event("startup")
async def startup_event():
    # Run Kafka consumer in background
    asyncio.create_task(consume_kafka_alerts())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # We don't expect messages from client, just keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
