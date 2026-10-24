from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils import data_transformation, predict_character
app = FastAPI()

@app.get("/")
def read_root():
    return {"res": "Hello World"}

@app.post("/predict")
def predict():
    data_transformation()
    result = predict_character([])
    if result.get('success'):
        return JSONResponse(
            content={"res": result.get('res')},
            status_code=201
        )
    else:
        return JSONResponse(
                    content={"error": result.get('error')},
                    status_code=500
                )
