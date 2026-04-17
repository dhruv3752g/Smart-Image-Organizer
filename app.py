from flask import Flask, render_template, request
import os
import gdown   # ✅ NEW
from predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
MODEL_PATH = "model/model.h5"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("model", exist_ok=True)

# ✅ DOWNLOAD MODEL IF NOT EXISTS
if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    url = "https://drive.google.com/uc?id=1409vluYH98pnBfHp3OE12fR63KdTrF_f"
    gdown.download(url, MODEL_PATH, quiet=False)
    print("Model downloaded!")

@app.route("/", methods=["GET", "POST"])
def index():
    label = None
    image_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            label = predict_image(path)
            image_path = path

    return render_template("index.html", label=label, image_path=image_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
