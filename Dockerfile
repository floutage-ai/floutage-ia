FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Installer Python, pip, OpenCV et dépendances système
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

# Copier et installer les dépendances
COPY requirements.txt /tmp/requirements.txt
RUN python3.10 -m pip install --upgrade pip && \
    python3.10 -m pip install -r /tmp/requirements.txt

# Copier le code dans le conteneur
WORKDIR /app
COPY . /app

# Exposer le port de Flask
EXPOSE 5000

# Commande pour lancer l'app Flask
CMD ["python3.10", "main.py"]
