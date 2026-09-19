using System;

class Program
{
    static void Main()
    {
        double[] averages = new double[3];

        for (int student = 1; student <= 3; student++)
        {
            double sum = 0;
            Console.WriteLine("Оценки для студента " + student + ":");

            for (int i = 1; i <= 5; i++)
            {
                Console.Write("Оценка " + i + ": ");
                double grade = Convert.ToDouble(Console.ReadLine());
                sum = sum + grade;
            }

            averages[student - 1] = sum / 5;
        }

        Console.WriteLine();
        Console.WriteLine("Средний балл студента 1: " + averages[0]);
        Console.WriteLine("Средний балл студента 2: " + averages[1]);
        Console.WriteLine("Средний балл студента 3: " + averages[2]);
    }
}
