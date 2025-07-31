from pathlib import Path

def generate_index(folder_path):
    folder = Path(folder_path)
    files = [f for f in folder.glob("*.html") if f.name != "index.html"]

    if not files:
        list_items = "<li>Aucun fichier HTML trouvé.</li>"
    else:
        list_items = "\n".join(f'<li><a href="{f.name}">{f.stem}</a></li>' for f in files)

    index_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Index {folder.name}</title>
      <link rel="stylesheet" href="../css/styles.css">
      <link href="https://cdn.jsdelivr.net/npm/prismjs/themes/prism.min.css" rel="stylesheet" />
    </head>
    <body>
      <h1>{folder.name}</h1>
      <ul>
{list_items}
    </ul>
    </body>
    </html>
    """

    with open(folder / "index.html", "w", encoding="utf-8") as file:
        file.write(index_content)
    print(f"Index généré dans {folder}")

def generate_root_index(root_path):
    root = Path(root_path)
    # Trouver tous les dossiers contenant un index.html (tech folders)
    folders = [f for f in root.iterdir() if f.is_dir() and (f / "index.html").exists()]

    if not folders:
        list_items = "<li>Aucun dossier tech trouvé.</li>"
    else:
        list_items = "\n".join(f'<li><a href="{folder.name}/index.html">{folder.name}</a></li>' for folder in folders)

    index_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Accueil Notebook</title>
      <link rel="stylesheet" href="./css/styles.css">
    </head>
    <body>
      <h1>Bienvenue sur mon Notebook multi-tech</h1>
      <ul>
        {list_items}
      </ul>
    </body>
    </html>
    """

    with open(root / "index.html", "w", encoding="utf-8") as file:
        file.write(index_content)
    print(f"Index racine généré dans {root}")

if __name__ == "__main__":
    root_dir = "../"
    tech_folders = ["python", "javascript", "dotnet"]  # liste des dossiers tech

    # Générer les index dans chaque dossier tech
    for folder in tech_folders:
        folder_path = Path(root_dir) / folder
        if folder_path.exists() and folder_path.is_dir():
            generate_index(folder_path)
        else:
            print(f"Attention : le dossier {folder_path} n'existe pas ou n'est pas un dossier.")
    # Générer l'index racine
    generate_root_index(root_dir)
