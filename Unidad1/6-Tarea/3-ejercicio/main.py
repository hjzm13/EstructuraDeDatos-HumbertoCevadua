from pruebas import PruebasFibonacci

if __name__ == "__main__":
    valores_n = [5, 10, 20, 30, 35]
    resultados = PruebasFibonacci.medir_tiempos(valores_n)

    print("\nTabla de Resultados:\n")
    print(f"{'n':<5}{'Fibonacci':<15}{'Recursivo (s)':<15}{'Iterativo (s)':<15}{'Diferencia':<15}")
    for fila in resultados:
        print(f"{fila['n']:<5}{fila['Fibonacci']:<15}{fila['Recursivo (s)']:<15}{fila['Iterativo (s)']:<15}{fila['Diferencia']:<15}")
