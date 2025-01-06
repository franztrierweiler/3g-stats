#!/usr/bin/env python

# Projet 3g-stats
# Fichier run.py
# Point d'entrée du projet, lit les fichiers et réalise le traitement complet.

import os
import defines
import xls_helper
import datetime

def start():
    # Init 
    print(os.path.basename(__file__))
    print('Start at ' + str(datetime.datetime.now()))
    
    # Tous les chemins sont relatifs au répertoire de run.py
    dir_path = os.path.dirname(os.path.realpath(__file__))
    in_csv = os.path.join(dir_path, defines.PATH_IN_CSV)
    out_csv = os.path.join(dir_path, defines.PATH_OUT_XLSX)

    xls_helper.convert_csv_to_xlsx(in_csv)

    print('End at ' + str(datetime.datetime.now()))

if __name__ == '__main__':
    start()
