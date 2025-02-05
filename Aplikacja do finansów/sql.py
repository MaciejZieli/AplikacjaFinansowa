import sqlite3


class Baza_danych:
    def __init__(self):
        # conn zarządza połączeniem z bazą
        self.conn = sqlite3.connect('transaction.db')
        # cursor mamy do wykonywania komend na bazie
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Tabela_Transakcji(data text, kategoria text, typ text, kwota real)""")
        self.conn.commit()

    def dodaj_transakcje(self, transakcja):
        with self.conn:
            self.cursor.execute("INSERT INTO Tabela_Transakcji VALUES (:data, :kategoria, :typ, :kwota)",{'data':transakcja.data, 'kategoria':transakcja.kategoria,'typ':transakcja.typ,'kwota':transakcja.kwota})

    def oblicz_saldo(self):
        self.cursor.execute("SELECT SUM(kwota) FROM Tabela_Transakcji")
        return self.cursor.fetchone()[0]


        
    
