import sqlite3
from servizio import StudenteServizio
from servizio import AulaStudioServizio
from servizio import PrenotazioneAulaServizio


def mostra_menu():
    print("\n" + "=" * 50)
    print("    GESTIONALE AULE STUDIO ITS - MENU PRINCIPALE")
    print("=" * 50)
    print("\n--- GESTIONE STUDENTI ---")
    print("1. Registra nuovo studente")
    print("2. Visualizza studenti")
    print("3. Cancella studente")
    print("\n--- GESTIONE AULE STUDIO ---")
    print("4. Registra nuova aula studio")
    print("5. Visualizza posti disponibili")
    print("6. Cancella aula studio")
    print("\n--- PRENOTAZIONE AULE ---")
    print("7. Assegna nuovo aula studio a un studente")
    print("8. Visualizza prenotazioni attive")
    print("9. Cancella prenotazione")
    print("\n--- ALTRO ---")
    print("0. Esci dal programma")
    print("=" * 50)


def main():
    conn = None
    try:
        conn = sqlite3.connect('aule_studio_ITS.sqlite')
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
                        print(StudenteServizio.add_student(conn))
                    case 2:
                        studenti = StudenteServizio.get_all_students(conn)
                        if not studenti:
                            print("Nessun studente presente")
                        else:
                            for studente in studenti:
                                print(studente)
                    case 3:
                        print(StudenteServizio.delete_student(conn))
                    case 4:
                        print(AulaStudioServizio.add_room(conn))
                    case 5:
                        aule = AulaStudioServizio.get_all_rooms(conn)
                        if not aule:
                            print("Nessun aula studio presente")
                        else:
                            for aula in aule:
                                print(aula)
                    case 6:
                        print(AulaStudioServizio.delete_room(conn))
                    case 7:
                        print(PrenotazioneAulaServizio.add_booking(conn))
                    case 8:
                        prenotazioni = PrenotazioneAulaServizio.get_all_bookings(conn)
                        if not prenotazioni:
                            print("Nessuna prenotazione presente")
                        else:
                            for prenotazione in prenotazioni:
                                print(prenotazione)
                    case 9:
                        print(PrenotazioneAulaServizio.delete_booking(conn))
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