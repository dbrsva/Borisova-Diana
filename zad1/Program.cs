using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите длину прямоугольника: ");
        double a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Введите ширину прямоугольника: ");
        double b = Convert.ToDouble(Console.ReadLine());

        double area = a * b;
        double perimeter = 2 * (a + b);

        Console.WriteLine("Площадь прямоугольника: " + area);
        Console.WriteLine("Периметр прямоугольника: " + perimeter);
    }
}