import json

def leggi_saldo(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File inesistente, ne verrà creato uno nuovo.")
        return {}

def aggiungi_denaro():
    while True:
        try:
            denaro = round(float(input("Inserisci la quantità di denaro che vuoi aggiungere in cassa: ")), 2)
            print("Hai aggiunto €" +denaro+ "in cassa")
            if prezzo < 0:
                print("Il prezzo non può essere negativo.")
                continue
        except ValueError:
            print("Il valore inserito non è un numero, perfavore inserisci un numero valido.")
            
    with open("cassa.json", "w") as f:
        json.dump(denaro, f, indent=4)
        

    