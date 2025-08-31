@echo off
echo Starting FastAPI server...
start cmd /k "uvicorn fastapi_backend.main:app --reload"

timeout /t 5 >nul

echo Starting Streamlit app...
start cmd /k "streamlit run app.py"
