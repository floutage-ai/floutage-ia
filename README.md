# Floutage AI – README

Bienvenue dans **Floutage AI**, une application basée sur l’intelligence artificielle pour le floutage automatique des personnes et des informations sensibles dans des vidéos filmées par drone.

---

## 🚀 Objectif du projet

Créer une application performante qui :
- Détecte les humains et éléments privés (visages, plaques ...)
- Floute automatiquement ces éléments dans les vidéos
- Fonctionne en environnement Docker avec interface JupyterLab ou via une interface web Flask

---

## 🧠 Technologies principales

- Python 3.10+
- Ultralytics YOLOv8
- OpenCV / MediaPipe
- Flask (interface web)
- JupyterLab (via Docker)

---

## ⚙️ Lancement rapide (via Docker + JupyterLab)

```bash
# Build de l'image Docker
docker build -t floutage-ai .

# Lancement du conteneur avec montage du dossier local
# (exemple pour terminal Windows CMD)
docker run -p 8888:8888 -v "%cd%:/workspace" -it floutage-ai
```

> 📁 Les notebooks ou codes sont accessibles dans `/workspace` une fois Jupyter lancé.

---

## 🌐 Lancement Flask (interface web)

```bash
# Depuis le dossier racine du projet
python app/app.py
```

> Interface accessible sur `http://127.0.0.1:5000`

---

## 📂 Structure du dépôt

```
floutage-ia/
├── app/
│   ├── __init__.py          # Initialisation de l'app Flask
│   ├── app.py               # Point d'entrée Flask
│   ├── routes.py            # Définition des routes
│   ├── static/              # Fichiers CSS/JS
│   └── templates/           # HTML pour Flask
│       ├── index.html
│       ├── processing.html
│       └── result.html
├── data/                    # Dossier pour vidéos d'entrée et sortie
├── models/
│   └── floutage.py          # Traitement vidéo (YOLOv8 + OpenCV)
├── utils/                   # Fonctions auxiliaires
├── main.py                  # Script principal CLI
├── download_model.py        # Script de téléchargement YOLOv8
├── yolov8n.pt               # Fichier de modèle YOLOv8
├── requirements.txt         # Dépendances Python
├── Dockerfile               # Image Docker
├── .gitignore.txt
├── README.md
├── LICENSE.txt
├── CONTRIBUTING.md
└── .github/                 # Fichiers de contribution GitHub
    ├── CODEOWNERS
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## ⬇️ Téléchargement automatique du modèle YOLOv8

Un script (`download_model.py`) vérifie si le modèle `yolov8n.pt` est présent.  
S’il est absent ou vide, il sera automatiquement téléchargé.

---

## 👤 Responsable de validation des contributions

Les Pull Requests vers la branche `main` doivent être **validées par Alexandre (@alexmoreau-elixotech)**.  
Cette validation est requise automatiquement grâce au fichier [`CODEOWNERS`](.github/CODEOWNERS).

---

## 🤝 Contribuer

Voir le fichier [`CONTRIBUTING.md`](CONTRIBUTING.md) pour :
- Le workflow Git en équipe
- La création de branches (`prenom-dev`)
- Les conventions de commit
- Le rôle d’Alexandre comme validateur principal

---

## 📬 Contact

Pour toute demande, contactez **Hamza** sur Teams ou ouvrez une Issue.

---

Merci pour vos contributions 🙌
