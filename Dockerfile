FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Installer Python et dépendances système
RUN apt update && apt install -y \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3-pip \
    git \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances via requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN python3.10 -m pip install --upgrade pip && \
    python3.10 -m pip install -r /tmp/requirements.txt

# Ajouter le kernel Jupyter dans l'environnement
RUN python3.10 -m pip install ipykernel && \
    python3.10 -m ipykernel install --user --name=floutage-ia --display-name "Floutage IA (Docker)"

# Répertoire de travail dans le conteneur (monté depuis l’hôte)
WORKDIR /workspace

# Exposer JupyterLab
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]

# Copie du script de téléchargement du modèle YOLO
COPY download_model.py /workspace/download_model.py

# Téléchargement du modèle pendant le build
RUN python /workspace/download_model.py