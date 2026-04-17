import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json

model = tf.keras.models.load_model("model/model.h5")

# Load class indices
with open("model/class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse mapping
class_names = {v: k for k, v in class_indices.items()}

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    class_index = int(np.argmax(predictions))

    return class_names[class_index]