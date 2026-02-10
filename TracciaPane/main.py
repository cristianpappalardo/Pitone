import pane
import cassa
import transazioni


def main():
    #inizio main    
    while True:
        print("----Menu principale----")
        print("1.Visualizza i tipi di pane")
        print("2.Cerca un tipo di pane")
        print("3.Inserisci un nuovo tipo di pane")
        print("4.Modifica il prezzo di un tipo di pane\n")
        print("5.Leggi il saldo attuale")
        print("6.Aggiungi denaro in cassa\n")
        print("7.Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            print(pane.leggi_file())
        if scelta == "2":
            print(pane.cerca_pane())
        if scelta == "3":
            pane.nuovo_pane()
        if scelta == "4":
            pane.modifica_pane()
        if scelta == "5":
            print(cassa.leggi_saldo("cassa.json"))
        if scelta == "6":
            cassa.aggiungi_denaro()
        elif scelta == "7":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

    #fine main
        
if __name__ == main:
    main()