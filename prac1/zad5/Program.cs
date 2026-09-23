//Борисова Диана ИСИП23/1

using System;

class Program
{
    static void Main()
    {
        int[,] first = new int[3, 3];
        int[,] second = new int[3, 3];
        Console.WriteLine("Введите числа первой матрицы 3x3 через пробел, по строкам:");
        for (int i = 0; i < 3; i++)
        {
            string[] line = Console.ReadLine().Split(' ');
            for (int j = 0; j < 3; j++)
            {
                first[i, j] = Convert.ToInt32(line[j]);
            }
        }
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                second[j, i] = first[i, j];
            }
        }

        Console.WriteLine("Было:");
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(first[i, j] + " ");
            }
            Console.WriteLine();
        }

        Console.WriteLine("Стало:");
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write(second[i, j] + " ");
            }
            Console.WriteLine();
        }
    }
}
