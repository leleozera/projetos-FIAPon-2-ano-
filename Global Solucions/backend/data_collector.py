import requests
import json
import os
from datetime import datetime, timedelta

NASA_API_KEY = "SUA CHAVE AQUI"  


def fetch_neo_data(days: int = 7) -> dict:
    """
    Busca Near Earth Objects dos últimos N dias na API da NASA.
    """
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")

    url = (
        f"https://api.nasa.gov/neo/rest/v1/feed"
        f"?start_date={start_date}&end_date={end_date}&api_key={NASA_API_KEY}"
    )

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Salva localmente para não repetir chamadas
    os.makedirs("data", exist_ok=True)
    with open("data/neo_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Dados salvos: {data['element_count']} objetos encontrados.")
    return data


def parse_neo_data(data: dict) -> list[dict]:
    """
    Transforma o JSON da NASA em uma lista limpa de objetos.
    """
    objects = []
    for date, neos in data["near_earth_objects"].items():
        for neo in neos:
            objects.append({
                "id": neo["id"],
                "name": neo["name"],
                "date": date,
                "is_hazardous": neo["is_potentially_hazardous_asteroid"],
                "diameter_min_km": neo["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                "diameter_max_km": neo["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                "velocity_km_h": float(
                    neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
                ),
                "miss_distance_km": float(
                    neo["close_approach_data"][0]["miss_distance"]["kilometers"]
                ),
                "orbiting_body": neo["close_approach_data"][0]["orbiting_body"],
            })
    return objects


if __name__ == "__main__":
    raw = fetch_neo_data()
    parsed = parse_neo_data(raw)
    print(f"Exemplo de objeto: {parsed[0]}")
