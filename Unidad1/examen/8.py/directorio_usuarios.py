

from typing import Iterable, Optional
from modelos import Usuario

class DirectorioUsuarios:
    def __init__(self):
        
        self._usuarios = {}

    def cargar(self, usuarios: Iterable[Usuario]) -> None:
        for u in usuarios:
            self._usuarios[u.id] = u

    def agregar(self, usuario: Usuario) -> None:
        # Agrega o reemplaza por id
        self._usuarios[usuario.id] = usuario

    def buscar_por_id(self, user_id: int) -> Optional[Usuario]:
        # Retorna el usuario si existe, si no, None
        return self._usuarios.get(user_id)

    def cantidad(self) -> int:
        return len(self._usuarios)
