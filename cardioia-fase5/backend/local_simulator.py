"""
local_simulator.py

Simulador local do fluxo conversacional, usado apenas para TESTES quando as
credenciais reais do Watson Assistant ainda não estão configuradas.

Reproduz em Python simples a mesma lógica de intents/entities/dialog nodes
definida em cardioia-assistente-skill.json, para validar o backend e a
interface antes de plugar o Watson de verdade.

Isso NÃO substitui o Watson Assistant no entregável final — é só uma muleta
de desenvolvimento/teste.
"""

import re

SINTOMAS = {
    "dor no peito": ["dor no peito", "aperto no peito", "peito doendo"],
    "falta de ar": ["falta de ar", "dificuldade para respirar", "cansaço para respirar"],
    "palpitação": ["palpita", "coração acelerado", "coração disparado"],
    "tontura": ["tontura", "tonteira", "vertigem"],
    "cansaço": ["cansaço", "cansaco", "fadiga", "sem energia"],
}

URGENCIA_ALTA = ["forte", "intensa", "muito forte", "insuportável", "insuportavel", "muito ruim"]
URGENCIA_BAIXA = ["leve", "fraca", "baixa"]

SAUDACAO = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "tudo bem", "eae", "e ai"]
DESPEDIDA = ["tchau", "até mais", "ate mais", "obrigado", "obrigada", "encerrar", "valeu"]
INFO_CONDICAO = ["o que é", "o que e", "me explica", "explique", "o que causa", "entender sobre"]
CONSULTA = ["marcar", "consulta", "cardiologista", "agendar", "atendido", "atendimento"]


def _contains_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def _detect_sintoma(text: str):
    for sintoma, variações in SINTOMAS.items():
        if _contains_any(text, variações):
            return sintoma
    return None


def _detect_urgencia(text: str):
    if _contains_any(text, URGENCIA_ALTA):
        return "alta"
    if _contains_any(text, URGENCIA_BAIXA):
        return "baixa"
    return "moderada" if _detect_sintoma(text) else None


def simulate_message(text: str) -> dict:
    """Mesma assinatura de retorno do watson_client.send_message, mas 100% local."""
    normalized = text.lower().strip()

    sintoma = _detect_sintoma(normalized)
    if sintoma:
        urgencia = _detect_urgencia(normalized)
        if urgencia == "alta":
            reply = (
                f"Isso pode ser sério. Procure atendimento médico de emergência "
                f"imediatamente (pronto-socorro ou SAMU 192). Não vou conseguir "
                f"avaliar '{sintoma}' com segurança por aqui."
            )
        else:
            reply = (
                f"Entendi que você está sentindo {sintoma}. Há quanto tempo isso "
                f"está acontecendo, e a intensidade é leve, moderada ou forte?"
            )
        return {"replies": [reply], "intent": "Relatar_Sintoma", "confidence": 0.9}

    if _contains_any(normalized, INFO_CONDICAO):
        reply = (
            "Posso explicar de forma geral sobre condições cardiológicas comuns, "
            "mas qualquer diagnóstico precisa ser confirmado por um cardiologista. "
            "Sobre qual condição você quer saber mais?"
        )
        return {"replies": [reply], "intent": "Info_Condicao", "confidence": 0.85}

    if _contains_any(normalized, CONSULTA):
        reply = (
            "Recomendo agendar uma consulta com um cardiologista para avaliação "
            "presencial. Quer que eu explique quais informações levar para a consulta?"
        )
        return {"replies": [reply], "intent": "Orientacao_Consulta", "confidence": 0.85}

    if _contains_any(normalized, DESPEDIDA):
        reply = (
            "Fico à disposição. Cuide-se e, diante de qualquer sintoma forte, "
            "procure atendimento médico. Até logo!"
        )
        return {"replies": [reply], "intent": "Despedida", "confidence": 0.9}

    if _contains_any(normalized, SAUDACAO):
        reply = "Oi! Como você está se sentindo hoje?"
        return {"replies": [reply], "intent": "Saudacao", "confidence": 0.9}

    reply = (
        "Desculpe, não entendi bem. Você pode descrever o sintoma que está "
        "sentindo ou perguntar sobre alguma condição cardiológica?"
    )
    return {"replies": [reply], "intent": None, "confidence": None}
