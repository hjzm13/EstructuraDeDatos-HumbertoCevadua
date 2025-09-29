namespace Practica1;

class Program
{
    static void Main(string[] args)
    {

        Console.Write("Ingresa un número entero: ");
        if (!int.TryParse(Console.ReadLine(), out int numero))
        {
            Console.WriteLine("Entrada inválida.");
            return;
        }

        Console.WriteLine(EsPrimo(numero) ? "Es primo" : "No es primo");
    }

    // Devuelve true si numero es primo; false en caso contrario.
    static bool EsPrimo(int numero)
    {
        if (numero < 2) return false;      // 0, 1 y negativos no son primos
        if (numero % 2 == 0) return numero == 2; // 2 es el único par primo

        // Probar solo impares hasta sqrt(n)
        for (int divisor = 3; divisor <= Math.Sqrt(numero); divisor += 2)
        {
            if (numero % divisor == 0) return false;
        }
        return true;
    }
}
