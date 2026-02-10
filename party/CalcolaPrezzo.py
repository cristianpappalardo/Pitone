class CalcolaPrezzo:

    def __init__(self):
        self.prezzo_unitario = 0.0
        self.unita = 0

    def incremento_unita(self, step_incremento):
        self.unita = self.unita + step_incremento

    def set_prezzo(self, prezzo_in_euro):
        self.prezzo_unitario = float(prezzo_in_euro)

    def calcolo_prezzo_totale(self):
        prezzo_totale = self.unita * self.prezzo_unitario
        return prezzo_totale

    def print_prezzo(self):
        print("Il prezzo totale è:", self.calcolo_prezzo_totale())
