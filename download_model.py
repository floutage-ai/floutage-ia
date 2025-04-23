import os
from pathlib import Path
from urllib.request import urlretrieve

MODEL_PATH = Path("yolov8n.pt")
MODEL_URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"

def download_yolo_model():
    if not MODEL_PATH.exists():
        print("📥 Téléchargement du modèle YOLOv8n...")
        urlretrieve(MODEL_URL, MODEL_PATH)
        print("✅ Modèle téléchargé avec succès : yolov8n.pt")
    else:
        print("✔️ Modèle déjà présent.")

if __name__ == "__main__":
    download_yolo_model()