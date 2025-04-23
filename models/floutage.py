import cv2
from ultralytics import YOLO

# 📦 Classes à flouter : personne = 0, chat = 15, chien = 16 dans COCO
CLASSES_TO_BLUR = [0, 15, 16]  # person, cat, dog

def flouter_video(input_path, output_path):
    """
    Floute les personnes et animaux domestiques dans une vidéo.
    
    Args:
        input_path (str): Chemin vers la vidéo originale.
        output_path (str): Chemin vers la vidéo floutée.
    """
    # ✅ Charger le modèle YOLOv8 (modèle léger 'n' = nano)
    model = YOLO('yolov8n.pt')

    # ✅ Ouvrir la vidéo originale
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("[❌] Impossible d'ouvrir la vidéo :", input_path)
        return

    # 📐 Récupérer infos sur la vidéo
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 🎥 Créer l'objet pour enregistrer la vidéo de sortie
    fourcc = cv2.VideoWriter_fourcc(*"avc1")  # ou "H264" si "avc1" ne marche pas
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print("[🚀] Début du traitement de la vidéo...")

    while True:
        success, frame = cap.read()
        if not success:
            break  # fin de la vidéo

        # 🧠 Appliquer la détection avec YOLO
        results = model(frame, verbose=False)[0]

        for box in results.boxes:
            cls = int(box.cls.item())  # classe détectée
            if cls in CLASSES_TO_BLUR:
                # 📦 Coordonnées du rectangle de la détection
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # 🔒 S'assurer qu'on reste dans les dimensions de l'image
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(width, x2), min(height, y2)

                # 🎯 Appliquer le flou sur la zone détectée
                roi = frame[y1:y2, x1:x2]
                roi_blur = cv2.GaussianBlur(roi, (51, 51), 30)
                frame[y1:y2, x1:x2] = roi_blur

        # 💾 Ajouter la frame floutée dans la vidéo finale
        out.write(frame)

    # ✅ Libérer les ressources
    cap.release()
    out.release()
    print("[✅] Vidéo floutée enregistrée sous :", output_path)
