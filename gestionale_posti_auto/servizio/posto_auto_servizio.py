import sqlite3
from modelli.posto_auto import PostoAuto

class PostoAutoServizio:
    #creo la connessione al database    
    conn = sqlite3.connect("parcheggio.sqlite")

    #aggiungo un nuovo posto_auto al database
    def aggiungi_posto_auto(self, conn):
        posto_auto = self.salva_posto_auto()
        cur = conn.cursor()
        cur.execute('''INSERT INTO posti_auto (assegnazione) VALUES (?)''', 
                    (posto_auto.assegnazione))
        return "Nuovo posto auto aggiunto con successo"

    #istanzio un nuovo posto_auto 
    def salva_posto_auto(self):
        assegnazione = "disponibile"
        posto_auto = PostoAuto(None, assegnazione)
        return posto_auto
    
    #visualizzo i posti auto presenti nel database
    def visualizza_posto_auto(self, conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM posto_auto')
        posto_auto = cur.fetchall()
        return posto_auto

    #visualizzo un posto auto in base all'id inserito dall'utente
    def get_posto_auto_by_id(self, conn):
        posto_id = self.inserisci_id()
        cur = conn.cursor()
        cur.execute('SELECT * FROM posti_auto WHERE posto_id = ?', (posto_id,))
        posto_auto = cur.fetchone()
        return posto_auto

    #inserisco l'id del posto auto
    def inserisci_id(self):
        posto_id = input("Inserisci l'id del posto auto").strip().lower()
        if not posto_id : return "Il campo id non puo essere vuoto"
        return posto_id

    #cancello un posto auto
    def cancella_posto_auto(self, conn):
        posto_id = self.inserisci_id()
        cur = conn.cursor()
        cur.execute('DELETE FROM posti_auto WHERE posto_id = ?', (posto_id,))
        return "Posto auto cancellato con successo"

    #chiudo la connessione
    conn.commit()
    conn.close()