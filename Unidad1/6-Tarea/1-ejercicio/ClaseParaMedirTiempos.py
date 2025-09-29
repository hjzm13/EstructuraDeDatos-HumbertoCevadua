import time
import random
from ClaseParaBusquedas import Busquedas
class Comparador:
    def __init__(self, tamanos):
        self.tamanos = tamanos
    
    def ejecutar(self):
        print(f"{'Tamaño':<10}{'Lineal (s)':<15}{'Binaria (s)':<15}{'Ratio L/B':<10}")
        print("-"*50)
        
        for n in self.tamanos:
            lista = list(range(n))  # lista ordenada
            buscador = Busquedas(lista)
            
            # 5 elementos que existen y 5 que no
            existentes = random.sample(lista, 5)
            no_existentes = [n + i for i in range(5)]
            pruebas = existentes + no_existentes
            
            # --- Búsqueda lineal ---
            inicio = time.time()
            for objetivo in pruebas:
                buscador.lineal(objetivo)
            fin = time.time()
            tiempo_lineal = (fin - inicio) / len(pruebas)
            
            # --- Búsqueda binaria ---
            inicio = time.time()
            for objetivo in pruebas:
                buscador.binaria(objetivo)
            fin = time.time()
            tiempo_binaria = (fin - inicio) / len(pruebas)
            
            ratio = tiempo_lineal / tiempo_binaria if tiempo_binaria > 0 else float('inf')
            
            print(f"{n:<10}{tiempo_lineal:<15.8f}{tiempo_binaria:<15.8f}{ratio:<10.2f}")
