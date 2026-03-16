from dump import crea_database
from servizio.parcheggio_service import ParcheggioService


service = ParcheggioService()


def leggi_intero(prompt: str) -> int:
    while True:
        valore = input(prompt).strip()
        if valore.isdigit():
            return int(valore)
        print("Valore non valido. Inserire un numero intero.")


def stampa_menu() -> None:
    print("\n=== Gestione Parcheggio Aziendale ===")
    print("1. Inserisci dipendente")
    print("2. Visualizza dipendenti")
    print("3. Inserisci posto auto")
    print("4. Visualizza posti auto")
    print("5. Aggiorna stato posto auto")
    print("6. Elimina posto auto")
    print("7. Crea assegnazione")
    print("8. Visualizza assegnazioni")
    print("9. Rimuovi assegnazione")
    print("0. Esci")


def inserisci_dipendente() -> None:
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    email = input("Email: ").strip()

    dipendente = service.aggiungi_dipendente(nome, cognome, email)
    print(f"Dipendente inserito con ID {dipendente.id}.")


def visualizza_dipendenti() -> None:
    dipendenti = service.lista_dipendenti()
    if not dipendenti:
        print("Nessun dipendente registrato.")
        return

    for d in dipendenti:
        print(f"[{d.id}] {d.nome} {d.cognome} - {d.email}")


def inserisci_posto() -> None:
    codice = input("Codice posto (es. A01): ").strip()
    posto = service.aggiungi_posto_auto(codice)
    print(f"Posto auto inserito con ID {posto.id}.")


def visualizza_posti() -> None:
    posti = service.lista_posti_auto()
    if not posti:
        print("Nessun posto auto registrato.")
        return

    for p in posti:
        print(f"[{p.id}] Codice: {p.codice} - Stato: {p.stato}")


def aggiorna_stato_posto() -> None:
    posto_id = leggi_intero("ID posto auto: ")
    stato = input("Nuovo stato (disponibile/assegnato): ").strip().lower()
    service.aggiorna_stato_posto(posto_id, stato)
    print("Stato aggiornato con successo.")


def elimina_posto() -> None:
    posto_id = leggi_intero("ID posto auto da eliminare: ")
    service.elimina_posto_auto(posto_id)
    print("Posto auto eliminato con successo.")


def crea_assegnazione() -> None:
    dipendente_id = leggi_intero("ID dipendente: ")
    posto_id = leggi_intero("ID posto auto: ")
    assegnazione = service.assegna_posto(dipendente_id, posto_id)
    print(f"Assegnazione creata con ID {assegnazione.id}.")


def visualizza_assegnazioni() -> None:
    assegnazioni = service.lista_assegnazioni()
    if not assegnazioni:
        print("Nessuna assegnazione presente.")
        return

    for a in assegnazioni:
        print(
            f"[{a['id']}] Dipendente: {a['dipendente']} (ID {a['dipendente_id']})"
            f" -> Posto: {a['posto_codice']} (ID {a['posto_id']})"
        )


def rimuovi_assegnazione() -> None:
    dipendente_id = leggi_intero("ID dipendente da liberare: ")
    service.rimuovi_assegnazione(dipendente_id)
    print("Assegnazione rimossa con successo.")


def main() -> None:
    crea_database()

    azioni = {
        "1": inserisci_dipendente,
        "2": visualizza_dipendenti,
        "3": inserisci_posto,
        "4": visualizza_posti,
        "5": aggiorna_stato_posto,
        "6": elimina_posto,
        "7": crea_assegnazione,
        "8": visualizza_assegnazioni,
        "9": rimuovi_assegnazione,
    }

    while True:
        stampa_menu()
        scelta = input("Seleziona un'opzione: ").strip()

        if scelta == "0":
            print("Uscita dal programma.")
            break

        azione = azioni.get(scelta)
        if azione is None:
            print("Scelta non valida.")
            continue

        try:
            azione()
        except ValueError as exc:
            print(f"Errore: {exc}")
        except Exception as exc:
            print(f"Errore inatteso: {exc}")


if __name__ == "__main__":
    main()
