from cliente import Cliente
from sala import Sala
from prenotazione import Prenotazione

# registrazione cliente
def registrazione_cliente(conn):
    nome_gruppo = input("Inserire il nome del gruppo: ")
    nome_referente = input("Inserire il nome del referente: ")
    num_cell = input("Inserire il numero del cellulare del referente: ")
    email = input("Inserire l'email del referente: ")

    cliente = Cliente(nome_gruppo, nome_referente, num_cell, email)

    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO clienti VALUES (?, ?, ?, ?)',
                    (cliente.nome_gruppo, cliente.nome_referente, cliente.num_cell, cliente.email))
    except Exception as e:
        print("Error:", e)

    return

# visualizzazione clienti
def visualizza_clienti(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM clienti')
    clienti = cur.fetchall()

    for cliente in clienti:
        print(cliente)

# creazione sala
def creazione_sala(conn):
    nome_sala = input("Inserire il nome della sala: ")
    prenotazione = "non attiva"

    sala = Sala(nome_sala, prenotazione)

    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO sale VALUES (?, ?)', (sala.nome_sala, sala.prenotazione))
    except Exception as e:
        print("Error:", e)

    return

# visualizzazione sale
def visualizza_sale(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM sale')
    sale = cur.fetchall()

    for sala in sale:
        print(sala)

# creazione prenotazione
def nuova_prenotazione(conn):
    while True:
        inizio_prenotazione = int(input("Inserire l'ora di inizio:"))
        fine_prenotazione = int(input("Inserire l'ora di fine:"))
        if inizio_prenotazione > fine_prenotazione:
            print("l'ora d'inizio non può essere maggiore dell'ora di fine")
            continue
        elif fine_prenotazione - inizio_prenotazione > 1:
            print("la sala non può essere prenotata per più di un'ora")
            continue
        else:
            
            break

    prenotazione = Prenotazione(inizio_prenotazione, fine_prenotazione)

    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO prenotazione VALUES (?, ?)", (prenotazione.inizio_prenotazione, prenotazione.fine_prenotazione))
    except Exception as e:
        print("Error:", e)

# visualizzazione prenotazioni
def visualizza_prenotazioni(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM prenotazione')
    prenotazioni = cur.fetchall()

    for prenotazione in prenotazioni:
        print(prenotazione)



