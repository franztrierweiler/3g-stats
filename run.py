#!/usr/bin/env python

# La ligne ci-dessus permet de lancer le script Python sur un système UNIX
# Ne pas oublier de changer les droits d'exécution du fichier par un chmod (ex: chmod 777)

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
    in_csv_path = os.path.join(dir_path, defines.PATH_IN_CSV)
    out_xlsx_path = os.path.join(dir_path, defines.PATH_OUT_XLSX)

    xls_helper.concatenate(in_csv_path,
                           defines.CSV_BASE_NAME,
                           defines.MERGED_CSV_FILE_NAME)

    xls_helper.generate_xls(in_csv_path,
                            defines.MERGED_CSV_FILE_NAME,
                            out_xlsx_path,
                            defines.CONSOLIDATED_XLSX_FILE_NAME)

    print('End at ' + str(datetime.datetime.now()))

if __name__ == '__main__':
    start()
