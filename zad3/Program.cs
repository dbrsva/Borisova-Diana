using System;

class Program
{
    static void Main()
    {
        double sum = 0;

        for (int i = 1; i <= 7; i++)
        {
            Console.Write("Введите температуру за день " + i + ": ");
            double temp = Convert.ToDouble(Console.ReadLine());
            sum = sum + temp;
        }

        double average = sum / 7;

        Console.WriteLine("Средняя температура за неделю: " + average);
    }
}
