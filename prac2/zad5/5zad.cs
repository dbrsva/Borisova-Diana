using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, int> fruits = new Dictionary<string, int>();

        while (true)
        {
            Console.Write("Введите название фрукта (или 'выход' для остановки): ");
            string fruit = Console.ReadLine();

            if (fruit == "выход")
            {
                break;
            }

            if (fruits.ContainsKey(fruit))
            {
                fruits[fruit] = fruits[fruit] + 1;
            }
            else
            {
                fruits[fruit] = 1;
            }

            Console.WriteLine(fruit + ": " + fruits[fruit]);
        }

        Console.WriteLine();
        Console.WriteLine("Итоговый словарь:");
        foreach (KeyValuePair<string, int> item in fruits)
        {
            Console.WriteLine(item.Key + ": " + item.Value);
        }
    }
}
