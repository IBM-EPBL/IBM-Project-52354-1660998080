from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow import keras
from keras.models import load_model
import tensorflow as tf
import os
from io import BytesIO
import pybase64

model = load_model('models/mnistCNN.h5')

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('main.html')


@app.route('/about')
def upload_file1():
    return render_template('main.html')


@app.route('/upload')
def upload_file2():
    return render_template('index6.html')


@app.route('/predict', methods=['POST'])
def upload_image_file():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(request.files['file'].stream).convert('L')
        img = img.resize((28, 28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1, 28, 28, 1)
        prediction = model.predict(im2arr)
        y_pred = np.argmax(prediction)
        #prediction_percentage = str(max(list(map(lambda x: round(x*100, 2), prediction[0]))))+"%"
        prediction_percentage = str(round(max(prediction[0])*100, 2))+"%"
        #y_pred = pd.Series(prediction,name="Label")
        filename = file.filename
        path = os.path.join("static/images", filename)
        img = Image.open(file.stream)
        file.save(path)
        #encoded_string = pybase64.b64encode(open(path, "rb").read()).decode('UTF-8')
        if filename.endswith('jpg') or filename.endswith('jpeg'):
            with BytesIO() as buf:
                img.save(buf, 'jpeg')
                image_bytes = buf.getvalue()
            encoded_string = pybase64.b64encode(image_bytes).decode()
            encoded_string = "data:image/jpeg;base64,"+encoded_string
        if filename.endswith('png'):
            with BytesIO() as buf:
                img.save(buf, 'png')
                image_bytes = buf.getvalue()
            encoded_string = pybase64.b64encode(image_bytes).decode()
            encoded_string = "data:image/png;base64,"+encoded_string
        os.remove(path)
        if (y_pred == 0 or y_pred == 1 or y_pred == 2 or y_pred == 3 or y_pred == 4 or y_pred == 5 or y_pred == 6 or y_pred == 7 or y_pred == 8 or y_pred == 9):
            return render_template("result.html", digit=y_pred, user_image=encoded_string, percentage=prediction_percentage, showcase=str(y_pred))
        else:
            return render_template("result.html", digit="No digit found.", user_image=encoded_string, percentage=prediction_percentage)
    else:
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)