#!/usr/bin/env python

# La ligne ci-dessus permet de lancer le script Python sur un système UNIX
# Ne pas oublier de changer les droits d'exécution du fichier par un chmod (ex: chmod 777)

# Projet 3g-stats
# Fichier xls_helper.py
# Quelques utilitaires XLS avec Panda

import os
import glob
import pandas
import defines

# Concatène un lot de fichiers CSV en un seul fichier CSV
# Realise auparavant un traitement sur les colonnes rssiOrange
# in_csv: répertoire des fichiers CSV où sera aussi écrit le fichier concaténé
# in_csv_base_name: motif de recherche des fichiers CSV à lire
# out_csv_file_name: nom du fichier CSV final
def concatenate_clean_csv(in_csv, in_csv_base_name, out_csv_file_name):
    dfs = []
    for csv_file in glob.glob(os.path.join(in_csv, in_csv_base_name)):
        df = pandas.read_csv(csv_file, encoding="utf-16",
                             delimiter=";")
        
        # Transformer les valeurs de la colonne rssiOrange
        # Pour cela, nous itérons le dataframe issu du fichier CSV
        for ind, data in df.iterrows():
            # Ne pas traiter le header
            if (ind >= 0):
                value = str(df.loc[ind, "rssiOrange"])
                # La cellule est vide ou contient une chaine de type x/y, alors détruire la ligne
                if ("/" not in value):
                    # Si la cellule n'est pas de type x/y alors la détruire
                    df.drop (labels=ind, inplace=True)
                else:
                    # Ne garder que le numérateur exprimé dans la chaine de type x/y, alors détruire la ligne
                    df.loc[ind, "rssiOrange"] = value.split("/")[0]
                    # Si cette valeur est supérieure au seuil RSSI, détruire la ligne
                    if (int(df.loc[ind, "rssiOrange"]) > defines.RSSI_MAX_VALUE):
                        # Il m'a fallu deux heures pour trouver que inplace=True est requis lors du drop, sinon la ligne n'est pas effacée
                        df.drop (labels=ind, inplace=True)

        
        dfs.append(df)

        if (defines.VERBOSE == "YES"):
            print("- Traité: lecture et concaténation de " + csv_file)
            print("-> Axes: " + str(df.axes))
            print("--------\n")

    df = pandas.concat(dfs,
                       ignore_index=True)

    # Très logique: le paramètre delimiter de read_csv s'appelle sep dans to_csv
    df.to_csv(os.path.join(in_csv, out_csv_file_name),
              index=False, sep=";", encoding="utf-16")

# Transforme un lot de fichiers CSV en fichiers XLS
# in_csv: répertoire du fichier CSV source
# in_csv_file_name: nom du fichier CSV source
# out_xlxs: répertoire du fichier XLXS produit
# out_xlxs_file_name: nom du fichier XLXS à produire
def generate_xls(in_csv, in_csv_file_name, out_xlsx, out_xlsx_file_name):
    new_dataFrame = pandas.read_csv(os.path.join(in_csv, in_csv_file_name),
                                    encoding="utf-16",
                                    delimiter=";")
    
    new_dataFrame.to_excel(os.path.join(out_xlsx, out_xlsx_file_name),
                           sheet_name="Subjects", index=False)

if __name__ == '__main__':
    print("Je suis un module")
