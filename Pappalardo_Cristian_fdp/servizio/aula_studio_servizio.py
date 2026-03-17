import sqlite3
from modelli import AulaStudio

class AulaStudioServizio:
    #aggiungo un nuovo aula_studio al database
    @staticmethod
    def add_room(conn):
        try:
            aula_studio = AulaStudioServizio.save_room()
            cur = conn.cursor()
            cur.execute('''INSERT INTO aule_studio (nome_aula, posti_disponibili) VALUES (?, ?)''', 
                        (aula_studio.nome_aula ,aula_studio.posti_disponibili,))
            conn.commit()
            return "Nuovo aula studio aggiunto con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.IntegrityError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante l'aggiunta del aula studio"

    #istanzio un nuovo aula_studio 
    @staticmethod
    def save_room():
        nome_aula = input("Inserisci il nome dell'aula: ").strip().lower()
        posti_disponibili_raw = input("inserisci il numero di posti disponibili: ").strip()
        if not posti_disponibili_raw:
            raise ValueError("Il campo posti disponibili non può essere vuoto")
        if not posti_disponibili_raw.isdigit():
            raise ValueError("I posti devono essere numerici")
        posti_disponibili = int(posti_disponibili_raw)
        if posti_disponibili > 30:
            raise ValueError("Il numero di posti disponibili non può essere maggiore di 30")
        aula_studio = AulaStudio(None, nome_aula, posti_disponibili)
        return aula_studio
    
    #visualizzo le aule studio presenti nel database
    @staticmethod
    def get_all_rooms(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM aule_studio')
        aula_studio = cur.fetchall()
        return aula_studio

    #visualizzo una aula studio in base all'id inserito dall'utente
    @staticmethod
    def get_room_by_id(conn):
        try:
            aula_id = AulaStudioServizio.insert_id("Inserisci l'id del aula studio: ")
        except ValueError:
            return None

        cur = conn.cursor()
        cur.execute('SELECT * FROM aule_studio WHERE aula_id = ?', (aula_id,))
        aula_studio = cur.fetchone()
        return aula_studio

    #inserisco l'id del aula studio
    @staticmethod
    def insert_id(prompt="inserisci id: "):
        valore = input(prompt).strip()
        if not valore:
            raise ValueError("Il campo id non puo essere vuoto")
        if not valore.isdigit():
            raise ValueError("L'id deve essere numerico")
        return int(valore)

    #cancello una aula studio
    @staticmethod
    def delete_room(conn):
        try:
            aula_id = AulaStudioServizio.insert_id("Inserisci l'id del aula studio da cancellare: ")

            cur = conn.cursor()
            cur.execute('DELETE FROM aule_studio WHERE aula_id = ?', (aula_id,))
            conn.commit()
            if cur.rowcount == 0:
                raise ValueError("Nessun aula studio trovato con l'id indicato")
            return "Aula studio cancellata con successo"
        except ValueError as e:
            conn.rollback()
            return str(e)
        except sqlite3.Error:
            conn.rollback()
            return "Errore database durante la cancellazione del aula studio"