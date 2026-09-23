using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите количество студентов n: ");
        int n = Convert.ToInt32(Console.ReadLine());

        Console.Write("Введите количество предметов m: ");
        int m = Convert.ToInt32(Console.ReadLine());

        int[,] grades = new int[n, m];

        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("Оценки студента " + (i + 1) + ":");
            for (int j = 0; j < m; j++)
            {
                Console.Write("Предмет " + (j + 1) + ": ");
                grades[i, j] = Convert.ToInt32(Console.ReadLine());
            }
        }

        Console.WriteLine();
        for (int i = 0; i < n; i++)
        {
            int sum = 0;
            for (int j = 0; j < m; j++)
            {
                sum = sum + grades[i, j];
            }
            double average = (double)sum / m;
            Console.WriteLine("Средний балл студента " + (i + 1) + ": " + average);
        }
    }
}
