@echo off
echo ========================================================
echo Starting CallGuard AI Enterprise Platform...
echo ========================================================

echo [1/5] Starting core infrastructure via Docker Compose...
docker-compose up -d

echo Waiting 10 seconds for infrastructure to initialize...
timeout /t 10 /nobreak

echo [2/5] Starting API Gateway...
start "CallGuard API Gateway" cmd /k "cd services\api-gateway && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

echo [3/5] Starting AI Engine Worker...
start "CallGuard AI Engine" cmd /k "cd services\ai-engine && pip install -r requirements.txt && python -m app.main"

echo [4/5] Starting Notification Service...
start "CallGuard Notification Service" cmd /k "cd services\notifications && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload"

echo [5/5] Starting Frontend Next.js App...
start "CallGuard Frontend Dashboard" cmd /k "cd services\frontend && npm install && npm run dev"

echo.
echo ========================================================
echo CallGuard AI is booting up! 
echo.
echo - Frontend Dashboard: http://localhost:3000
echo - API Gateway Docs:   http://localhost:8000/docs
echo - Grafana:            http://localhost:3001
echo - Prometheus:         http://localhost:9090
echo ========================================================
echo.
pause
