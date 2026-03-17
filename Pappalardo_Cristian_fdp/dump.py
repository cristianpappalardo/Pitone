import sqlite3

def dump(conn):
    try:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS prenotazioni ')
        cur.execute('DROP TABLE IF EXISTS aule_studio ')
        cur.execute('DROP TABLE IF EXISTS studenti ')

        cur.execute('''CREATE TABLE studenti (
            studenti_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT not null ,
            cognome TEXT not null,
            email text not null 
    )''')
        
        cur.execute('''CREATE TABLE aule_studio(
            nome_aula TEXT not null,
            aula_id INTEGER PRIMARY KEY AUTOINCREMENT,
            posti_disponibili INTEGER      
    )''')

        cur.execute('''CREATE TABLE prenotazioni(
                    prenotazioni_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studenti_id INTEGER not null,
                    aula_id INTEGER not null,
                    FOREIGN KEY (studenti_id) REFERENCES studenti(studenti_id),
                    FOREIGN KEY (aula_id) REFERENCES aule_studio(aula_id)
    )''')

        cur.execute('''INSERT INTO aule_studio (nome_aula, aula_id, posti_disponibili) VALUES (?, ?, ?)''', ("Dummy", 1, 10))

        conn.commit()
        return "Database inizializzato correttamente"
    except sqlite3.Error as e:
        conn.rollback()
        return f"Errore durante l'inizializzazione del database: {e}"


if __name__ == "__main__":
    connection = None
    try:
        connection = sqlite3.connect("aule_studio_ITS.sqlite")
        print(dump(connection))
    except sqlite3.Error:
        print("Errore di connessione al database")
    finally:
        if connection is not None:
            connection.close()