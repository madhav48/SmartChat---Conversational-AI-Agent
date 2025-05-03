from fastapi import Request, FastAPI, status, Body, Form
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import List, Union, Literal, Dict
from .llm_client import BaseLLMClient
from .llm_client_provider import get_llm_client

import os

app = FastAPI()
current_provider = {"name": os.getenv("DEFAULT_LLM_PROVIDER", "gemini")}


class HealthCheck(BaseModel):
    status: str


# Message format: {'role': 'user' or 'assistant', 'content': str}
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: Union[str, Dict[str, str]]  # Can be extended later


class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []  # List of dicts only


class ChatResponse(BaseModel):
    response: str
    history: List[Dict[str, str]]


@app.get(
    "/health",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    summary="Perform a Health Check"
)
def health() -> HealthCheck:
    return HealthCheck(status="ok")


@app.get("/admin/provider", response_class=HTMLResponse)
async def get_provider_form():
    return f"""
    <html>
        <head><title>Change LLM Provider</title></head>
        <body>
            <h2>Current Provider: {current_provider['name'].capitalize()}</h2>
            <form method="post" action="/admin/provider">
                <label>Select Provider:</label>
                <select name="provider">
                    <option value="gemini">Gemini</option>
                    <option value="deepseek">Deep Seek</option>
                    <option value="microsoft_phi4">Microsoft PHI 4</option>
                </select>
                <button type="submit">Change</button>
            </form>
        </body>
    </html>
    """


@app.post("/admin/provider")
async def set_provider(provider: str = Form(...)):
    if provider not in ("gemini", "deepseek", "microsoft_phi4"):
        raise HTTPException(status_code=400, detail="Unsupported provider")
    current_provider["name"] = provider
    return RedirectResponse("/admin/provider", status_code=303)


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    client: BaseLLMClient = get_llm_client(current_provider['name'])
    text = client.generate(req.message, req.history)
    if isinstance(text, tuple):
        text = text[0]  # 
    new_hist = req.history + [{"role": "assistant", "content": text}]
    return ChatResponse(response=text, history=new_hist)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"errors": exc.errors()})
