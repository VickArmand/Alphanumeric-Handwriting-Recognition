from tensorflow.keras.models import load_model
import os
import numpy as np

def data_transformation():
    pass

def predict_character(pixel_data=[]) -> dict:
    model_location = os.getenv('MODEL_LOCATION')
    if model_location:
        model_path = os.fspath(model_location)
        if os.path.exists(model_path):
            loaded_model = load_model(model_path)
            predictions = loaded_model.predict(pixel_data)
            predicted_label = np.argmax(predictions, axis=1)
            return {"success": True, "res": predicted_label}
        else:
            return {"success": False, "error": "Model path not found"}
    else:
        return {"success": False, "error": "No model path set in the environmental variable"}