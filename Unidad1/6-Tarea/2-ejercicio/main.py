from comparador import Comparador

class Main:
    @staticmethod
    def run():
        dimensiones = [100, 500, 1000, 5000, 10000]
        comparador = Comparador(dimensiones)
        comparador.ejecutar()
        comparador.ejecutar_casos()

if __name__ == "__main__":
    Main.run()
