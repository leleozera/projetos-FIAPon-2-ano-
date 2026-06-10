import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def analyze(objects: list[dict]) -> dict:
    """
    Recebe lista de NEOs e retorna estatísticas + clusters KMeans.
    """
    df = pd.DataFrame(objects)

    # Estatísticas gerais
    stats = {
        "total_objetos": len(df),
        "potencialmente_perigosos": int(df["is_hazardous"].sum()),
        "velocidade_media_km_h": round(df["velocity_km_h"].mean(), 2),
        "distancia_media_km": round(df["miss_distance_km"].mean(), 2),
        "diametro_medio_km": round(df["diameter_max_km"].mean(), 4),
    }

    # Clustering por velocidade e distância (KMeans com 3 grupos)
    features = df[["velocity_km_h", "miss_distance_km", "diameter_max_km"]].copy()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(scaled)

    cluster_summary = (
        df.groupby("cluster")[["velocity_km_h", "miss_distance_km", "diameter_max_km"]]
        .mean()
        .round(2)
        .reset_index()
        .to_dict(orient="records")
    )

    return {
        "stats": stats,
        "clusters": cluster_summary,
        "objects": df.to_dict(orient="records"),
    }
