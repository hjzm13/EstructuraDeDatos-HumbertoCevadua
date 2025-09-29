# indice_productos.py
# Ordenamientos y consultas por precio

from typing import Iterable, List
from modelos import Producto

class IndiceProductos:
    def __init__(self):
        self._productos: List[Producto] = []
        self._ordenados: List[Producto] = []  

    def cargar(self, productos: Iterable[Producto]) -> None:
        self._productos = list(productos)
        self._ordenados = []  

    def agregar(self, producto: Producto) -> None:
        self._productos.append(producto)
        self._ordenados = [] 

    def ordenar_por_precio(self) -> List[Producto]:
        
        if not self._ordenados:
            self._ordenados = sorted(self._productos)  # usa precio primero
        return self._ordenados

    def top_k_baratos(self, k: int) -> List[Producto]:
    
        return sorted(self._productos)[:k]

    def top_k_caros(self, k: int) -> List[Producto]:
        return sorted(self._productos, reverse=True)[:k]

    def cantidad(self) -> int:
        return len(self._productos)
