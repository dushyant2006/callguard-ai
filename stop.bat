@echo off
echo ========================================================
echo Stopping CallGuard AI Enterprise Platform...
echo ========================================================

echo Spinning down Docker Compose infrastructure...
docker-compose down

echo.
echo All background infrastructure stopped. 
echo Note: Please manually close the command prompt windows that were opened for the API, AI Engine, Notifications, and Frontend.
echo ========================================================
pause
