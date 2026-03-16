import sqlite3

def dump(conn):
    try:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS assegnazione_posti ')
        cur.execute('DROP TABLE IF EXISTS posti_auto ')
        cur.execute('DROP TABLE IF EXISTS dipendenti ')

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
                    posto_id INTEGER not null,
                    UNIQUE(dipendente_id),
                    UNIQUE(posto_id),
                    FOREIGN KEY (dipendente_id) REFERENCES dipendenti(dipendente_id),
                    FOREIGN KEY (posto_id) REFERENCES posti_auto(posto_id)
    )''')

        conn.commit()
        return "Database inizializzato correttamente"
    except sqlite3.Error as e:
        conn.rollback()
        return f"Errore durante l'inizializzazione del database: {e}"


if __name__ == "__main__":
    connection = None
    try:
        connection = sqlite3.connect("parcheggio.sqlite")
        print(dump(connection))
    except sqlite3.Error:
        print("Errore di connessione al database")
    finally:
        if connection is not None:
            connection.close()