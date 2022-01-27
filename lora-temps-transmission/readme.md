# Projet temps de transmission LoRa

## Synopsis
Le projet temps de transmission Lora consiste à analyser le temps de transmission de données avec la technologie LoRa. 

## Données
Les données obtenus à partir du Fipy Pycomm et ont été sauvegardées dans le dossier *data/raw*. La technologie LoRa permet à un utilisateur de choisir le facteur d'étalement, 
la bande passante ainsi que le taux de redondance des bits de données lors de la transmission. C'est pourquoi les données de l'expérience regroupent toutes les transmissions avec 
les différents paramètres possible. Afin de mieux comprendre les données générées, le dossier references contient le code source embarqué par le Pycomm qui a permis d'enregistrer les données.

## Tâches
Les tâches demandées dans ce projet sont les suivantes.

OK 1. Écrire un programme qui fusionne les fichiers csv (*dossier src/data*).
2. Établir pour chaque variable le nombre de valeurs manquantes et aberrante ainsi que le pourcentage que cela représente.
3. Établir le nombre et le pourcentage d'observations qui ont des valeurs aberrantes et/ou manquantes.
4. Calculer le temps d'envoi des données.
OK 5. Définir les fonctions ComputeMean (moyenne) et ComputeMedian et calculer (*src/model/model.py*) le temps médian de transmission pour chaque facteur d'étalement (spreading factor).
6. Afficher la courbe qui montre la relation entre la taille des données et le temps d'envoi associée en fonction du facteur d'étalement (spreading factor),
la bande passante et la taux de redondance (coding rate).



