import os

# Cookiecutter remplace cette variable par ton choix dans le terminal
chosen_language = "{{ cookiecutter.language }}"

# Dictionnaire des linters/fichiers à supprimer selon le langage choisi
linters_to_purge = {
    "python": ["eslint.config.mjs"],
    "javascript": ["pyproject.toml"],
    "go": ["eslint.config.mjs", "pyproject.toml"],
    "autre": ["eslint.config.mjs", "pyproject.toml"]
}

# Nettoyage automatique
if chosen_language in linters_to_purge:
    for file_to_delete in linters_to_purge[chosen_language]:
        file_path = os.path.join(os.getcwd(), file_to_delete)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"🧹 Nettoyage : suppression de {file_to_delete} (non requis pour {chosen_language})")
