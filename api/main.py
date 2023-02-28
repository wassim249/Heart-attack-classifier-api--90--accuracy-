import os
import sys
from pickle import load
from fastapi import FastAPI
from Person import Person

app = FastAPI(title="Heart Attack Prediction API", description="Simple API for predicting heart attack", version="1.0")

@app.on_event("startup")
async def load_model():
    global model
    model = load(open(f"../model/heart_disease.pkl", "rb"))

@app.post("/predict" , tags=["Prediction"])
async def get_prediction(person : Person):
    data = dict(person)['data']
    prediction = model.predict([data]).tolist()
    return {
        "prediction": prediction,
        "data": data,
    }
    
# command to run the API
# uvicorn main:app --reload
