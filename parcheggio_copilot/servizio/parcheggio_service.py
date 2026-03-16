from __future__ import annotations

from typing import List

from modelli import Assegnazione, Dipendente, PostoAuto

from .database import get_connection


class ParcheggioService:
    def aggiungi_dipendente(self, nome: str, cognome: str, email: str) -> Dipendente:
        if not nome.strip() or not cognome.strip() or not email.strip():
            raise ValueError("Nome, cognome ed email sono obbligatori.")

        query = """
            INSERT INTO dipendenti (nome, cognome, email)
            VALUES (?, ?, ?)
        """

        with get_connection() as conn:
            try:
                cur = conn.execute(query, (nome.strip(), cognome.strip(), email.strip().lower()))
                dipendente_id = cur.lastrowid
            except Exception as exc:
                raise ValueError(f"Errore inserimento dipendente: {exc}") from exc

        return Dipendente(dipendente_id, nome.strip(), cognome.strip(), email.strip().lower())

    def lista_dipendenti(self) -> List[Dipendente]:
        query = "SELECT id, nome, cognome, email FROM dipendenti ORDER BY cognome, nome"

        with get_connection() as conn:
            rows = conn.execute(query).fetchall()

        return [Dipendente(r["id"], r["nome"], r["cognome"], r["email"]) for r in rows]

    def aggiungi_posto_auto(self, codice: str) -> PostoAuto:
        if not codice.strip():
            raise ValueError("Il codice del posto auto e obbligatorio.")

        query = "INSERT INTO posti_auto (codice, stato) VALUES (?, 'disponibile')"

        with get_connection() as conn:
            try:
                cur = conn.execute(query, (codice.strip().upper(),))
                posto_id = cur.lastrowid
            except Exception as exc:
                raise ValueError(f"Errore inserimento posto auto: {exc}") from exc

        return PostoAuto(posto_id, codice.strip().upper(), "disponibile")

    def lista_posti_auto(self) -> List[PostoAuto]:
        query = "SELECT id, codice, stato FROM posti_auto ORDER BY codice"

        with get_connection() as conn:
            rows = conn.execute(query).fetchall()

        return [PostoAuto(r["id"], r["codice"], r["stato"]) for r in rows]

    def aggiorna_stato_posto(self, posto_id: int, nuovo_stato: str) -> None:
        stato = nuovo_stato.strip().lower()
        if stato not in {"disponibile", "assegnato"}:
            raise ValueError("Stato non valido. Usa 'disponibile' o 'assegnato'.")

        with get_connection() as conn:
            posto = conn.execute("SELECT id FROM posti_auto WHERE id = ?", (posto_id,)).fetchone()
            if posto is None:
                raise ValueError("Posto auto non trovato.")

            if stato == "disponibile":
                # Se si forza disponibile, eventuali assegnazioni devono sparire.
                conn.execute("DELETE FROM assegnazioni WHERE posto_id = ?", (posto_id,))

            conn.execute("UPDATE posti_auto SET stato = ? WHERE id = ?", (stato, posto_id))

    def elimina_posto_auto(self, posto_id: int) -> None:
        with get_connection() as conn:
            posto = conn.execute("SELECT id FROM posti_auto WHERE id = ?", (posto_id,)).fetchone()
            if posto is None:
                raise ValueError("Posto auto non trovato.")

            conn.execute("DELETE FROM posti_auto WHERE id = ?", (posto_id,))

    def assegna_posto(self, dipendente_id: int, posto_id: int) -> Assegnazione:
        with get_connection() as conn:
            dipendente = conn.execute("SELECT id FROM dipendenti WHERE id = ?", (dipendente_id,)).fetchone()
            if dipendente is None:
                raise ValueError("Dipendente non trovato.")

            posto = conn.execute(
                "SELECT id, stato FROM posti_auto WHERE id = ?",
                (posto_id,),
            ).fetchone()
            if posto is None:
                raise ValueError("Posto auto non trovato.")

            gia_assegnato = conn.execute(
                "SELECT id FROM assegnazioni WHERE dipendente_id = ?",
                (dipendente_id,),
            ).fetchone()
            if gia_assegnato is not None:
                raise ValueError("Il dipendente ha gia un posto assegnato.")

            occupato = conn.execute(
                "SELECT id FROM assegnazioni WHERE posto_id = ?",
                (posto_id,),
            ).fetchone()
            if occupato is not None or posto["stato"] == "assegnato":
                raise ValueError("Il posto auto e gia assegnato.")

            cur = conn.execute(
                "INSERT INTO assegnazioni (dipendente_id, posto_id) VALUES (?, ?)",
                (dipendente_id, posto_id),
            )
            assegnazione_id = cur.lastrowid
            conn.execute("UPDATE posti_auto SET stato = 'assegnato' WHERE id = ?", (posto_id,))

        return Assegnazione(assegnazione_id, dipendente_id, posto_id)

    def rimuovi_assegnazione(self, dipendente_id: int) -> None:
        with get_connection() as conn:
            assegnazione = conn.execute(
                "SELECT id, posto_id FROM assegnazioni WHERE dipendente_id = ?",
                (dipendente_id,),
            ).fetchone()

            if assegnazione is None:
                raise ValueError("Nessuna assegnazione trovata per il dipendente indicato.")

            conn.execute("DELETE FROM assegnazioni WHERE id = ?", (assegnazione["id"],))
            conn.execute(
                "UPDATE posti_auto SET stato = 'disponibile' WHERE id = ?",
                (assegnazione["posto_id"],),
            )

    def lista_assegnazioni(self) -> List[dict]:
        query = """
            SELECT
                a.id,
                d.id AS dipendente_id,
                d.nome,
                d.cognome,
                p.id AS posto_id,
                p.codice
            FROM assegnazioni a
            JOIN dipendenti d ON d.id = a.dipendente_id
            JOIN posti_auto p ON p.id = a.posto_id
            ORDER BY d.cognome, d.nome
        """

        with get_connection() as conn:
            rows = conn.execute(query).fetchall()

        return [
            {
                "id": row["id"],
                "dipendente_id": row["dipendente_id"],
                "dipendente": f"{row['nome']} {row['cognome']}",
                "posto_id": row["posto_id"],
                "posto_codice": row["codice"],
            }
            for row in rows
        ]
