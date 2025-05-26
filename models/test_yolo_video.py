import cv2
from ultralytics import YOLO

print("📦 Chargement du modèle...")
model = YOLO("data/VisDrone2019-DET/runs/train/yolov8n_visdrone4/weights/best.pt")

video_path = "data/video-test.mp4"
print(f"📹 Ouverture de la vidéo : {video_path}")
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Impossible d'ouvrir la vidéo.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"📏 Taille vidéo : {width}x{height}, FPS: {fps}")

out = cv2.VideoWriter("video-test-processed.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

CLASSES_TO_BLUR = [1]  # ajuster selon VisDrone

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("📉 Fin de la vidéo.")
        break

    frame_count += 1
    print(f"🖼️ Traitement frame {frame_count}")

    results = model(frame)[0]

    for box in results.boxes:
        class_id = int(box.cls[0])
        if class_id in CLASSES_TO_BLUR:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            roi = frame[y1:y2, x1:x2]
            if roi.size == 0:
                continue
            roi_blur = cv2.GaussianBlur(roi, (99, 99), 30)
            frame[y1:y2, x1:x2] = roi_blur

    out.write(frame)

cap.release()
out.release()
print("✅ Vidéo traitée : video-test-processed.mp4")
