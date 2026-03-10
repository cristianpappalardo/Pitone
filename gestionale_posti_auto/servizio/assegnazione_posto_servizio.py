import sqlite3
from modelli.assegnazione_posto import AssegnazionePosto 
from servizio.dipendente_servizio import Dipendente
from servizio.posto_auto_servizio import PostoAuto


class AssegnazionePostoServizio:
    #creo la connessione al database    
    conn = sqlite3.connect("parcheggio.sqlite")

    #aggiungo una nuova assegnazione posto al database
    def aggiungi_assegnazione(self, conn):
        assegnazione = self.salva_assegnazione()
        cur = conn.cursor()
        cur.execute('''INSERT INTO assegnazione_posti (dipendente_id, posto_id) VALUES (?, ?)''', 
                    (assegnazione.id_tuple[0], assegnazione.id_tuple[1]))
        return "Nuovo posto auto aggiunto con successo"

    #istanzio un nuovo oggetto assegnazione posto 
    def salva_assegnazione(self):
        id_tuple = self.get_dipendente_id_and_posto_id()
        assegnazione_posto = AssegnazionePosto(None, id_tuple[0], id_tuple[1])
        return assegnazione_posto
    
    #visualizzo i posti auto presenti nel database
    def visualizza_assegnazione(self, conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM assegnazione_posti')
        assegnazione_posto = cur.fetchall()
        return assegnazione_posto
    
    #restituisce uan tupla con l'id del dipendente e del posto auto
    def get_dipendente_id_and_posto_id(self):
        dipendente_id = Dipendente.inserisci_id()
        posto_id = PostoAuto.inserisci_id()
        return (dipendente_id, posto_id)

    #cancello un assegnazione posto
    def cancella_assegnazione(self, conn):
        assegnazione_id = self.inserisci_id()
        cur = conn.cursor()
        cur.execute('DELETE FROM assegnazione_posti WHERE assegnazione_id = ?', (assegnazione_id,))
        return "Assegnazione posto auto cancellata con successo"

    #chiudo la connessione
    conn.commit()
    conn.close()