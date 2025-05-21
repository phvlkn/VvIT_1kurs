from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

@app.get("/summary/{topic}")
def get_summary(topic: str):
    return {"summary": wikipedia.summary(topic)}

@app.get("/search/")
def search_topic(q: str):
    return {"results": wikipedia.search(q)}

class TopicRequest(BaseModel):
    topic: str

class TopicSummary(BaseModel):
    summary: str

@app.post("/summary", response_model=TopicSummary)
def post_summary(req: TopicRequest):
    return TopicSummary(summary=wikipedia.summary(req.topic))