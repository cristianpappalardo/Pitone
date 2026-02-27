import sqlite3
import service


def mostra_menu():
    print("\n" + "=" * 50)
    print("    GESTIONALE SALA PROVE MUSICALI - MENU PRINCIPALE")
    print("=" * 50)
    print("\n--- GESTIONE UTENTI---")
    print("1. Aggiungi nuovo utente")
    print("2. Visualizza tutti gli utenti")
    print("\n--- GESTIONE SALE ---")
    print("3. Registra una nuova sala")
    print("4. Visualizza tutte le sale")
    print("\n--- GESTIONE PRENOTAZIONI ---")
    print("5. Registra una nuova prenotazione")
    print("6. Visualizza le prenotazioni")
    print("\n--- ALTRO ---")
    print("0. Esci dal programma")
    print("=" * 50)


def main():
    mostra_menu()
    conn = sqlite3.connect('musicale.sqlite')
    while True:
        try:
            case = int(input("Inserire un numero: "))
        except ValueError:
            print("Inserire un numero valido")
            continue
        match case:
            case 1:
                service.registrazione_cliente(conn)
            case 2:
                service.visualizza_clienti(conn)
            case 3:
                service.creazione_sala(conn)
            case 4:
                service.visualizza_sale(conn)
            case 5:
                service.nuova_prenotazione(conn)
            case 6:
                service.visualizza_prenotazioni(conn)
            case 0:
                print("Uscita in corso...")
                conn.close()
                break

        # Pausa prima di mostrare di nuovo il menu
        input("\nPremere INVIO per continuare...")
    
    

if __name__ == "__main__":
    main()