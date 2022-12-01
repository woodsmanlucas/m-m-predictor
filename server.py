import pickle
import os
import numpy as np
from flask import Flask, flash, request, redirect, url_for
from keras.utils import load_img, img_to_array
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post requests has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            img = load_img(f'./uploads/{filename}', target_size=(100, 100))
            x = img_to_array(img)
            x /= 255
            x = np.expand_dims(x, axis=0)

            images = np.vstack([x])
            model = pickle.load(open('./history.pkl', 'rb'))
            prediction = model.predict(images, batch_size=10)[0][0]
            if prediction < 0.5:
                return f'This is an M&M the prediction was {prediction} 1 is definately not and M&M and 0 is an M&M'
            else:
                return f'This is not an M&M the prediction was {prediction} 1 is definately not and M&M and 0 is an M&M'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''
