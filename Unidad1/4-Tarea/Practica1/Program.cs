using System;

namespace Practica1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese el modelo de su coche:");
            string modelo = Console.ReadLine();

            Console.WriteLine("Ingrese la marca de su coche:");
            string marca = Console.ReadLine();

            Coche miCoche = new Coche(marca, modelo);

            string respuesta = "1";
            do
            {
                Decidir(miCoche); // método estático abajo
                Console.WriteLine("¿Quieres decidir otra acción? si=1, no=2");
                respuesta = Console.ReadLine();
            }
            while (respuesta == "1");
        }

        static void Decidir(Coche coche)
        {
            Console.WriteLine("Elige: 1) Acelerar  2) Frenar");
            string opcion = Console.ReadLine();

            Console.WriteLine("Cantidad:");
            int cantidad = int.Parse(Console.ReadLine());

            if (opcion == "1") coche.Acelerar(cantidad);
            else coche.Frenar(cantidad);

            Console.WriteLine($"Velocidad actual: {coche.Velocidad} km/h");
        }
    }
}
