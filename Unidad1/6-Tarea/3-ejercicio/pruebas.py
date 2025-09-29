import time
from fibonacci_recursivo import FibonacciRecursivo
from fibonacci_iterativo import FibonacciIterativo
from fibonacci_memo import FibonacciMemo

class PruebasFibonacci:
    @staticmethod
    def medir_tiempos(valores_n):
        resultados = []

        for n in valores_n:
            fila = {"n": n}

            # Fibonacci recursivo
            inicio = time.time()
            resultado_rec = FibonacciRecursivo.calcular(n)
            fin = time.time()
            tiempo_rec = fin - inicio

            # Fibonacci iterativo
            inicio = time.time()
            resultado_it = FibonacciIterativo.calcular(n)
            fin = time.time()
            tiempo_it = fin - inicio

            # Verificación
            assert resultado_rec == resultado_it, f"Error en n={n}"

            fila["Fibonacci"] = resultado_it
            fila["Recursivo (s)"] = round(tiempo_rec, 6)
            fila["Iterativo (s)"] = round(tiempo_it, 6)
            fila["Diferencia"] = round(tiempo_rec - tiempo_it, 6)

            resultados.append(fila)

        return resultados
