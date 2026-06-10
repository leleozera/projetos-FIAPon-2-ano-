from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data_collector import fetch_neo_data, parse_neo_data
from analyzer import analyze
from rag import ask

app = FastAPI(title="AstroSight API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    pergunta: str


@app.get("/")
def root():
    return {"status": "AstroSight API rodando"}


@app.get("/dados")
def get_dados():
    """Retorna os objetos próximos à Terra dos últimos 7 dias."""
    raw = fetch_neo_data(days=7)
    objects = parse_neo_data(raw)
    return {"total": len(objects), "objetos": objects}


@app.get("/analise")
def get_analise():
    """Retorna estatísticas e clusters ML dos objetos."""
    raw = fetch_neo_data(days=7)
    objects = parse_neo_data(raw)
    result = analyze(objects)
    return result


@app.post("/chat")
def chat(request: ChatRequest):
    """Responde perguntas sobre os objetos espaciais usando RAG + Gemini."""
    raw = fetch_neo_data(days=7)
    objects = parse_neo_data(raw)
    resposta = ask(request.pergunta, objects)
    return {"pergunta": request.pergunta, "resposta": resposta}
