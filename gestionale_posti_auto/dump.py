import sqlite3

conn = sqlite3.connect("parcheggio.sqlite")

def dump(conn):
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS dipendenti ')
    cur.execute('DROP TABLE IF EXISTS posti ')
    cur.execute('DROP TABLE IF EXISTS assegnazioni ')

    cur.execute('''CREATE TABLE dipendenti (
        dipendente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT not null ,
        cognome TEXT not null,
        num_cell INTEGER not null ,
        email text not null 
)''')
    
    cur.execute('''CREATE TABLE posti_auto(
        posto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assegnazione TEXT not null      
)''')

    cur.execute('''CREATE TABLE assegnazione_posti(
                assegnazione_id INTEGER PRIMARY KEY AUTOINCREMENT,
                dipendente_id INTEGER not null,
                posto_id INTEGERE not null,
                FOREIGN KEY (dipendente_id) REFERENCES dipendenti(dipendente_id),
                FOREIGN KEY (posto_id) REFERENCES posti_auto(posto_id)
)''')


conn.commit()
conn.close()