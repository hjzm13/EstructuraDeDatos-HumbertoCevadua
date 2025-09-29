


from dataclasses import dataclass

@dataclass(frozen=True)
class Usuario:
    id: int
    nombre: str
    correo: str

@dataclass(order=True, frozen=True)
class Producto:
    precio: float
    id: int
    nombre: str
