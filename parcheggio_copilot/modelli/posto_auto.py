from dataclasses import dataclass


@dataclass(frozen=True)
class PostoAuto:
    id: int
    codice: str
    stato: str
