class MenadzerFinansow:
    def __init__(self, transakcje,):
        self.transakcje = transakcje

    def dodaj_transakcje(self, transakcja):
        self.transakcje.append(transakcja)

    def historia_transakcje(self):
        for transakcja in self.transakcje:
            print(f"{transakcja.kategoria}:{transakcja.data}:{transakcja.typ}:{transakcja.kwota}")

    def saldo(self):
        x=0
        for transakcja in self.transakcje:
            x+=transakcja.kwota
        return x

    def filtrowanie_transakcje(self, data):
        return list(filter(lambda x:x.data == data, self.transakcje))

    def sortowanie_transakcje(self):
        return sorted(self.transakcje, key=lambda x:x.data)





