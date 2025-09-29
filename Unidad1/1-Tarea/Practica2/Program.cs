namespace Practica2;

class Program
{
    //Calcule el area de un circulo dado su radio 
    static void Main(string[] args)
    {
        //Practica 2
        Console.WriteLine("Practica 2.- Calcular el area de un circulo ");
        Instrucciones();

    }
    public static double CalcularAreaCirculo(double radio)
    {
        // Area = Pi*radio^2
        double area = Math.PI * Math.Pow(radio, 2);
        return area;
    }
    public static void Instrucciones()
    {
        System.Console.WriteLine("Ingrese el radio del circula para saber su Area");
        double radio = double.Parse(Console.ReadLine());
        double Area = CalcularAreaCirculo(radio);
        System.Console.WriteLine($"El area de su circulo es: {Area} ");
    }
}
