class Transakcja:
    def __init__(self, kwota, kategoria, typ, data):
        self.kwota = kwota
        self.kategoria = kategoria
        self.typ = typ
        self.data = data

    def __iter__(self):
        return iter([self.kwota, self.kategoria, self.typ, self.data])
