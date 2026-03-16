from servizio.database import DB_PATH, get_connection


def crea_database() -> None:
    with get_connection() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS dipendenti (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cognome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS posti_auto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codice TEXT NOT NULL UNIQUE,
                stato TEXT NOT NULL CHECK (stato IN ('disponibile', 'assegnato'))
            );

            CREATE TABLE IF NOT EXISTS assegnazioni (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dipendente_id INTEGER NOT NULL UNIQUE,
                posto_id INTEGER NOT NULL UNIQUE,
                FOREIGN KEY (dipendente_id) REFERENCES dipendenti(id) ON DELETE CASCADE,
                FOREIGN KEY (posto_id) REFERENCES posti_auto(id) ON DELETE CASCADE
            );
            """
        )


if __name__ == "__main__":
    crea_database()
    print(f"Database creato con successo in: {DB_PATH}")
