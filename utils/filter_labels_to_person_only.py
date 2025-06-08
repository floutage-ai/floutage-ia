import os

# Classes à conserver : 0 = people, 1 = pedestrian
CLASSES_TO_KEEP = {"0", "1"}

def filter_labels(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                full_path = os.path.join(root, file)
                with open(full_path, "r") as f:
                    lines = f.readlines()
                filtered = [line for line in lines if line.strip().split()[0] in CLASSES_TO_KEEP]
                with open(full_path, "w") as f:
                    f.writelines(filtered)
                print(f"{file} → {len(filtered)} lignes gardées")

# 🔧 Adapte si besoin
train_labels = "/home/azureuser/floutage-clean/data/VisDrone2019-DET/VisDrone2019-DET-train/labels"
val_labels = "/home/azureuser/floutage-clean/data/VisDrone2019-DET/VisDrone2019-DET-val/labels"

filter_labels(train_labels)
filter_labels(val_labels)
