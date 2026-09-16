"""
app.py

Backend Flask do Assistente Cardiológico Conversacional (CardioIA - Fase 5).

Rotas:
    GET  /health         -> verifica se o serviço está no ar
    POST /session        -> cria um novo session_id de app (usado pelo frontend)
    POST /chat           -> envia uma mensagem do usuário e devolve a resposta do assistente

O backend atua apenas como ponte entre a interface e o Watson Assistant:
não guarda o conteúdo clínico, apenas o session_id necessário para manter o
contexto da conversa.
"""

import uuid
import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

import config
from local_simulator import simulate_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cardioia-backend")

app = Flask(__name__)
CORS(app)  # permite que a interface (frontend) em outra origem consuma a API

if config.SIMULATION_MODE:
    logger.warning(
        "SIMULATION_MODE ativo: respondendo com regras locais, sem chamar o "
        "Watson Assistant de verdade. Preencha o .env com credenciais reais "
        "para desativar."
    )
    watson_client = None
else:
    from watson_client import WatsonAssistantClient
    watson_client = WatsonAssistantClient()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/session", methods=["POST"])
def create_session():
    """Gera um novo identificador de sessão para o app (não é o session_id do Watson)."""
    session_id = str(uuid.uuid4())
    return jsonify({"session_id": session_id}), 201


@app.route("/chat", methods=["POST"])
def chat():
    """
    Espera um JSON no corpo da requisição:
        { "session_id": "<id gerado por /session>", "message": "texto do usuário" }

    Devolve:
        {
            "replies": ["...", "..."],
            "intent": "nome_da_intent" | null,
            "confidence": 0.87 | null,
            "session_id": "..."
        }
    """
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")
    message = (data.get("message") or "").strip()

    if not session_id:
        return jsonify({"error": "session_id é obrigatório. Chame /session primeiro."}), 400
    if not message:
        return jsonify({"error": "message não pode ser vazio."}), 400

    try:
        if config.SIMULATION_MODE:
            result = simulate_message(message)
            result["session_id"] = session_id
        else:
            result = watson_client.send_message(session_id, message)
    except Exception as exc:  # falha de rede/credenciais/serviço do Watson
        logger.exception("Erro ao consultar o Watson Assistant")
        return (
            jsonify(
                {
                    "error": "Não foi possível falar com o assistente no momento.",
                    "detail": str(exc),
                }
            ),
            502,
        )

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.FLASK_PORT, debug=config.FLASK_DEBUG)
