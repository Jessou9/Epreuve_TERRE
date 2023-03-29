# Exercice Nom du programme
# Créez un programme qui affiche son nom de fichier.

import os #importer un fichier exterieur
namefile = os.path.basename(__file__)
print(namefile)
