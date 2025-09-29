using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;

namespace Practica2;

class Program
{
    static void Main(string[] args)
    {
        string opcion;

        do
        {
            JuegoPrincipal();

            Console.Write("\n¿Quieres jugar de nuevo? (si = 1/no = 2): ");
            opcion = Console.ReadLine();

        } while (opcion == "1");
    }

    public static int LeerNumeroEntero()
    {
        int numero;
        while (!int.TryParse(Console.ReadLine(), out numero))
        {
            System.Console.WriteLine("Ingresa un numero Entero");
        }
        return numero;
    }
    public static int LimiteMax()
    {
        int limite;
        System.Console.WriteLine("Ingrese el limete Ejemplo: 100");
        limite = LeerNumeroEntero();
        while (limite < 2)
        {
            Console.Write("El límite debe ser >= 2. Intente de nuevo: ");
            limite = LeerNumeroEntero();
        }
        return limite;
    }
    public static void JuegoPrincipal()
    {
        System.Console.WriteLine("===Adivine el Numero===");
        int max = LimiteMax();
        //General numero random
        Random numAlatorio = new Random();
        int secreto = numAlatorio.Next(1, max + 1);
        //bucle
        int intentos = 0;
        System.Console.WriteLine($"He pensado un número entre 1 y {max}. Adivinalo");
        System.Console.Write("Tu intento: ");
        while (true)
        {
            int intento = LeerNumeroEntero();
            intentos++;
            if (secreto == intento)
            {
                System.Console.WriteLine($"Correcto!!! Era {secreto}. Intentos: {intentos}");
                break;
            }
            else if (intento < 2 || intento > max)
            {
                System.Console.WriteLine($"Fuera de rango. Debe estar entre 1 y {max}.");
            }
            else if (intento < secreto)
            {
                System.Console.WriteLine("bajo");
            }
            else if (intento > secreto)
            {
                System.Console.WriteLine("alto");
            }
            else
            {
                System.Console.WriteLine("intente de nuevo");
            }
        }

    }
}
