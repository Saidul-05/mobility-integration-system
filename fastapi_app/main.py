import os
import redis
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="MIS FastAPI Service")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

class AIRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI AI service"}

@app.post("/ai/recommend")
def recommend(data: AIRequest):
    # Simple example storing last query in Redis
    r.set("last_query", data.query)
    # Real AI logic could be integrated here (TensorFlow, PyTorch, OpenAI)
    return {
        "recommendation": ["Service A", "Service B"],
        "stored_query": data.query
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
