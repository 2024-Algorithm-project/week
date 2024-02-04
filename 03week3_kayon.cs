using System;

class Program
{
    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int X = int.Parse(input[1]);
        int Y = int.Parse(input[2]);

        for (int i = 1; i <= N; i++)
        {
            if (i % X != 0 && i % Y != 0)
            {
                Console.WriteLine('N');
                continue;
            }

            if (i % X == 0 && i % Y == 0)
            {
                Console.WriteLine('AB');
            }
            

            if (i % X == 0)
            {
                Console.Write('A');
            }

            if (i % Y == 0)
            {
                Console.Write('B');
            }

            Console.WriteLine();
        }
    }
}
