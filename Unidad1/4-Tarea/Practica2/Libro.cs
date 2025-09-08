
    public class Libro
    {
        // Propiedades
        public string Titulo { get; set; }
        public string Autor  { get; set; }

        // Constructor
        public Libro(string titulo, string autor)
        {
            Titulo = titulo ?? "";
            Autor  = autor  ?? "";
        }

        // Método de instancia
        public void MostrarInformacion()
        {
            Console.WriteLine($" \"{Titulo}\" — {Autor}");
        }

      
    }

