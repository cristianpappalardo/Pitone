import json

def check_prezzo():
    while True:
        try:
            prezzo = round(float(input("Inserisci il prezzo unitario per questo pane: ")), 2)
            if prezzo < 0:
                print("Il prezzo non può essere negativo.")
                continue
            return prezzo
        except ValueError:
            print("Il valore inserito non è un numero, perfavore inserisci un numero valido.")


def create_file_pane(pane_dict):
    with open("pane.json", "w") as f:
        json.dump(pane_dict, f, indent=4)


def leggi_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File inesistente, ne verrà creato uno nuovo.")
        return {}


def nuovo_pane():
    pane_dict = leggi_file("pane.json")
    ID = len(pane_dict)

    while True:
        scelta = input("Vuoi inserire un nuovo tipo di pane? S/N: ")

        if scelta.upper() == "N":
            print("Arrivederci")
            break

        elif scelta.upper() == "S":
            nome_pane = input("Inserisci il nome del pane: ")

            if nome_pane in pane_dict: 
                print("Questo pane esiste già, scegli un altro nome.") 
                continue

            prezzo = check_prezzo()

            pane_dict[nome_pane] = {
                "codice univoco": ID,
                "descrizione": input("Inserisci una descrizione per questo pane: "),
                "prezzo unitario": prezzo
            }

            ID += 1
            create_file_pane(pane_dict)
            
            print("Nuovo tipo di pane aggiunto")
            
        else:
            print("Scelta non valida, riprova")
    
    return pane_dict


def cerca_pane(nome_pane):
    dati = leggi_file("pane.json")
    return dati.get(nome_pane, None)


def modifica_pane():
    dati = leggi_file("pane.json")

    while True:
        scelta = input("Vuoi modificare il prezzo di un tipo di pane? S/N: ")

        if scelta.upper() == "N":
            break

        elif scelta.upper() == "S":
            nome_pane = input("Quale tipo di pane vuoi modificare? Inserisci il nome: ")

            if nome_pane not in dati:
                print("Errore, questo tipo di pane non esiste")
                continue

            nuovo_prezzo = check_prezzo()
            dati[nome_pane]["prezzo unitario"] = nuovo_prezzo

            create_file_pane(dati)
            print("Prezzo aggiornato.")

        else:
            print("Errore, inserisci S oppure N")
