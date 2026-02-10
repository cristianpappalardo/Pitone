"""
GESTIONALE BIBLIOTECA - Programma Principale (main)

Questo è il file principale del programma che gestisce una piccola biblioteca.
Il programma permette di:
- Gestire i libri (aggiungere, visualizzare)
- Gestire gli utenti (registrare, visualizzare)
- Gestire i prestiti e le restituzioni
- Visualizzare statistiche e report

Il programma è strutturato in moduli separati:
- libri.py: gestione dei libri
- utenti.py: gestione degli utenti
- prestiti.py: gestione dei prestiti e delle restituzioni

Ogni modulo ha le proprie funzioni e il proprio file di salvataggio dati.
"""

# Importiamo tutte le funzioni necessarie dai vari moduli
from book import Book
from user import User
from loans import Loan

def mostra_menu():
    """
    Mostra il menu principale con tutte le opzioni disponibili.
    """
    print("\n" + "=" * 50)
    print("    GESTIONALE BIBLIOTECA - MENU PRINCIPALE")
    print("=" * 50)
    print("\n--- GESTIONE LIBRI ---")
    print("1. Aggiungi nuovo libro")
    print("2. Visualizza tutti i libri")
    print("3. Cerca libro per ISBN")
    print("\n--- GESTIONE UTENTI ---")
    print("4. Registra nuovo utente")
    print("5. Visualizza tutti gli utenti")
    print("\n--- PRESTITI E RESTITUZIONI ---")
    print("6. Registra prestito/i")
    print("7. Registra restituzione/i")
    print("\n--- REPORT E STATISTICHE ---")
    print("8. Report libri più prestati")
    print("9. Report utenti più attivi")
    print("\n--- ALTRO ---")
    print("0. Esci dal programma")
    print("=" * 50)


def main():
    """
    Funzione principale del programma.
    Gestisce il menu e l'esecuzione delle varie funzionalità.
    """
    # Mostriamo un messaggio di benvenuto
    print("=" * 50)
    print("    BENVENUTO NEL GESTIONALE BIBLIOTECA")
    print("=" * 50)

    # Carichiamo i dati esistenti da file o database

    # Ciclo principale del programma
    while True:
        # Mostriamo il menu
        mostra_menu()

        # Chiediamo all'utente di scegliere un'opzione
        scelta = input("\nInserisci la tua scelta: ").strip()

        # Gestiamo le varie scelte con if-elif-else

        if scelta == '1':
            # Opzione 1: Aggiungi nuovo libro
           libro = Book(isbn=input("Inserisci il codice ISBN: ").strip(),
                        title=input("Inserisci il titolo: ").strip(),
                        author=input("Inserisci l'autore: ").strip(),
                        copies=int(input("Inserisci il numero di copie: ").strip()))
           libro.add_book()

        elif scelta == '2':
            # Opzione 2: Visualizza tutti i libri
            libro = Book(isbn='', title='', author='', copies=0)  # Creiamo un'istanza temporanea per accedere ai metodi statici
            print("\n=== ELENCO DEI LIBRI ===")
            libri = libro.get_all_books()
            print(f"{'ISBN':<15} {'Titolo':<30} {'Autore':<20} {'Copie':<10}")
            print("-" * 80)
            for l in libri:
                print(f"{l[0]:<15} {l[1]:<30} {l[2]:<20} {l[3]:<10}")
            
        elif scelta == '3':
            # Opzione 3 : Cerca libro per ISBN
            libro = Book(isbn='', title='', author='', copies=0)  # Creiamo un'istanza temporanea per accedere ai metodi statici
            isbn = input("Inserisci il codice ISBN da cercare: ").strip()
            libro_trovato = libro.get_book_from_isbn(isbn)
            print("\n=== RISULTATO RICERCA ===")
            if libro_trovato:
                print(f"ISBN: {libro_trovato[0]}")
                print(f"Titolo: {libro_trovato[1]}")
                print(f"Autore: {libro_trovato[2]}")
                print(f"Copie disponibili: {libro_trovato[3]}")

        elif scelta == '4':
            # Opzione 4: Registra nuovo utente
            user = User(user_id=0, name=input("Inserisci il nome: ").strip(),
                        surname=input("Inserisci il cognome: ").strip(),
                        email=input("Inserisci l'email: ").strip())
            user.add_user()
            print("\nUtente registrato con successo!")

        elif scelta == '5':
            # Opzione 5: Visualizza tutti gli utenti
            user = User(user_id=0, name='', surname='', email='')  # Creiamo un'istanza temporanea per accedere ai metodi statici
            print("\n=== ELENCO DEGLI UTENTI ===")
            utenti = user.get_all_users()
            print(f"{'ID':<5} {'Nome':<20} {'Cognome':<20} {'Email':<30}")
            print("-" * 75)
            for u in utenti:
                print(f"{u[0]:<5} {u[1]:<20} {u[2]:<20} {u[3]:<30}")
                print("-" * 75)

        elif scelta == '6':
            # Opzione 6: Registra prestito/i
            prestito = Loan(loan_id=0, user_id=int(input("Inserisci l'ID dell'utente: ").strip()),
                            isbn=input("Inserisci il codice ISBN del libro: ").strip(),
                            loan_date=input("Inserisci la data del prestito (YYYY-MM-DD): ").strip(),
                            return_date="")  # La data di restituzione sarà vuota fino a quando il libro non viene restituito
            prestito.add_loan()
            print("\nPrestito registrato con successo!")

        elif scelta == '7':
            # Opzione 7: Registra restituzione/i
            prestito = Loan(loan_id=int(input("Inserisci l'ID del prestito: ").strip()),
                            user_id=0, isbn='', loan_date='', return_date='')  # Creiamo un'istanza temporanea per accedere ai metodi
            prestito.add_return(return_date=input("Inserisci la data di restituzione (YYYY-MM-DD): ").strip())
            print("\nRestituzione registrata con successo!")

        elif scelta == '0':
            # Opzione 0: Esci dal programma
            print("\nGrazie per aver usato il gestionale biblioteca!")
            print("Arrivederci!")
            break  # Usciamo dal ciclo while e terminiamo il programma

        else:
            # Se l'utente inserisce un'opzione non valida
            print("\nERRORE: Opzione non valida! Riprova.")

        # Pausa prima di mostrare di nuovo il menu
        input("\nPremere INVIO per continuare...")

main()
