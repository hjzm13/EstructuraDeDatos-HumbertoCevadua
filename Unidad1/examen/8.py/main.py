
import random
from modelos import Usuario, Producto
from directorio_usuarios import DirectorioUsuarios
from indice_productos import IndiceProductos
from estadistica_en_linea import EstadisticaEnLinea

def demo_busqueda_usuarios():
    print("=== BÚSQUEDA DE USUARIOS POR ID ===")
    n = 1_000_000
    directorio = DirectorioUsuarios()
    # Generamos usuarios: id=0..n-1
    directorio.cargar(Usuario(id=i, nombre=f"Usuario{i}", correo=f"u{i}@mail.com") for i in range(n))
    print(f"Usuarios cargados: {directorio.cantidad():,}")

    # Pruebas de búsqueda
    for prueba_id in [0, n//2, n-1, n+5]:
        u = directorio.buscar_por_id(prueba_id)
        resultado = f"ENCONTRADO: {u.nombre}" if u else "NO EXISTE"
        print(f"Buscar id {prueba_id}: {resultado}")

def demo_ordenamientos_productos():
    print("\n=== ORDENAMIENTO DE PRODUCTOS POR PRECIO ===")
    m = 10_000
    indice = IndiceProductos()
    # Productos con precios aleatorios (1.00 a 1000.00)
    productos = [
        Producto(id=i, nombre=f"Prod{i}", precio=round(random.uniform(1.0, 1000.0), 2))
        for i in range(m)
    ]
    indice.cargar(productos)
    print(f"Productos cargados: {indice.cantidad():,}")

    # Lista completa ordenada por precio
    ordenados = indice.ordenar_por_precio()
    print(f"Más barato: ${ordenados[0].precio}  |  Más caro: ${ordenados[-1].precio}")

    # Top-K sencillos
    k = 5
    baratos = indice.top_k_baratos(k)
    caros = indice.top_k_caros(k)
    print(f"Top {k} baratos:", [p.precio for p in baratos])
    print(f"Top {k} caros  :", [p.precio for p in caros])

def demo_estadistica_en_tiempo_real():
    print("\n=== ESTADÍSTICA EN TIEMPO REAL (STREAM) ===")
    stats = EstadisticaEnLinea()
    # Simulamos lecturas 
    random.seed(7)
    for _ in range(50_000):
        x = random.gauss(100, 15)  # media 100, desviación 15
        stats.actualizar(x)

    print("Resumen:", stats.resumen())

if __name__ == "__main__":
    demo_busqueda_usuarios()
    demo_ordenamientos_productos()
    demo_estadistica_en_tiempo_real()
