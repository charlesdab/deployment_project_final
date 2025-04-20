from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Crée une instance de l'application FastAPI
app = FastAPI()

# Chargement du modèle
model = joblib.load("outputs/best_model_v5.joblib")

# Modèle d'entrée pour la requête
class PredictionRequest(BaseModel):
    input: list[list[float]]

# Colonnes attendues par le modèle
feature_columns = [
    "model_key", "mileage", "engine_power", "fuel", "paint_color",
    "car_type", "private_parking_available", "has_gps", "has_air_conditioning", 
    "automatic_car", "has_getaround_connect", "has_speed_regulator", "winter_tires"
]

@app.post("/predict")
def predict(request: PredictionRequest):
    # Convertir les données d'entrée en DataFrame avec les colonnes attendues
    X = pd.DataFrame(request.input, columns=feature_columns)
    prediction = model.predict(X).tolist()
    return {"prediction": prediction}