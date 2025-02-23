import os
import redis
import jwt
from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="MIS FastAPI Service")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretjwt")  # same as in .env

class AIRequest(BaseModel):
    query: str

def verify_jwt(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth_header[len("Bearer "):]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        # optional: check user ID or roles in payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI AI service"}

@app.post("/ai/recommend")
def recommend(data: AIRequest, _: None = Depends(verify_jwt)):
    # Check last query in Redis
    r.set("last_query", data.query)
    # Real AI logic could be integrated (TensorFlow, PyTorch, etc.)
    return {
        "recommendation": ["Service A", "Service B"],
        "stored_query": data.query
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
