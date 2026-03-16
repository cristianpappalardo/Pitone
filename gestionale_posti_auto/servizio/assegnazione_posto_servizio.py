import sqlite3
from modelli.assegnazione_posto import AssegnazionePosto 
from servizio.dipendente_servizio import DipendenteServizio
from servizio.posto_auto_servizio import PostoAutoServizio


class AssegnazionePostoServizio:
    #aggiungo una nuova assegnazione posto al database
    @staticmethod
    def aggiungi_assegnazione(conn):
        try:
            assegnazione = AssegnazionePostoServizio.salva_assegnazione(conn)

            cur = conn.cursor()
            cur.execute('''INSERT INTO assegnazione_posti (dipendente_id, posto_id) VALUES (?, ?)''', 
                        (assegnazione.dipendente_id, assegnazione.posto_id))
            cur.execute('UPDATE posti_auto SET assegnazione = ? WHERE posto_id = ?', ('assegnato', assegnazione.posto_id))
            conn.commit()
            return "Assegnazione posto auto creata con successo"
        except (ValueError, sqlite3.IntegrityError) as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la creazione dell'assegnazione"

    #istanzio un nuovo oggetto assegnazione posto 
    @staticmethod
    def salva_assegnazione(conn):
        id_tuple = AssegnazionePostoServizio.get_dipendente_id_and_posto_id()

        dipendente_id, posto_id = id_tuple
        cur = conn.cursor()

        cur.execute('SELECT 1 FROM dipendenti WHERE dipendente_id = ?', (dipendente_id,))
        if cur.fetchone() is None:
            raise ValueError("Dipendente non trovato")

        cur.execute('SELECT assegnazione FROM posti_auto WHERE posto_id = ?', (posto_id,))
        posto = cur.fetchone()
        if posto is None:
            raise ValueError("Posto auto non trovato")
        if posto[0] != 'disponibile':
            raise ValueError("Il posto auto indicato non e disponibile")

        cur.execute('SELECT 1 FROM assegnazione_posti WHERE dipendente_id = ?', (dipendente_id,))
        if cur.fetchone() is not None:
            raise ValueError("Il dipendente ha gia un posto assegnato")

        assegnazione_posto = AssegnazionePosto(None, id_tuple[0], id_tuple[1])
        return assegnazione_posto
    
    #visualizzo i posti auto presenti nel database
    @staticmethod
    def visualizza_assegnazione(conn):
        cur = conn.cursor()
        #eseguo una query che restituisce l'id dell'assegnazione, il nome e cognome del dipendente e l'id del posto auto assegnato
        #uso join per unire le tabelle assegnazione_posti, dipendenti e posti_auto, in modo da poter visualizzare tutte le informazioni necessarie in un'unica query
        cur.execute('''
            SELECT ap.assegnazione_id, d.nome, d.cognome, p.posto_id
            FROM assegnazione_posti ap
            JOIN dipendenti d ON d.dipendente_id = ap.dipendente_id 
            JOIN posti_auto p ON p.posto_id = ap.posto_id

        ''')
        assegnazione_posto = cur.fetchall()
        if not assegnazione_posto:
            return []
        return [
            f"Assegnazione {assegnazione_id}: dipendente {nome} {cognome} -> posto_id {posto_id}"
            for assegnazione_id, nome, cognome, posto_id in assegnazione_posto
        ]
    
    #restituisce uan tupla con l'id del dipendente e del posto auto
    @staticmethod
    def get_dipendente_id_and_posto_id():
        dipendente_id = DipendenteServizio.inserisci_id("Inserisci l'id del dipendente: ")
        posto_id = PostoAutoServizio.inserisci_id("Inserisci l'id del posto auto: ")

        return (dipendente_id, posto_id)

    #cancello un assegnazione posto
    @staticmethod
    def cancella_assegnazione(conn):
        try:
            assegnazione_id = AssegnazionePostoServizio.inserisci_id("Inserisci l'id dell'assegnazione da cancellare: ")

            cur = conn.cursor()
            cur.execute('SELECT posto_id FROM assegnazione_posti WHERE assegnazione_id = ?', (assegnazione_id,))
            record = cur.fetchone()
            if record is None:
                raise ValueError("Assegnazione non trovata")

            cur.execute('DELETE FROM assegnazione_posti WHERE assegnazione_id = ?', (assegnazione_id,))
            cur.execute('UPDATE posti_auto SET assegnazione = ? WHERE posto_id = ?', ('disponibile', record[0]))
            conn.commit()
            return "Assegnazione posto auto cancellata con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione dell'assegnazione"

    @staticmethod
    def inserisci_id(messaggio="Inserisci l'id: "):
        valore = input(messaggio).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)