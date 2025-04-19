# Floutage AI – README

Bienvenue dans **Floutage AI**, une application basée sur l’intelligence artificielle pour le floutage automatique des personnes et des informations sensibles dans des vidéos filmées par drone.

---

## 🚀 Objectif du projet

Créer une application performante qui :
- Détecte les humains et éléments privés (visages, plaques, numéros de maison)
- Floute automatiquement ces éléments dans les vidéos
- Fonctionne en environnement Docker avec interface JupyterLab

---

## 🧠 Technologies principales

- Python 3.10+
- OpenCV / YOLO / MediaPipe
- JupyterLab (via Docker)

---

## ⚙️ Lancement rapide (via Docker)

```bash
# Build l'image Docker
docker build -t floutage-ai .

# Lance le conteneur avec JupyterLab
# (exemple pour terminal Windows CMD)
docker run -p 8888:8888 -v "%cd%:/workspace" -it floutage-ai
```

> 📁 Les notebooks sont accessibles dans `/workspace` une fois Jupyter lancé.

---

## 📂 Structure du dépôt

```
floutage-ai/
├── notebooks/         # Notebooks Jupyter (travail principal)
├── output/            # Résultats du traitement (non versionné)
├── videos/            # Données d’entrée (non versionnées)
├── .github/           # CODEOWNERS, workflows, etc.
├── .gitignore         # Fichiers/dossiers exclus
├── Dockerfile         # Image Docker de l'environnement
├── requirements.txt   # Dépendances Python
├── README.md          # Présent fichier
└── CONTRIBUTING.md    # Guide pour les contributeurs
```

---

## 👤 Responsable de validation des contributions

Les Pull Requests vers la branche `main` doivent être **validées par Alexandre (@alexmoreau-elixotech)**. 
Cette validation est requise automatiquement grâce au fichier [`CODEOWNERS`](.github/CODEOWNERS).

Aucune modification directe sur `main` n’est autorisée sans validation.

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
