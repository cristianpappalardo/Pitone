import sqlite3
from modelli.dipendente import Dipendente

class DipendenteServizio:
    #creo la connessione al database    
    conn = sqlite3.connect("parcheggio.sqlite")

    #aggiungo un nuovo dipendente al database
    def aggiungi_dipendente(self, conn):
        dipendente = self.salva_dipendente()
        cur = conn.cursor()
        cur.execute('''INSERT INTO dipendenti (nome, cognome, num_cell, email) VALUES (?, ?, ?, ?)''', 
                    (dipendente.nome, dipendente.cognome, dipendente.num_cell, dipendente.email))
        return "Nuovo dipendente aggiunto con successo"

    #istanzio un nuovo dipendente con i dati inseriti dall'utente
    def salva_dipendente(self):
        nome = input("Inserisci il nome del dipendente").strip().lower()
        cognome = input("Inserisci il cognome del dipendente").strip().lower()
        num_cell = input("Inserisci il numero di cellulare del dipendente").strip().lower()
        email = input("Inserisci l'email del dipendente").strip().lower()
        #controllo che i campi non siano vuoti
        if not nome : return "Il campo nome non puo essere vuoto"
        if not cognome : return "Il campo cognome non puo essere vuoto"
        if not num_cell : return "Il campo num_cell non puo essere vuoto"
        if not email : return "Il campo email non puo essere vuoto"


        dipendente = Dipendente(None, nome, cognome, num_cell, email)

        return dipendente
    
    #visualizzo i dipendenti presenti nel database
    def visualizza_dipendenti(self, conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM dipendenti')
        dipendenti = cur.fetchall()
        return dipendenti

    #visualizzo un dipendente in base all'id inserito dall'utente
    def get_dipendente_by_id(self, conn):
        dipendente_id = self.inserisci_id()
        cur = conn.cursor()
        cur.execute('SELECT * FROM dipendenti WHERE dipendente_id = ?', (dipendente_id,))
        dipendente = cur.fetchone()
        return dipendente

    #inserisco l'id del dipendente 
    def inserisci_id(self):
        dipendente_id = input("Inserisci l'id del dipendente").strip().lower()
        if not dipendente_id : return "Il campo id non puo essere vuoto"
        return dipendente_id

    #cancello un dipendente
    def cancella_dipendente(self, conn):
        dipendente_id = self.inserisci_id()
        cur = conn.cursor()
        cur.execute('DELETE FROM dipendenti WHERE dipendente_id = ?', (dipendente_id,))
        return "Dipendente cancellato con successo"

    #chiudo la connessione
    conn.commit()
    conn.close()