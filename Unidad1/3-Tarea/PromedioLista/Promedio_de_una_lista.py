def calcular_promedio_lista(lista):
    if len(lista)==0:
        return 0
    else:
        return sum(lista)/len(lista)

print("caluladora de promedio")
entrada = input("Ingresa los números separados por espacio: ")
# convertimos la cadena a una lista de enteros o flotantes
#    split() -> separa por espacios
#    map(float, ...) -> convierte cada dato a número decimal
numeros = list(map(float,entrada.split()))
#resultado
resultado = calcular_promedio_lista(numeros)
print("El promedio es:", resultado)