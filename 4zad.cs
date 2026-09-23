using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, string> phoneBook = new Dictionary<string, string>();

        while (true)
        {
            Console.WriteLine();
            Console.WriteLine("Выберите действие: добавить, поиск, показать, выход");
            string command = Console.ReadLine();

            if (command == "выход")
            {
                break;
            }
            else if (command == "добавить")
            {
                Console.Write("Введите имя: ");
                string name = Console.ReadLine();
                Console.Write("Введите номер телефона: ");
                string phone = Console.ReadLine();

                phoneBook[name] = phone;
                Console.WriteLine("Контакт добавлен.");
            }
            else if (command == "поиск")
            {
                Console.Write("Введите имя для поиска: ");
                string name = Console.ReadLine();

                if (phoneBook.ContainsKey(name))
                {
                    Console.WriteLine(name + ": " + phoneBook[name]);
                }
                else
                {
                    Console.WriteLine("Контакт не найден.");
                }
            }
            else if (command == "показать")
            {
                Console.WriteLine("Список контактов:");
                foreach (KeyValuePair<string, string> contact in phoneBook)
                {
                    Console.WriteLine(contact.Key + ": " + contact.Value);
                }
            }
            else
            {
                Console.WriteLine("Неизвестная команда.");
            }
        }

        Console.WriteLine("Программа завершена.");
    }
}
