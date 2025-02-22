from fastapi import FastAPI
import uvicorn
import redis
import os
from pydantic import BaseModel

# Connect to Redis
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

app = FastAPI(title="MIS FastAPI Service")

class AIRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI AI service"}

@app.post("/ai/recommend")
def recommend(data: AIRequest):
    # Simple example: store & retrieve from Redis
    r.set("last_query", data.query)
    # AI logic could be integrated here (e.g., TensorFlow, PyTorch, OpenAI)
    return {"recommendation": ["Service A", "Service B"], "stored_query": data.query}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
