import sys
import os
import csv
from datetime import datetime

### Variable
chemin_journal = f"/molika/log/{datetime.now().strftime('%Y-%m-%d')}_molika.csv"
date = datetime.now().strftime("%Y-%m-%d")
date_file = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
user = os.environ.get('USER')

def condition(texte):
    # Vous devez définir cette fonction pour qu'elle fasse quelque chose avec le texte
    return "Résultat de la condition"

def logexp(texte, result):
    existe_deja = os.path.isfile(chemin_journal)

    with open(chemin_journal, mode='a', newline='') as fichier_csv:
        fieldnames = ['Date', 'Utilisateur', 'Commande_Input', 'Output']
        writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames, delimiter=';')  # Spécifier le délimiteur
        
        if not existe_deja:
            writer.writeheader()

        writer.writerow({'Date': date_file, 'Utilisateur': user, 'Commande_Input': texte, 'Output': result})

if __name__ == "__main__":
    ## permet de définir le nombre d'argument a la commande
    if len(sys.argv) > 2:
        log = sys.argv[1]
        texte = sys.argv[2]

        result = condition(texte)

        if log != "logoff":
            logexp(texte, result)
            
    else:
        print("Erreur : il manque un argument")