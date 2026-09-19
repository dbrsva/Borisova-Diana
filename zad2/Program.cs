using System;

class Program
{
    static void Main()
    {
        double rate = 82.5;

        Console.Write("Введите количество рублей: ");
        double rubles = Convert.ToDouble(Console.ReadLine());

        double dollars = rubles / rate;

        Console.WriteLine("Это составляет " + dollars + " долларов");
    }
}
