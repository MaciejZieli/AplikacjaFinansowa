#aplikacja do zarządzania finansami
from Folder_Classy.menadzer_finansow import MenadzerFinansow
from Folder_Classy.sql import Baza_danych
from Folder_Classy.transakcje import Transakcja
from csv import eksportuj

# transakcje = odczyt()

finanse=MenadzerFinansow([])

bazadanych=Baza_danych()

while True:
    print("1, wyświetl saldo")
    print("2, wyświetl historię transakcji")
    print("3, dodaj przychód")
    print("4, dodaj wydatek, wstaw minus przed kwotą")

    wybor = int(input("wybierz cyfrę 1-4"))

    if wybor == 1:
        print(f"Aktualne saldo: {bazadanych.oblicz_saldo()}")
    elif wybor == 2:
        finanse.historia_transakcje()
    elif wybor == 3 or wybor == 4:
        kwota = float(input("wpisz kwotę transakcji"))
        kategoria = input()
        typ = input()
        data = input("%Y-%m-%d")
        bazadanych.dodaj_transakcje(Transakcja(kwota, kategoria, typ, data))
    else:
        print("Nieprawidłowy wybór, spróbuje 1-4")
        break

eksportuj(finanse.transakcje)









