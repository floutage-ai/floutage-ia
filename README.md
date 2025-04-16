# 🕵️‍♂️ Floutage AI – Détection et floutage automatique des personnes dans les vidéos

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Jupyter](https://img.shields.io/badge/JupyterLab-enabled-orange?logo=jupyter)](https://jupyter.org/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](./CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 🎯 Objectif du projet

**Floutage AI** est une application d’intelligence artificielle développée en Python permettant de :
- détecter automatiquement les personnes dans des vidéos,
- flouter ces personnes pour garantir leur anonymat,
- exploiter des modèles comme YOLOv8 et OpenCV,
- utiliser une interface interactive via **JupyterLab**.

---

## ⚙️ Stack technique

- Python 3.10
- OpenCV
- Ultralytics YOLOv8
- Torch (CPU ou GPU)
- Docker (environnement isolé)
- JupyterLab (interface interactive)

---

## 🏗️ Installation locale avec Docker

### 1. Cloner le dépôt

```bash
git clone https://github.com/floutage-ai/floutage-ia.git
cd floutage-ai
```
---
### 2. Construire l’image Docker
```bash

docker build -t floutage-ai .
```

### 3. Lancer l’environnement JupyterLab
```bash

docker run -p 8888:8888 -v "$(pwd)":/workspace -it floutage-ai
```

Ouvre ton navigateur et accède à :
👉 http://localhost:8888

Sélectionne le kernel Floutage IA (Docker) dans JupyterLab

---

## 📁 Arborescence du projet
``` lua

floutage-ai/
├── Dockerfile
├── requirements.txt
├── notebooks/
│   └── main.ipynb
├── videos/
│   └── (tes vidéos à flouter)
├── output/
│   └── (vidéos floutées)
├── .gitignore
├── README.md
└── LICENSE
```
---

## 🧑‍💻 Branches de travail & Rôles


master	    Version stable du projet

hamza-dev	Développement de Hamza

dorra-dev	Développement de Dorra

joselio-dev	Développement de Joselio

---

## 🤝 Contribution

Clonez le repo

Travaillez sur votre branche (hamza-dev, etc.)

Créez une Pull Request vers master une fois une fonctionnalité prête

Suivez les bonnes pratiques de versionnage et de nommage

---

## 📜 Licence

Ce projet est sous licence MIT – voir le fichier LICENSE pour plus d'informations.

---

## 📬 Contact & Collaboration
Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à proposer une pull request.