import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def build_context_from_data(objects: list[dict]) -> str:
    lines = []
    for obj in objects:
        perigo = "SIM" if obj["is_hazardous"] else "NÃO"
        lines.append(
            f"Objeto: {obj['name']} | Data: {obj['date']} | "
            f"Perigoso: {perigo} | "
            f"Velocidade: {obj['velocity_km_h']:.0f} km/h | "
            f"Distância da Terra: {obj['miss_distance_km']:.0f} km | "
            f"Diâmetro estimado: {obj['diameter_max_km']:.4f} km"
        )
    return "\n".join(lines)


def ask(question: str, objects: list[dict]) -> str:
    context = build_context_from_data(objects)

    prompt = f"""Você é um assistente especialista em astronomia e objetos próximos à Terra.
Use os dados abaixo para responder à pergunta do usuário em português.

DADOS DOS OBJETOS ESPACIAIS:
{context}

PERGUNTA: {question}

Responda de forma clara e objetiva baseando-se nos dados fornecidos."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente especialista em astronomia e objetos próximos à Terra. Responda sempre em português. Seja direto e objetivo: responda a pergunta em 2 a 4 frases no máximo, apresentando o resultado principal primeiro e depois uma breve justificativa com os dados. Não elabore além do necessário. Use quebras de linha para separar itens quando houver lista. Não use emojis."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content