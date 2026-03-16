class PostoAuto:
    def __init__(self, posto_id, assegnazione):
        self.posto_id = posto_id        # None finché il database non assegna l'id automaticamente
        self.assegnazione = assegnazione  # Stringa: 'disponibile' oppure 'assegnato'