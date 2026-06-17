from fastapi import FastAPI
import pandas as pd
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = (
    BASE_DIR
    / "data"
    / "processed"
    / "dataset_final.csv"
)

df = pd.read_csv(csv_path)

@app.get("/")
def inicio():
    return {"mensaje": "API de Vehículos"}

@app.get("/vehiculos")
def vehiculos():
    return df.head(20).to_dict(orient="records")

@app.get("/estadisticas")
def estadisticas():
    try:
        return {
            "cantidad": len(df),
            "precio_promedio": float(df["precio_usd"].mean())
        }
    except Exception as e:
        return {"error": str(e)}