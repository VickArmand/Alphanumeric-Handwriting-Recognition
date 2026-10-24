from fastapi import FastAPI
from utils import data_transformation, predict_character
app = FastAPI()

@app.get("/")
def read_root():
    return {"res": "Hello World"}

@app.post("/predict")
def predict():
    data_transformation()
    return {"res": predict_character()}
