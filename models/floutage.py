import cv2
from ultralytics import YOLO

# 📦 Classes à flouter : classe 'people' = 1 dans le modèle VisDrone
CLASSES_TO_BLUR = [1]  # adapter selon la classe 'people' dans ton modèle
MEMORY_FRAMES = 10      # nombre de frames pendant lesquelles on garde le flou

def flouter_video(input_path, output_path):
    """
    Floute les personnes et animaux domestiques dans une vidéo avec suivi ByteTrack.

    Args:
        input_path (str): Chemin vers la vidéo originale.
        output_path (str): Chemin vers la vidéo floutée.
    """
    print("[📥] Chargement du modèle YOLO avec tracking...")
    model = YOLO("models/best.pt")

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("[❌] Impossible d'ouvrir la vidéo :", input_path)
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print("[🚀] Début du traitement avec suivi des objets...")
    memory = {}  # key: track_id -> {'bbox': (x1, y1, x2, y2), 'frames_left': MEMORY_FRAMES}
    frame_idx = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model.track(frame, persist=True, tracker="bytetrack.yaml")[0]
        detections = {}

        for box in results.boxes:
            cls = int(box.cls.item())
            if cls in CLASSES_TO_BLUR and box.id is not None:
                track_id = int(box.id.item())
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(width, x2), min(height, y2)
                detections[track_id] = (x1, y1, x2, y2)

        # 🎯 Mise à jour mémoire
        for track_id in list(memory.keys()):
            if track_id not in detections:
                memory[track_id]['frames_left'] -= 1
                if memory[track_id]['frames_left'] <= 0:
                    del memory[track_id]
            else:
                memory[track_id]['bbox'] = detections[track_id]
                memory[track_id]['frames_left'] = MEMORY_FRAMES

        for track_id in detections:
            if track_id not in memory:
                memory[track_id] = {'bbox': detections[track_id], 'frames_left': MEMORY_FRAMES}

        # 📦 Appliquer le flou sur toutes les bboxes mémorisées
        for track_id, data in memory.items():
            x1, y1, x2, y2 = data['bbox']
            roi = frame[y1:y2, x1:x2]
            if roi.size > 0:
                roi_blur = cv2.GaussianBlur(roi, (51, 51), 30)
                frame[y1:y2, x1:x2] = roi_blur

        out.write(frame)
        frame_idx += 1

    cap.release()
    out.release()
    print("[✅] Vidéo floutée avec suivi enregistrée sous :", output_path)
