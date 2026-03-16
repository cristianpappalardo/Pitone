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
    print("3. Cancella dipendente")
    print("\n--- GESTIONE POSTI AUTO ---")
    print("4. Registra nuova posto auto")
    print("5. Visualizza posti auto")
    print("6. Cancella posto auto")
    print("\n--- ASSEGNAZIONE POSTI ---")
    print("7. Assegna nuovo posto auto a un dipendente")
    print("8. Visualizza posti assegnati")
    print("9. Cancella assegnazione posto")
    print("\n--- ALTRO ---")
    print("0. Esci dal programma")
    print("=" * 50)


def main():
    conn = None
    try:
        conn = sqlite3.connect('parcheggio.sqlite')
        while True:
            mostra_menu()
            try:
                case = int(input("Inserire un numero: "))
            except ValueError:
                print("Inserire un numero valido")
                continue

            try:
                match case:
                    case 1:
                        print(DipendenteServizio.aggiungi_dipendente(conn))
                    case 2:
                        dipendenti = DipendenteServizio.visualizza_dipendenti(conn)
                        if not dipendenti:
                            print("Nessun dipendente presente")
                        else:
                            for dipendente in dipendenti:
                                print(dipendente)
                    case 3:
                        print(DipendenteServizio.cancella_dipendente(conn))
                    case 4:
                        print(PostoAutoServizio.aggiungi_posto_auto(conn))
                    case 5:
                        posti_auto = PostoAutoServizio.visualizza_posto_auto(conn)
                        if not posti_auto:
                            print("Nessun posto auto presente")
                        else:
                            for posto in posti_auto:
                                print(posto)
                    case 6:
                        print(PostoAutoServizio.cancella_posto_auto(conn))
                    case 7:
                        print(AssegnazionePostoServizio.aggiungi_assegnazione(conn))
                    case 8:
                        assegnazioni = AssegnazionePostoServizio.visualizza_assegnazione(conn)
                        if not assegnazioni:
                            print("Nessuna assegnazione presente")
                        else:
                            for assegnazione in assegnazioni:
                                print(assegnazione)
                    case 9:
                        print(AssegnazionePostoServizio.cancella_assegnazione(conn))
                    case 0:
                        print("Uscita in corso...")
                        break
                    #funziona come default, se l'utente inserisce un numero non presente nel menu, viene stampato un messaggio di errore
                    case _:
                        print("Scelta non valida.")
            except sqlite3.Error:
                print("Errore database durante l'operazione selezionata")
            #alla fine di ogni operazione, viene chiesto all'utente di premere INVIO per continuare, in modo da poter visualizzare i risultati prima di mostrare nuovamente il menu
            input("\nPremere INVIO per continuare...")
    except sqlite3.Error:
        print("Errore durante l'apertura del database")
    finally:
        if conn is not None:
            conn.close()
    
    
if __name__ == "__main__":
    main()