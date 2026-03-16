class AssegnazionePosto:
    def __init__(self, assegnazione_id, dipendente_id, posto_id):
        self.assegnazione_id = assegnazione_id  # None finché il database non genera l'id
        self.dipendente_id = dipendente_id      # Riferimento al dipendente (chiave esterna)
        self.posto_id = posto_id                # Riferimento al posto auto (chiave esterna)