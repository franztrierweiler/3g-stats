#!/usr/bin/env python

# Projet 3g-stats
# Fichier xls_helper.py
# Quelques utilitaires XLS avec Panda

import os
import glob
import csv
from xlsxwriter.workbook import Workbook

# Transforme un lot de fichiers CSV en fichiers XLS
# in_csv: répertoire des fichiers CSV
# out_xls: répertoire des fichiers XLSX
def convert_csv_to_xlsx(in_csv, out_xls):
    for csvfile in glob.glob(os.path.join(in_csv, '*.csv')):
        workbook = Workbook(out_xls + csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()

if __name__ == '__main__':
    print("Je suis un module")
