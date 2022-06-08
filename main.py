import os

os.chdir("experiment")

# Chargement des données
os.system("python exp_load_data.py")

# Visualisation des prédictions
os.system("python exp_visualization.py")

# Algorithmes
os.system("python exp_algorithms.py")

# Résultats des régressions selon la taille de l'ensemble d'entraînement
os.system("python exp_training_size.py")

# Visualisation des résultats
os.system("python plot_exp_training_size.py")

# Test sur les hyperparamètres
os.system("python exp_hyperparam.py")

# Visualisation des résultats
os.system("python plot_exp_training_size.py")