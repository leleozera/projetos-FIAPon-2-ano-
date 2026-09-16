"""
watson_client.py

Wrapper de integração com o IBM Watson Assistant, usando a API v1 (baseada em
workspace/skill), que é a forma direta de conversar com um Dialog Skill
clássico como o que foi importado via cardioia-assistente-skill.json.

Referência: IBM Watson Assistant v1 API
https://cloud.ibm.com/apidocs/assistant/assistant-v1
"""

from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import config


class WatsonAssistantClient:
    """Encapsula a comunicação com o Watson Assistant (API v1 / workspace)."""

    def __init__(self):
        authenticator = IAMAuthenticator(config.WATSON_API_KEY)
        self.assistant = AssistantV1(
            version=config.WATSON_VERSION,
            authenticator=authenticator,
        )
        self.assistant.set_service_url(config.WATSON_URL)
        self.workspace_id = config.WATSON_WORKSPACE_ID

        # contexto de conversa por sessão do app: { app_session_id: context_dict }
        # o "context" é o que o Watson usa pra lembrar em que ponto do diálogo
        # cada usuário está (equivalente à sessão da API v2).
        self._contexts = {}

    def send_message(self, app_session_id: str, text: str) -> dict:
        """
        Envia a mensagem do usuário ao Watson Assistant (workspace) e devolve
        uma resposta normalizada:

            {
                "replies": ["texto 1", "texto 2", ...],
                "intent": "nome_da_intent_detectada" | None,
                "confidence": 0.0-1.0 | None,
                "session_id": "<id interno da sessão do app>"
            }
        """
        context = self._contexts.get(app_session_id, {})

        result = self.assistant.message(
            workspace_id=self.workspace_id,
            input={"text": text},
            context=context,
        ).get_result()

        # guarda o contexto atualizado pra próxima mensagem dessa sessão
        self._contexts[app_session_id] = result.get("context", {})

        output = result.get("output", {})
        replies = output.get("text", [])

        intents = output.get("intents", [])
        top_intent = intents[0]["intent"] if intents else None
        top_confidence = intents[0]["confidence"] if intents else None

        if not replies:
            replies = ["Desculpe, não entendi. Pode reformular sua pergunta?"]

        return {
            "replies": replies,
            "intent": top_intent,
            "confidence": top_confidence,
            "session_id": app_session_id,
        }

    def close_session(self, app_session_id: str) -> None:
        """Limpa o contexto de conversa dessa sessão, reiniciando o diálogo."""
        self._contexts.pop(app_session_id, None)