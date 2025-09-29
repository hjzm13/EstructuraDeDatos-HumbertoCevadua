import time
import random

class Busquedas:
    def __init__(self, lista):
        self.lista = lista
    
    def lineal(self, objetivo):
        """
        Búsqueda lineal O(n)
        Retorna posición del elemento o -1 si no existe
        """
        for i, elemento in enumerate(self.lista):
            if elemento == objetivo:
                return i
        return -1
    
    def binaria(self, objetivo):
        """
        Búsqueda binaria O(log n)
        PRECONDICIÓN: lista debe estar ordenada
        """
        izquierda, derecha = 0, len(self.lista) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if self.lista[medio] == objetivo:
                return medio
            elif self.lista[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1
