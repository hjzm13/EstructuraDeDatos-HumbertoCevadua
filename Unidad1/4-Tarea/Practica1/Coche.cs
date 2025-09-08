    public class Coche
{
    public string Marca { get; set; }
    public string Modelo { get; set; }
    public int Velocidad { get; private set; }

    public Coche(string marca, string modelo)
    {
        Marca = marca;
        Modelo = modelo;
        Velocidad = 0;
    }

    public void Acelerar(int cantidad)
    {
        Velocidad += cantidad;
    }

    public void Frenar(int cantidad)
    {
        Velocidad -= cantidad;
        if (Velocidad < 0) Velocidad = 0;
    }
}

