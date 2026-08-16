@echo off
cd /d "%~dp0"
cd backend
python -m uvicorn main:app --reload --port 8000
