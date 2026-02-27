import sqlite3

conn = sqlite3.connect('musicale.sqlite')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS clienti ')
cur.execute('''CREATE TABLE clienti (
    clienti_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_gruppo TEXT not null ,
    nome_referente TEXT not null,
    num_cell INTEGER not null ,
    email text not null 
)''')



cur.execute('DROP TABLE IF EXISTS sale ')
cur.execute('''CREATE TABLE sale (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_sala TEXT NOT NULL,
    prenotazione TEXT NOT NULL 
)''')


cur.execute('DROP TABLE IF EXISTS prenotazioni ')
cur.execute('''CREATE TABLE prenotazioni (
    prenotazione_id INTEGER PRIMARY KEY AUTOINCREMENT,
    clienti_id INTEGER NOT NULL,
    sale_id INTEGER NOT NULL,
    inizio_prenotazione TEXT not null ,
    fine_prenotazione TEXT not null ,
    FOREIGN KEY (clienti_id) REFERENCES clienti(clienti_id),
    FOREIGN KEY (sale_id) REFERENCES sale(sale_id)
)''')

conn.commit()
conn.close()