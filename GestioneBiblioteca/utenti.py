import json

def create_file(utenti):
    with open("utenti.json", "w") as f:
        json.dump(utenti, f, indent=4)


def leggi_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File inesistente, ne verrà creato uno nuovo.")
        return {}
        
        
def nuovo_utente():
    utenti = leggi_file("utenti.json")
    ID = len(utenti)

    while True:
        scelta = input("Vuoi inserire un nuovo utente? S/N: ")

        if scelta.upper() == "N":
            print("Arrivederci")
            break

        elif scelta.upper() == "S":
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")

            
            utenti[ID] = {
                "codice univoco": ID,
                "nome": nome,
                "cognome" : cognome
            }

            ID += 1
            create_file(utenti)
            
            print("Nuovo utente aggiunto")
            
        else:
            print("Scelta non valida, riprova")
    
    return utenti