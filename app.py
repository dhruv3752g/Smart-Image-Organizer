from flask import Flask, render_template, request
import os
from predict import predict_image

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    app.run(debug=True)