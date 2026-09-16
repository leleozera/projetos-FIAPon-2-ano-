"""
config.py

Carrega as credenciais e parâmetros do Watson Assistant a partir de variáveis
de ambiente (arquivo .env em desenvolvimento). Nunca commitar o .env real —
apenas o .env.example com placeholders.
"""

import os
from dotenv import load_dotenv

load_dotenv()

WATSON_API_KEY = os.getenv("WATSON_API_KEY", "")
WATSON_URL = os.getenv("WATSON_URL", "")
# ID do Skill (workspace) — aparece em "Skill details" > "Skill ID" na tela do
# skill dentro do watsonx Assistant. Usado pela API v1 (message por workspace).
WATSON_WORKSPACE_ID = os.getenv("WATSON_WORKSPACE_ID", "")
WATSON_VERSION = os.getenv("WATSON_VERSION", "2021-06-14")

FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"

# Se True (ou se as credenciais do Watson não estiverem preenchidas), o backend
# usa local_simulator.py em vez de chamar o Watson de verdade. Serve só para
# testar o fluxo/backend/interface antes de configurar o Watson real.
SIMULATION_MODE = (
    os.getenv("SIMULATION_MODE", "false").lower() == "true"
    or not (WATSON_API_KEY and WATSON_URL and WATSON_WORKSPACE_ID)
)


def validate():
    missing = [
        name
        for name, value in [
            ("WATSON_API_KEY", WATSON_API_KEY),
            ("WATSON_URL", WATSON_URL),
            ("WATSON_WORKSPACE_ID", WATSON_WORKSPACE_ID),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Variáveis de ambiente do Watson Assistant não configuradas: "
            + ", ".join(missing)
            + ". preencha .env com suas credenciais."
        )