from forma import Forma

class Triangolo(Forma):
    
    def area(self):
        print("area:", self.base * self.altezza / 2)	


base = int(input("base: "))
altezza = int(input("altezza: "))

forma = Triangolo(base, altezza)

forma.area()