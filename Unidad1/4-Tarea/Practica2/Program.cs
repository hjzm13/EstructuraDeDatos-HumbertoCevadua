namespace Practica2;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("\n=== Registro de libro ===");
        Console.Write("Título: ");
        string titulo = Console.ReadLine();

        Console.Write("Autor: ");
        string autor = Console.ReadLine();

        Libro miLibro = new Libro(titulo, autor);
        miLibro.MostrarInformacion(); 
    }
}
