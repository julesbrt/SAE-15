import pandas as pd
import glob
import os

def pandas():

    ## Récupération de toutes les données des fichiers .csv :

    fichiers_csv = glob.glob('..\..\data\\raw\sending*.csv')

    ## Les données sont regroupés dans une liste (ici "raw_liste") :

    raw_liste = []
    for file in fichiers_csv:
        raw_liste.append(pd.read_csv(file,sep=";"))

    ## Mise en forme des données dans la liste raw dans un fichier .csv :

    df = pd.concat(raw_liste, axis=0, sort=False)
    df.to_csv('..\..\data\processed\\resultat.csv',index=False)

    ## Vérification du succès de l'opération (Il affichera true si le fichier existe déjà) :

    if os.path.isfile('..\..\data\processed\\resultat.csv') is True:
        print("Opération effectuée avec succès.")
    else:
        print("Erreur !")

pandas()
