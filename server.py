import os
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from hashlib import sha256
from datetime import datetime
import per as model

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hash_filename(filename):
    filename, ext = filename.rsplit('.', 1)
    unique_filename = f"{secure_filename(filename)}-{int(datetime.now().timestamp())}"

    hash_filename = sha256(unique_filename.encode('utf-8')).hexdigest()

    return f"{hash_filename}.{ext}"

def upload_file(file):
    filename = secure_filename(file.filename)
    hashed_filename = hash_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], hashed_filename)
    file.save(file_path)

    file_url = f"/uploads/{hashed_filename}"

    return file_url

@app.route('/uploads/<filename>')
def serve_upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/v1/predict', methods=['POST'])
def predict_output():
    if 'file' not in request.files:
        return (
            {
                'status': 'failed',
                'message': 'No file given.'
            }, 
            400
        )
    
    file = request.files['file']

    if file.filename == '':
        return (
            {
                'status': 'failed',
                'message': 'No selected file.'
            },
            400
        )
    
    if file and allowed_file(file.filename):
        image_path = upload_file(file)
        model_result = model.predict(image_path)

        return {
            'status': 'success',
            'data': {
                'image': image_path,
                'message': 'Image uplaod successful',
                'result': model_result
            }
        }

if __name__ == '__main__':
    app.run(debug=True)