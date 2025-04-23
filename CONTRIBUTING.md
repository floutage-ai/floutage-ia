# 🤝 Contribuer au projet Floutage AI

Bienvenue dans le projet **Floutage AI** !\
Ce guide est destiné à tous les membres de notre équipe pour assurer une collaboration fluide et efficace.

---

## 👥 Membres de l’équipe

- **Alexandre** *(validateur principal)*
- **Hamza**
- **Dorra**
- **Joselio**

---

## ⚙️ Installation locale (Docker + JupyterLab)

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/hamzaQuebec/floutage-ai.git
   cd floutage-ai
   ```

2. Construire l’image Docker :
   ```bash
   docker build -t floutage-ai .
   ```

3. Lancer JupyterLab avec volume monté :

### 💡 Choix du volume selon le terminal :

| Terminal                 | Commande recommandée                          |
|--------------------------|-----------------------------------------------|
| **CMD (Windows)**        | `-v "%cd%:/workspace"`                        |
| **PowerShell (Windows)** | `-v "${PWD}:/workspace"`                      |
| **Bash/Linux/macOS**     | `-v "$(pwd):/workspace"`                      |

### ✅ Exemple complet (CMD) :
```cmd
docker run -p 8888:8888 -v "%cd%:/workspace" -it floutage-ai
```

---

## 🌱 Structure Git et branches

Chaque membre travaille dans sa propre branche de développement personnelle :

| Membre      | Branche            |
|-------------|---------------------|
| Hamza       | `hamza-dev`         |
| Dorra       | `dorra-dev`         |
| Joselio     | `joselio-dev`       |
| Alexandre   | `alexandre-dev`     |

La branche principale est `main`. Seules les versions **stables validées** y sont fusionnées.

---

## 🔄 Cycle de travail collaboratif

1. Chaque membre développe dans **sa propre branche `prenom-dev`**
2. Une fois les changements prêts, il crée une **Pull Request (PR)** vers `alexandre-dev`
3. **Alexandre**, en tant que validateur désigné (`CODEOWNERS`), relit, commente et valide les PR
4. Quand tout est stable, **Alexandre fusionne vers `main`**

> 🔒 La branche `main` est protégée. Aucune modification directe n’est possible. Toute mise à jour passe par une PR approuvée par Alexandre.

---

## 🧪 Vérification des branches

- Voir les branches locales : `git branch`
- Voir les branches distantes : `git branch -r`
- Tout voir : `git branch -a`

---

## 🧱 Convention de nommage

- `prenom-dev` : branche de travail personnelle
- `feature/description` : pour une fonctionnalité précise (facultatif)
- `fix/description` : pour une correction de bug spécifique

---

## 🧾 Convention de commit

Format recommandé :
```bash
git commit -m "type: message court"
```

Exemples de types : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

---

## 📬 Contact

En cas de doute ou de bug bloquant :

- Ouvrir une **Issue**
- Ou contactez **Hamza** sur Teams

Merci pour votre implication 🙌
