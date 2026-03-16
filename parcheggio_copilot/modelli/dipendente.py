from dataclasses import dataclass


@dataclass(frozen=True)
class Dipendente:
    id: int
    nome: str
    cognome: str
    email: str
