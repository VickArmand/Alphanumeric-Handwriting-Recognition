from tensorflow.keras.models import load_model
import os
import numpy as np

def data_transformation():
    pass

def predict_character(pixel_data):
    model_location = os.getenv('MODEL_LOCATION')
    loaded_model = load_model(model_location)
    predictions = loaded_model.predict(pixel_data)
    predicted_label = np.argmax(predictions, axis=1)
    return predicted_label