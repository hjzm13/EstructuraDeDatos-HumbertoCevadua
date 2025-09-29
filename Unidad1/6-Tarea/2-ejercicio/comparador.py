import random
import time
from claseBubbleSort import BubbleSort  

class Comparador:
    def __init__(self, dimensiones):
        self.dimensiones = dimensiones

    def medir_tiempo(self, func, datos):
        inicio = time.perf_counter()
        resultado = func(datos)
        fin = time.perf_counter()
        assert resultado == sorted(datos)  # verificación
        return fin - inicio

    def ejecutar(self):
        print("Tabla 2.1 - Tiempos de Ejecución por Dimensión")
        print("{:<10} {:<15} {:<15} {:<10}".format("Dimensión", "Bubble Sort (s)", "Sorted (s)", "Relación BS/MS"))

        for n in self.dimensiones:
            datos = random.sample(range(n * 10), n)
            t_bubble = self.medir_tiempo(BubbleSort.sort, datos)
            t_sorted = self.medir_tiempo(sorted, datos)
            print("{:<10} {:<15.5f} {:<15.5f} {:<10.2f}".format(
                n, t_bubble, t_sorted, t_bubble / t_sorted if t_sorted > 0 else 0))

    def ejecutar_casos(self):
        print("\nTabla 2.2 - Comportamiento en Casos Específicos (n=1000)")
        print("{:<15} {:<15} {:<15} {:<20}".format("Escenario", "Bubble Sort (s)", "Sorted (s)", "Observaciones"))

        # Caso 1: Ordenada
        ordenada = list(range(1000))
        t_bubble = self.medir_tiempo(BubbleSort.sort, ordenada)
        t_sorted = self.medir_tiempo(sorted, ordenada)
        print("{:<15} {:<15.5f} {:<15.5f} {:<20}".format("Ordenada", t_bubble, t_sorted, "Bubble aún lento"))

        # Caso 2: Inversa
        inversa = list(range(1000, 0, -1))
        t_bubble = self.medir_tiempo(BubbleSort.sort, inversa)
        t_sorted = self.medir_tiempo(sorted, inversa)
        print("{:<15} {:<15.5f} {:<15.5f} {:<20}".format("Inversa", t_bubble, t_sorted, "Peor caso para Bubble"))

        # Caso 3: Casi ordenada
        casi_ordenada = [x if x % 100 != 0 else x + 500 for x in range(1000)]
        t_bubble = self.medir_tiempo(BubbleSort.sort, casi_ordenada)
        t_sorted = self.medir_tiempo(sorted, casi_ordenada)
        print("{:<15} {:<15.5f} {:<15.5f} {:<20}".format("Casi ord.", t_bubble, t_sorted, "Caso intermedio"))
