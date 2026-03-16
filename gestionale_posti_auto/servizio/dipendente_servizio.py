import sqlite3
from modelli.dipendente import Dipendente

class DipendenteServizio:
    #aggiungo un nuovo dipendente al database
    @staticmethod
    def aggiungi_dipendente(conn):
        try:
            dipendente = DipendenteServizio.salva_dipendente()

            cur = conn.cursor()
            cur.execute('''INSERT INTO dipendenti (nome, cognome, num_cell, email) VALUES (?, ?, ?, ?)''', 
                        (dipendente.nome, dipendente.cognome, dipendente.num_cell, dipendente.email))
            conn.commit()
            return "Nuovo dipendente aggiunto con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.IntegrityError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante l'aggiunta del dipendente"

    #istanzio un nuovo dipendente con i dati inseriti dall'utente
    @staticmethod
    def salva_dipendente():
        nome = input("Inserisci il nome del dipendente: ").strip().lower()
        cognome = input("Inserisci il cognome del dipendente: ").strip().lower()
        num_cell = input("Inserisci il numero di cellulare del dipendente: ").strip()
        email = input("Inserisci l'email del dipendente: ").strip().lower()
        #controllo che i campi non siano vuoti
        if not nome:
            raise ValueError("Il campo nome non puo essere vuoto")
        if not cognome:
            raise ValueError("Il campo cognome non puo essere vuoto")
        if not num_cell:
            raise ValueError("Il campo num_cell non puo essere vuoto")
        if not email:
            raise ValueError("Il campo email non puo essere vuoto")

        dipendente = Dipendente(None, nome, cognome, num_cell, email) #creo un nuovo dipendente con id None, poiché l'id viene generato automaticamente dal database

        return dipendente
    
    #visualizzo i dipendenti presenti nel database
    @staticmethod
    def visualizza_dipendenti(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM dipendenti')
        dipendenti = cur.fetchall()
        return dipendenti

    #visualizzo un dipendente in base all'id inserito dall'utente
    @staticmethod
    def get_dipendente_by_id(conn):
        #chiedo all'utente di inserire l'id del dipendente che vuole visualizzare, e controllo che l'id sia valido
        try:
            dipendente_id = DipendenteServizio.inserisci_id("Inserisci l'id del dipendente: ")
        except ValueError:
            return None

        cur = conn.cursor()
        cur.execute('SELECT * FROM dipendenti WHERE dipendente_id = ?', (dipendente_id,))
        dipendente = cur.fetchone()
        return dipendente

    #inserisco l'id del dipendente 
    @staticmethod
    #funzione che chiede all'utente di inserire un id, e controlla che l'id sia valido (non vuoto e numerico)
    def inserisci_id(messaggio="Inserisci l'id: "): #
        valore = input(messaggio).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)

    #cancello un dipendente
    @staticmethod
    def cancella_dipendente(conn):
        try:
            dipendente_id = DipendenteServizio.inserisci_id("Inserisci l'id del dipendente da cancellare: ")

            cur = conn.cursor()
            cur.execute('DELETE FROM dipendenti WHERE dipendente_id = ?', (dipendente_id,))
            conn.commit()
            if cur.rowcount == 0:
                raise ValueError("Nessun dipendente trovato con l'id indicato")
            return "Dipendente cancellato con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione del dipendente"