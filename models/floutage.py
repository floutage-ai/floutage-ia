import cv2
import numpy as np
from ultralytics import YOLO

CLASSES_TO_BLUR = [0]  # Personne = 0 dans COCO
MEMORY_FRAMES = 20
PADDING = 10  # Pour élargir la zone de flou

CLASS_NAMES = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
    'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter',
    'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
    'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase',
    'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
    'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle',
    'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
    'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet',
    'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
    'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
    'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

def flouter_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    model = YOLO('models/yolov8m.pt')
    memory = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(frame, persist=True, tracker="bytetrack.yaml", conf=0.2)[0]
        current_ids = set()

        for box in results.boxes:
            cls_id = int(box.cls.item())
            if cls_id >= len(CLASS_NAMES):
                continue

            name = CLASS_NAMES[cls_id]
            track_id = int(box.id.item()) if box.id is not None else None
            if track_id is None:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            x1, y1 = max(0, x1 - PADDING), max(0, y1 - PADDING)
            x2, y2 = min(width, x2 + PADDING), min(height, y2 + PADDING)

            memory[track_id] = {
                'bbox': (x1, y1, x2, y2),
                'cls_id': cls_id,
                'name': name,
                'frames_left': MEMORY_FRAMES
            }
            current_ids.add(track_id)

        # Décrémenter les objets absents
        for track_id in list(memory.keys()):
            if track_id not in current_ids:
                memory[track_id]['frames_left'] -= 1
                if memory[track_id]['frames_left'] <= 0:
                    del memory[track_id]

        # Appliquer flou + annotation
        for data in memory.values():
            x1, y1, x2, y2 = data['bbox']
            cls_id = data['cls_id']
            name = data['name']

            if cls_id in CLASSES_TO_BLUR:
                roi = frame[y1:y2, x1:x2]
                if roi.size > 0:
                    frame[y1:y2, x1:x2] = cv2.GaussianBlur(roi, (51, 51), 30)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            (w, h), _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(frame, (x1, y1 - 20), (x1 + w, y1), (0, 0, 255), -1)
            cv2.putText(frame, name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        out.write(frame)

    cap.release()
    out.release()
    print(f"[✅] Vidéo enregistrée : {output_path}")
