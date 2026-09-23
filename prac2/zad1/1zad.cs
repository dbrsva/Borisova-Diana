using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите размер массива N: ");
        int n = Convert.ToInt32(Console.ReadLine());

        int[] numbers = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            Console.Write("Введите число " + (i + 1) + ": ");
            numbers[i] = Convert.ToInt32(Console.ReadLine());
            sum = sum + numbers[i];
        }

        double average = (double)sum / n;

        Console.WriteLine("Массив в обратном порядке:");
        for (int i = n - 1; i >= 0; i--)
        {
            Console.Write(numbers[i] + " ");
        }
        Console.WriteLine();

        int closest = numbers[0];
        double minDifference = Math.Abs(numbers[0] - average);

        for (int i = 1; i < n; i++)
        {
            double difference = Math.Abs(numbers[i] - average);
            if (difference < minDifference)
            {
                minDifference = difference;
                closest = numbers[i];
            }
        }

        Console.WriteLine("Среднее арифметическое: " + average);
        Console.WriteLine("Число, ближайшее к среднему: " + closest);
    }
}
