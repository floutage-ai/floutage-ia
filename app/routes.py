# app/routes.py

from flask import Blueprint, render_template, request, send_from_directory
from flask import flash, redirect, url_for ,send_file
from werkzeug.utils import secure_filename
import os
from models.floutage import flouter_video
from utils.carte_generator import creer_carte_mosaique
from utils.tile_generator import generer_tuiles

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


bp = Blueprint('main', __name__)

# 📍 Base du projet (racine)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 📁 Dossiers input/output
INPUT_FOLDER = os.path.join(BASE_DIR, 'data', 'input')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'data', 'output')
CARTES_FOLDER = os.path.join(BASE_DIR, 'data', 'cartes')
#image_path = os.path.join(CARTES_FOLDER, image_filename)
#jgw_path = os.path.join(CARTES_FOLDER, jgw_filename)



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/floutage')
def floutage():
    return render_template('floutage.html') 


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

@bp.route("/video/<filename>")
def afficher_video(filename):
    video_path = os.path.join("data", "output", filename)
    return send_file(video_path, mimetype='video/mp4')

@bp.route('/carte')
def carte():
    images = [f for f in os.listdir(CARTES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif'))]
    return render_template("carte.html", images=images)


@bp.route('/upload-mosaique', methods=['POST'])
def upload_mosaique():
    if 'image' not in request.files or 'jgw' not in request.files:
        flash("❌ Vous devez envoyer à la fois une image et un fichier .jgw.", "error")
        return redirect(url_for('main.carte'))

    image = request.files['image']
    jgw = request.files['jgw']

    if image.filename == '' or jgw.filename == '':
        flash("⚠️ Les deux fichiers doivent être sélectionnés.")
        return redirect(url_for('main.carte'))

    if not allowed_file(image.filename) or not jgw.filename.lower().endswith('.jgw'):
        flash("❌ Formats incorrects. Image = .jpg/.png | JGW = .jgw", "error") 
        return redirect(url_for('main.carte'))

    image_filename = secure_filename(image.filename)
    jgw_filename = os.path.splitext(image_filename)[0] + ".jgw"

    # ✅ Définir les chemins
    image_path = os.path.join(CARTES_FOLDER, image_filename)
    jgw_path = os.path.join(CARTES_FOLDER, jgw_filename)

    # ✅ Sauvegarder les fichiers
    image.save(image_path)
    jgw.save(jgw_path)

    flash("✅ Carte et fichier .jgw téléversés avec succès.","success")

    # ✅ Utiliser : générer les tuiles et afficher
    generer_tuiles(image_path, os.path.join(BASE_DIR, "data/tiles"))
    return render_template("carte_interactive.html", base_name=os.path.splitext(image_filename)[0].lower())


@bp.route('/ouvrir-mosaique', methods=['POST'])
def ouvrir_mosaique():
    filename = request.form.get('filename')
    if not filename:
        return "Aucun fichier sélectionné", 400

    image_path = os.path.join(CARTES_FOLDER, filename)
    generer_tuiles(image_path, os.path.join(BASE_DIR, "data/tiles"))
    return render_template("carte_interactive.html", base_name=os.path.splitext(filename)[0].lower())

@bp.route('/cartes/<filename>')
def get_carte(filename):
    return send_from_directory(CARTES_FOLDER, filename)

@bp.route("/cartes_interactives/<filename>")
def afficher_carte_interactive(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@bp.route('/tiles/<path:filename>')
def serve_tile(filename):
    print(f"[🧭] Tuile demandée : {filename}")
    tile_dir = os.path.join(BASE_DIR, 'data', 'tiles')
    return send_from_directory(tile_dir, filename)
