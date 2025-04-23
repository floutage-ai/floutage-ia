# app/routes.py

from flask import Blueprint, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from models.floutage import flouter_video

bp = Blueprint('main', __name__)

# 📍 Base du projet (racine)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 📁 Dossiers input/output
INPUT_FOLDER = os.path.join(BASE_DIR, 'data', 'input')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'data', 'output')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/start-process', methods=['POST'])
def start_process():
    if 'video' not in request.files:
        return "Aucun fichier vidéo envoyé", 400

    video = request.files['video']
    if video.filename == '':
        return "Fichier non sélectionné", 400

    filename = secure_filename(video.filename)
    input_path = os.path.join(INPUT_FOLDER, filename)
    video.save(input_path)

    with open(os.path.join(BASE_DIR, 'processing_temp.txt'), 'w') as f:
        f.write(f"{filename}\n")

    print("[📥] Vidéo reçue et sauvegardée, passage à la page d'attente...")
    return render_template("processing.html")

@bp.route('/process-wait')
def process_wait():
    temp_path = os.path.join(BASE_DIR, 'processing_temp.txt')

    if not os.path.exists(temp_path):
        return "Aucune vidéo en attente de traitement", 400

    with open(temp_path, 'r') as f:
        filename = f.readline().strip()

    os.remove(temp_path)

    input_path = os.path.join(INPUT_FOLDER, filename)
    processed_filename = f"processed_{os.path.splitext(filename)[0]}.mp4"
    output_path = os.path.join(OUTPUT_FOLDER, processed_filename)

    print("[🚀] Traitement vidéo :", filename)
    flouter_video(input_path, output_path)

    return render_template('result.html', output_video=processed_filename)

@bp.route('/video/<filename>')
def get_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)
