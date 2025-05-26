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
│   ├── __init__.py                # Initialisation de l'application Flask
│   ├── app.py                     # Lancement du serveur Flask
│   ├── routes.py                  # Définition des routes principales
│   ├── static/                    # Fichiers CSS/JS et assets statiques
│   └── templates/                 # Fichiers HTML Jinja2 pour Flask
│       ├── index.html             # Page d'accueil
│       ├── processing.html        # Page d'attente de traitement
│       └── result.html            # Page d'affichage du résultat
├── models/
│   ├── floutage.py                # Code de floutage (YOLOv8 + tracking)
│   └── best.pt                    # Modèle YOLO Medium entraîné (personnalisation VisDrone)
├── utils/
│   └── __init__.py                # Utilitaires ou helpers Python
├── main.py                        # Script principal pour CLI
├── download_model.py             # Téléchargement du modèle YOLOv8 si nécessaire
├── requirements.txt              # Liste des dépendances Python
├── Dockerfile                    # Configuration Docker du projet
├── .gitignore                    # Fichiers et dossiers ignorés par Git
├── README.md                     # Documentation du projet
├── LICENSE.txt                   # Licence d'utilisation
├── CONTRIBUTING.md               # Guide de contribution
└── .github/
    ├── CODEOWNERS                # Fichier des responsables du code
    ├── ISSUE_TEMPLATE/           # Modèles de tickets GitHub
    └── PULL_REQUEST_TEMPLATE.md  # Template de Pull Request

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
