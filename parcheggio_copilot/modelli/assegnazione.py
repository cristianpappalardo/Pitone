from dataclasses import dataclass


@dataclass(frozen=True)
class Assegnazione:
    id: int
    dipendente_id: int
    posto_id: int
