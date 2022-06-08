# Projet Python - Modèle de prédiction de l'année d'une chanson

## Structure du projet

Le projet contient 4 dossiers :
- **experiment** contient tous les scripts permettant de tester les fonctions du paquet RegPy et d'expérimenter les différentes méthodes de régression.
- **input** contient toutes les données nécessaires pour les tests et les expérimentations.
- **output** contient les sorties des différents scripts de experiment.
- **regpy** est le module développé lors de ce projet, il contient toutes les fonctionnalités utilisées pour les expériences et leur test.


## Comment faire fonctionner le module RegPy

Le module **regpy** ne contient pas de code principal (if __name__ == "__main__"). Il n'est donc pas conçu pour être utilisé comme script principal. On l'utilise en l'important dans un fichier de la manière suivante :

> from sys import path
> sys.path(<REGPY_PATH>)
> import regpy as rp

L'ensemble des fonctions des sous modules sont alors importées. Quelques exemples d'appels de fonctions :

> rp.load_data(<INPUT_PATH>) # Importation des données
> rp.LinearRegressionRidge(0.1) # Instanciation de la régression de Ridge

## Comment faire fonctionner les scripts d'expérimentation

Pour faire fonctionner un script, il suffit de se placer dans le répertoire experiment et d'interpréter le script avec Python3 comme ci-dessous :

> cd <PATH_EXPERIMENT>
> python <SCRIPT_NAME>

## Fonctionnement sur Spyder
Essayer d'ouvir chaque fichier à partir de l'onglet "fichier" de la fenêtre en haut à droite pour ne pas avoir de problème de chemin.