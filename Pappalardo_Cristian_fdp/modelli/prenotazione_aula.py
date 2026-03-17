class PrenotazioneAula:
    def __init__(self, prenotazione_id, studente_id, aula_id):
        self.prenotazione_id = prenotazione_id  # None finché il database non genera l'id
        self.studente_id = studente_id # Riferimento allo studente (chiave esterna)
        self.aula_id = aula_id # Riferimento all'aula studio (chiave esterna)