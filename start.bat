@echo off
cd api
python -m uvicorn index:app --reload --port 8765
