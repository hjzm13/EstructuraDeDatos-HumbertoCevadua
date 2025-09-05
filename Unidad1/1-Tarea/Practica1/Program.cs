using System.Diagnostics.Metrics;

internal class Program
{
    // Crear un programa que convierta grado celisius a Fahrenheit.
    private static void Main(string[] args)
    {
        Console.WriteLine("Practica 1");
        instructiones();
    }
    public static void instructiones()
    {
        Console.WriteLine("Agregue la temperatura en Celsius que quiera convertir a fahrenheit");
        double gradosC = double.Parse(Console.ReadLine());
        double gradosF = ConvertirCelAFah(gradosC);
        Console.WriteLine($"La temperatura en farhanheit es {gradosF}");
    }
    public static double ConvertirCelAFah(double celisius)
    {
        double fahrenheit = 0;
        // formula = F=(C×1.8)+32
        fahrenheit = (celisius * 1.8) + 32;
        return fahrenheit;
    }
}