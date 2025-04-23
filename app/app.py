from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'data/input'
OUTPUT_FOLDER = 'data/output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    video = request.files.get('video')
    if video:
        path = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(path)
        # TODO: Appeler ta fonction floutage ici (models/floutage.py)
        return redirect(url_for('result'))
    return "Aucune vidéo reçue"

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
