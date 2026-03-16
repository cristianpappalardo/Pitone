import sqlite3
from modelli.posto_auto import PostoAuto

class PostoAutoServizio:
    #aggiungo un nuovo posto_auto al database
    @staticmethod
    def aggiungi_posto_auto(conn):
        try:
            posto_auto = PostoAutoServizio.salva_posto_auto()
            cur = conn.cursor()
            cur.execute('''INSERT INTO posti_auto (assegnazione) VALUES (?)''', 
                        (posto_auto.assegnazione,))
            conn.commit()
            return "Nuovo posto auto aggiunto con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.IntegrityError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante l'aggiunta del posto auto"

    #istanzio un nuovo posto_auto 
    @staticmethod
    def salva_posto_auto():
        assegnazione = "disponibile"
        posto_auto = PostoAuto(None, assegnazione)
        return posto_auto
    
    #visualizzo i posti auto presenti nel database
    @staticmethod
    def visualizza_posto_auto(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM posti_auto')
        posto_auto = cur.fetchall()
        return posto_auto

    #visualizzo un posto auto in base all'id inserito dall'utente
    @staticmethod
    def get_posto_auto_by_id(conn):
        try:
            posto_id = PostoAutoServizio.inserisci_id("Inserisci l'id del posto auto: ")
        except ValueError:
            return None

        cur = conn.cursor()
        cur.execute('SELECT * FROM posti_auto WHERE posto_id = ?', (posto_id,))
        posto_auto = cur.fetchone()
        return posto_auto

    #inserisco l'id del posto auto
    @staticmethod
    def inserisci_id(messaggio="Inserisci l'id: "):
        valore = input(messaggio).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)

    #cancello un posto auto
    @staticmethod
    def cancella_posto_auto(conn):
        try:
            posto_id = PostoAutoServizio.inserisci_id("Inserisci l'id del posto auto da cancellare: ")

            cur = conn.cursor()
            cur.execute('DELETE FROM posti_auto WHERE posto_id = ?', (posto_id,))
            conn.commit()
            if cur.rowcount == 0:
                raise ValueError("Nessun posto auto trovato con l'id indicato")
            return "Posto auto cancellato con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione del posto auto"