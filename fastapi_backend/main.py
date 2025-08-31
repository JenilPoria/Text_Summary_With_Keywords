from fastapi import FastAPI
# from api import router 
from fastapi_backend.api import router   # ❌ won't work (dash invalid in imports)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI backend running!"}

# app.include_router(router,prefix="/api")
app.include_router(router)