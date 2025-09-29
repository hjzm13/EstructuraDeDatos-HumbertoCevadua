


def main():
    alumnos = []  # lista vacía

    while True:
        nombre = input("Ingresa el nombre del alumno (escribe 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
        alumnos.append(nombre)

    print("\n--- Lista de alumnos registrados ---")
    for alumno in alumnos:
        print("-", alumno)

    print(f"\nTotal de alumnos registrados: {len(alumnos)}")

# Punto de entrada
if __name__ == "__main__":
    main()
