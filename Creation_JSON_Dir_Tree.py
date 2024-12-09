import os
import json
from tkinter import Tk
from tkinter.filedialog import askdirectory


def get_directory_size(path):
    """
    Calculer récursivement la taille d'un répertoire.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Vérifie si le fichier est accessible pour éviter des erreurs.
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size


def analyze_directory(base_path):
    """
    Analyser récursivement le contenu d'un répertoire et retourner les informations sous forme de liste.
    """
    data = []
    for root, dirs, files in os.walk(base_path):
        # Calculer la taille du répertoire courant
        dir_size = get_directory_size(root)
        # Ajouter les informations du répertoire à la liste
        data.append({"nom": root, "taille": dir_size})
        print(".",end="")
    return data


def save_to_json(data, output_file="Arborescence.json"):
    """
    Enregistrer les données dans un fichier JSON.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def select_directory():
    """
    Ouvrir un sélecteur pour choisir le répertoire à analyser.
    """
    root = Tk()
    root.withdraw()  # Masquer la fenêtre principale de Tkinter
    directory = askdirectory(title="Sélectionnez un répertoire à analyser")
    root.destroy()  # Fermer Tkinter après la sélection
    return directory


def main():
    print("Ouverture du sélecteur de répertoire...")
    base_directory = select_directory()

    if not base_directory:
        print("Aucun répertoire sélectionné. Fin du programme.")
        return

    print(f"Répertoire sélectionné : {base_directory}")

    output_file = "Arborescence.json"  # Nom par défaut du fichier JSON
    print(f"Les résultats seront enregistrés dans le fichier : {output_file}")

    print("Analyse en cours...")
    directory_data = analyze_directory(base_directory)
    print()
    print(f"Enregistrement des résultats dans {output_file}...")
    save_to_json(directory_data, output_file)

    print(f"Analyse terminée avec succès. Le fichier JSON a été sauvegardé sous : {os.path.abspath(output_file)}")


if __name__ == "__main__":
    main()
