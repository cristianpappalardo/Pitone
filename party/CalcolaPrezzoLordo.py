from CalcolaPrezzo import CalcolaPrezzo

class CalcolaPrezzoLordo(CalcolaPrezzo):
    
    def __init__(self):
        super().__init__()
        self.iva = 0

    def set_iva(self, iva_in_percentuale):
        self.iva = iva_in_percentuale

    def calcolo_prezzo_lordo(self):
        prezzo_lordo = self.calcolo_prezzo_totale() * (1 + self.iva / 100)
        return prezzo_lordo

    def print_prezzo_lordo(self):
        print("Il prezzo lordo è:", self.calcolo_prezzo_lordo())