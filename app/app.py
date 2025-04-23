# app/app.py

from flask import Flask
from app.routes import bp as routes_bp
import os

def create_app():
    app = Flask(__name__)

    # 📂 Crée les dossiers data/input et data/output s’ils n'existent pas
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_folder = os.path.join(BASE_DIR, 'data', 'input')
    output_folder = os.path.join(BASE_DIR, 'data', 'output')

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # 📍 Configuration Flask
    app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
    app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

    # 🔗 Enregistre les routes
    app.register_blueprint(routes_bp)

    return app
