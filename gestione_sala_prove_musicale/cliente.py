class Cliente:
    def __init__(self, nome_gruppo, nome_referente, num_cell, email):
        self.nome_gruppo = nome_gruppo
        self.nome_referente = nome_referente
        self.num_cell = num_cell
        self.email = email

    def get_cliente(self):
        return self.nome_gruppo, self.nome_referente, self.num_cell, self.email