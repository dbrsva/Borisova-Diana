using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int>();

        while (true)
        {
            Console.Write("Введите число: ");
            int number = Convert.ToInt32(Console.ReadLine());

            if (numbers.Contains(number))
            {
                Console.WriteLine("Число " + number + " уже было введено. Остановка.");
                break;
            }

            numbers.Add(number);
        }

        Console.WriteLine("Массив чисел:");
        foreach (int number in numbers)
        {
            Console.Write(number + " ");
        }
        Console.WriteLine();
    }
}
