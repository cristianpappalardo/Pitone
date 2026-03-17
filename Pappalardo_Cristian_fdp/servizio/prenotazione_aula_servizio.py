import sqlite3
from modelli import PrenotazioneAula
from servizio.studente_servizio import StudenteServizio
from servizio.aula_studio_servizio import AulaStudioServizio


class PrenotazioneAulaServizio:
    #aggiungo una nuova prenotazione aula al database
    @staticmethod
    def add_booking(conn):
        try:
            prenotazione = PrenotazioneAulaServizio.save_booking(conn)

            cur = conn.cursor()
            cur.execute('''INSERT INTO prenotazioni (studenti_id, aula_id) VALUES (?, ?)''', 
                        (prenotazione.studente_id, prenotazione.aula_id))
            cur.execute('UPDATE aule_studio SET posti_disponibili = posti_disponibili - 1 WHERE aula_id = ?', (prenotazione.aula_id,))
            conn.commit()
            return "Prenotazione aula creata con successo"
        except (ValueError, sqlite3.IntegrityError) as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la creazione della prenotazione"

    #istanzio un nuovo oggetto prenotazione aula 
    @staticmethod
    def save_booking(conn):
        id_tuple = PrenotazioneAulaServizio.get_students_id_and_room_id()

        studente_id, aula_id = id_tuple
        cur = conn.cursor()

        cur.execute('SELECT 1 FROM studenti WHERE studenti_id = ?', (studente_id,))
        if cur.fetchone() is None:
            raise ValueError("Studente non trovato")

        cur.execute('SELECT posti_disponibili FROM aule_studio WHERE aula_id = ?', (aula_id,))
        aula = cur.fetchone()
        if aula is None:
            raise ValueError("Posto non trovato")
        if aula[0] < 1:
            raise ValueError("L'aula studio non ha posti disponibili")

        cur.execute('SELECT 1 FROM prenotazioni WHERE studenti_id = ?', (studente_id,))
        if cur.fetchone() is not None:
            raise ValueError("Lo studente ha gia un aula assegnata")

        prenotazione = PrenotazioneAula(None, id_tuple[0], id_tuple[1])
        return prenotazione
    
    #visualizzo i posti  presenti nel database
    @staticmethod
    def get_all_bookings(conn):
        cur = conn.cursor()
        #eseguo una query che restituisce l'id dell'prenotazione, il nome e cognome del studente e l'id del aula  assegnato
        #uso join per unire le tabelle prenotazioni, studenti e aula_studio, in modo da poter visualizzare tutte le informazioni necessarie in un'unica query
        cur.execute('''SELECT prenotazioni.prenotazioni_id, studenti.nome, studenti.cognome, prenotazioni.aula_id
                    FROM prenotazioni
                    JOIN studenti ON prenotazioni.studenti_id = studenti.studenti_id
                    JOIN aule_studio ON prenotazioni.aula_id = aule_studio.aula_id''')
        
        prenotazione = cur.fetchall()
        if not prenotazione:
            return []
        return [
            f"Prenotazione {prenotazione_id}: studente {nome} {cognome} -> aula_id {aula_id}"
            for prenotazione_id, nome, cognome, aula_id in prenotazione
        ]
    
    #restituisce uan tupla con l'id del studente e del aula 
    @staticmethod
    def get_students_id_and_room_id():
        studente_id = StudenteServizio.insert_id("Inserisci l'id del studente: ")
        aula_id = AulaStudioServizio.insert_id("Inserisci l'id del aula : ")

        return (studente_id, aula_id)

    #cancello un prenotazione aula
    @staticmethod
    def delete_booking(conn):
        try:
            prenotazione_id = PrenotazioneAulaServizio.insert_id("Inserisci l'id della prenotazione da cancellare: ")

            cur = conn.cursor()
            cur.execute('SELECT aula_id FROM prenotazioni WHERE prenotazioni_id = ?', (prenotazione_id,))
            record = cur.fetchone()
            if record is None:
                raise ValueError("Prenotazione non trovata")

            cur.execute('DELETE FROM prenotazioni WHERE prenotazioni_id = ?', (prenotazione_id,))
            cur.execute('UPDATE aule_studio SET posti_disponibili = posti_disponibili + 1 WHERE aula_id = ?', (record[0],))
            conn.commit()
            return "Prenotazione aula  cancellata con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione dell'prenotazione"

    @staticmethod
    def insert_id(prompt="Inserisci l'id: "):
        valore = input(prompt).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)