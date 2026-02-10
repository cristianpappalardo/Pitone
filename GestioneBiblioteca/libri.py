import json

def create_file(libri_dict):
    with open("libri.json", "w") as f:
        json.dump(libri_dict, f, indent=4)


def leggi_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File inesistente, ne verrà creato uno nuovo.")
        return {}


def nuovo_libro():
    libri_dict = leggi_file("libri.json")
    id = len(libri_dict)

    while True:
        scelta = input("Vuoi inserire un nuovo libro? S/N: ")

        if scelta.upper() == "N":
            print("Arrivederci")
            break

        elif scelta.upper() == "S":
            nome_libro = input("Inserisci il nome del libro: ")
            autore = input("Inserisci il nome dell'autore: ")
            copie_disponibili = input("Quante copie sono attualmente disponibili?: ")

            if nome_libro in libri_dict and autore in libri_dict: 
                print("Questo libro esiste già") 
                break

            
            libri_dict[nome_libro] = {
                "codice ISBN": id,
                "autore": autore,
                "copie disponibili" : copie_disponibili
            }

            id += 1
            create_file(libri_dict)
            
            print("Nuovo libro aggiunto")
            
        else:
            print("Scelta non valida, riprova")
    
    return libri_dict


def modifica_copie(libri_dict, nome_libro, autore, nuove_copie):
    if nome_libro in libri_dict and libri_dict[nome_libro]["autore"] == autore:
        libri_dict[nome_libro]["copie disponibili"] = nuove_copie
        create_file(libri_dict)
        print(f"Aggiornate le copie disponibili per '{nome_libro}' a {nuove_copie}.")
    else:
        print("Libro non trovato nel sistema.")