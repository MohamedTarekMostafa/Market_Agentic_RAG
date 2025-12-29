from fastapi import FastAPI
from pydantic import BaseModel
from processor import get_chain

app = FastAPI()
report_chain = get_chain()

class RequestSchema(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: RequestSchema):
    response = report_chain.invoke({"query": request.query})
    return {"answer": response}

