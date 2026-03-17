import sqlite3
from modelli import Studente

class StudenteServizio:
    #aggiungo un nuovo studente al database
    @staticmethod
    def add_student(conn):
        try:
            studente = StudenteServizio.save_student()

            cur = conn.cursor()
            cur.execute('''INSERT INTO studenti (nome, cognome, email) VALUES (?, ?, ?)''', 
                        (studente.nome, studente.cognome, studente.email))
            conn.commit()
            return "Nuovo studente aggiunto con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.IntegrityError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante l'aggiunta del studente"

    #istanzio un nuovo studente con i dati inseriti dall'utente
    @staticmethod
    def save_student():
        nome = input("Inserisci il nome del studente: ").strip().lower()
        cognome = input("Inserisci il cognome del studente: ").strip().lower()
        email = input("Inserisci l'email del studente: ").strip().lower()
        #controllo che i campi non siano vuoti
        if not nome:
            raise ValueError("Il campo nome non puo essere vuoto")
        if not cognome:
            raise ValueError("Il campo cognome non puo essere vuoto")
        if not email:
            raise ValueError("Il campo email non puo essere vuoto")

        studente = Studente(None, nome, cognome, email) #creo un nuovo studente con id None, poiché l'id viene generato automaticamente dal database

        return studente
    
    #visualizzo i studenti presenti nel database
    @staticmethod
    def get_all_students(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM studenti')
        studenti = cur.fetchall()
        return studenti

    #visualizzo un studente in base all'id inserito dall'utente
    @staticmethod
    def get_student_by_id(conn):
        #chiedo all'utente di inserire l'id del studente che vuole visualizzare, e controllo che l'id sia valido
        try:
            studente_id = StudenteServizio.insert_id("Inserisci l'id del studente: ")
        except ValueError:
            return None

        cur = conn.cursor()
        cur.execute('SELECT * FROM studenti WHERE studenti_id = ?', (studente_id,))
        studente = cur.fetchone()
        return studente

    @staticmethod
    #funzione che chiede all'utente di inserire un id, e controlla che l'id sia valido (non vuoto e numerico)
    def insert_id(prompt="Inserisci id: "): 
        valore = input(prompt).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)

    #cancello un studente
    @staticmethod
    def delete_student(conn):
        try:
            studente_id = StudenteServizio.insert_id("Inserisci l'id del studente da cancellare: ")

            cur = conn.cursor()
            cur.execute('DELETE FROM studenti WHERE studenti_id = ?', (studente_id,))
            conn.commit()
            if cur.rowcount == 0:
                raise ValueError("Nessun studente trovato con l'id indicato")
            return "Studente cancellato con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione del studente"