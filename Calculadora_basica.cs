using System;

class Program
{
    static int Sumar(int a, int b) => a + b;
    static int Restar(int a, int b) => a - b;
    static int Multiplicar(int a, int b) => a * b;
    static int Dividir(int a, int b) => b != 0 ? a / b : throw new DivideByZeroException("No se puede dividir por cero.");

    static void Menu()
    {
        while (true)
        {
            Console.WriteLine("\nSeleccione una operación:");
            Console.WriteLine("1. Sumar");
            Console.WriteLine("2. Restar");
            Console.WriteLine("3. Multiplicar");
            Console.WriteLine("4. Dividir");
            Console.WriteLine("5. Salir");
            Console.Write("Opción: ");

            string opcion = Console.ReadLine();
            if (opcion == "5") break;

            Console.Write("Ingrese el primer número: ");
            int num1 = int.Parse(Console.ReadLine());

            Console.Write("Ingrese el segundo número: ");
            int num2 = int.Parse(Console.ReadLine());

            try
            {
                int resultado = opcion switch
                {
                    "1" => Sumar(num1, num2),
                    "2" => Restar(num1, num2),
                    "3" => Multiplicar(num1, num2),
                    "4" => Dividir(num1, num2),
                    _ => throw new Exception("Opción no válida.")
                };

                Console.WriteLine($"Resultado: {resultado}");
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }
    }

    static void Main()
    {
        Menu();
    }
}
