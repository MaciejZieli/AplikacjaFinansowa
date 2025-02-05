import os

import csv
from Folder_Classy.transakcje import Transakcja


def eksportuj(transactions_to_csv):
#with open - ścieżka do pliku  w - zapisa    r - odczyt

    with open("nazwa_pliku.csv", mode='w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        for transaction in transactions_to_csv:
            wr.writerow(list(transaction))


def reader(csv_file):
    pass


def reader(csv_file):
    pass


def odczyt():
    if os.path.exists("nazwa_pliku.csv"):
        with open("nazwa_pliku.csv", mode='r') as csv_file:
            reader = reader(csv_file)
            result=[]
            for row in reader:
                result.append(Transakcja(float(row[0]), row[1], row[2], row[3]))
            return result
    else:
        return[]

