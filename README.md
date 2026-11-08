# 🚀 Cookiecutter POC Universal

> Un template de projet intelligent, multi-langage et hautement automatisé pour amorcer des Preuves de Concept (POC) en moins de 30 secondes sous WSL2, avec une gouvernance DevOps de niveau professionnel intégrée dès le premier commit.

---

## 🎯 Vision & Objectifs

Quand on enchaîne les POCs (en Python, JavaScript, Go, etc.), configurer manuellement les linters, les hooks Git et la CI/CD représente une friction inutile. Ce template implémente une approche **"zéro-friction et auto-gouvernée"** :
* **Agagnostique :** Un seul point d'entrée pour n'importe quel langage.
* **Propre :** Suppression automatique des fichiers superflus selon le langage choisi.
* **Normé :** Validation locale et continue des commits (Conventional Commits).
* **Automatisé :** Gestion des versions (SemVer) et des changelogs sans intervention humaine.

---

## 🛠️ Ce qui est inclus dans chaque POC généré

1. **Génération conditionnelle :**
   * Intègre les configurations adaptées (`pyproject.toml` pour Python, `eslint.config.mjs` pour JavaScript).
   * Nettoie automatiquement les fichiers non désirés via un hook `post_gen_project.py`.
2. **Gouvernance Git locale (`pre-commit`) :**
   * Bloque le code non formaté (espaces superflus, fins de fichiers).
   * Force le respect strict de la norme **Conventional Commits** (`feat:`, `fix:`, `chore:`).
3. **CI/CD & Release Automatique (GitHub Actions) :**
   * Pipeline de validation universel (`pre-commit/action`).
   * **Semantic Release & Keep a Changelog** piloté par *Release Please* pour générer automatiquement les tags, les versions et le fichier `CHANGELOG.md` à chaque fusion sur `main`.

---

## 📂 Structure du Meta-Dépôt Template

```text
cookiecutter-poc-universal/
├── .github/
│   └── workflows/
│       └── ci-release.yml             # CI/CD & Release du template lui-même
├── hooks/
│   └── post_gen_project.py            # Script de nettoyage post-génération
├── .pre-commit-config.yaml            # Linters & Conventional Commits du template
├── .release-please-config.json        # Configuration Keep a Changelog / Release Please
├── .release-please-manifest.json      # Registre de version du template
├── cookiecutter.json                  # Formulaire interactif de configuration
├── README.md                          # Documentation du template
│
└── {{cookiecutter.project_slug}}/     # Le squelette injecté dans tes futurs POCs
    ├── .github/workflows/ci.yml
    ├── .pre-commit-config.yaml
    ├── eslint.config.mjs
    ├── pyproject.toml
    └── README.md

```

---

## 📦 Prérequis (Environnement WSL2 / Linux)

Assure-toi d'avoir installé les outils d'isolation nécessaires :

```bash
# 1. Installer pipx si ce n'est pas déjà fait
sudo apt update && sudo apt install -y pipx
pipx ensurepath

# 2. Installer Cookiecutter globalement
pipx install cookiecutter

```

---

## 🚀 Utilisation : Comment créer un nouveau POC ?

1. **Générer le projet** depuis ton terminal WSL2 :
```bash
cookiecutter [https://github.com/TON-PSEUDO/cookiecutter-poc-universal](https://github.com/TON-PSEUDO/cookiecutter-poc-universal)

```


*(Réponds aux questions du terminal : nom du projet, auteur, choix du langage parmi `python`, `javascript`, `go`, `autre`)*
2. **Entrer dans le répertoire généré et activer les hooks :**
```bash
cd mon-nouveau-poc
pre-commit install --install-hooks

```


3. **Coder et commiter (aux normes Conventional Commits) :**
```bash
git add .
git commit -m "feat(api): initialisation du serveur de test"

```



---

## ⚙️ Maintenir et faire évoluer ce Template

Ce dépôt template est lui-même versionné et auto-gouverné. Si tu souhaites le modifier ou y ajouter des linters :

* Les modifications des règles globales se font dans `{{cookiecutter.project_slug}}/`.
* Les releases du template sont gérées automatiquement par la CI. Respecte les Conventional Commits sur ce dépôt pour incrémenter sa propre version !

---

## 📄 Licence

Distribué sous licence MIT. Voir `LICENSE` pour plus de détails.
