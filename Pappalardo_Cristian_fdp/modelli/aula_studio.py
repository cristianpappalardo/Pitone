class AulaStudio:
    def __init__(self, aula_id, nome_aula, posti_disponibili):
        self.aula_id = aula_id # None finché il database non assegna l'id automaticamente
        self.nome_aula = nome_aula 
        self.posti_disponibili = posti_disponibili  