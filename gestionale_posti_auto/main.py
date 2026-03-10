import sqlite3
from servizio.dipendente_servizio import DipendenteServizio
from servizio.posto_auto_servizio import PostoAutoServizio
from servizio.assegnazione_posto_servizio import AssegnazionePostoServizio


def mostra_menu():
    print("\n" + "=" * 50)
    print("    GESTIONALE PARCHEGGIO AZIENDALE - MENU PRINCIPALE")
    print("=" * 50)
    print("\n--- GESTIONE DIPENDENTI ---")
    print("1. Registra nuovo dipendente")
    print("2. Visualizza dipendenti")
    print("3. Aggiorna dipendente")
    print("\n--- GESTIONE POSTI AUTO ---")
    print("4. Registra nuova posto auto")
    print("5. Visualizza posti auto")
    print("6. Aggiorna posto auto")
    print("\n--- ASSEGNAZIONE POSTI ---")
    print("7. Assegna nuovo posto auto a un dipendente")
    print("8. Visualizza posti assegnati")
    print("9. Cancella assegnazione posto")
    print("\n--- ALTRO ---")
    print("0. Esci dal programma")
    print("=" * 50)


def main():
    mostra_menu()
    conn = sqlite3.connect('parcheggio.sqlite')
    while True:
        mostra_menu()
        try:
            case = int(input("Inserire un numero: "))
        except ValueError:
            print("Inserire un numero valido")
            continue
        match case:
            case 1:
                DipendenteServizio.aggiungi_dipendente(conn)
            case 2:
                DipendenteServizio.visualizza_dipendenti(conn)
            case 3:
                DipendenteServizio.cancella_dipendente(conn)
            case 4:
                PostoAutoServizio.aggiungi_posto_auto(conn)
            case 5:
                PostoAutoServizio.visualizza_posto_auto(conn)
            case 6:
                PostoAutoServizio.cancella_posto_auto(conn)
            case 7:
                AssegnazionePostoServizio.aggiungi_assegnazione(conn)
            case 8:
                AssegnazionePostoServizio.visualizza_prenotazioni(conn)
            case 9:
                AssegnazionePostoServizio.cancella_prenotazione(conn)
            case 0:
                print("Uscita in corso...")
                conn.close()
                break
            case _:
                print("Scelta non valida.")

        input("\nPremere INVIO per continuare...")
    
    

if __name__ == "__main__":
    main()