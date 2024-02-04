using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace _2024Algorithm
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //사용자가 정수 n을 입력
            int num = int.Parse(Console.ReadLine());
            //공백으로 구분된 문자열들을 입력받아 배열에 저장
            string[] list = Console.ReadLine().Split();

            //초기 좌표
            int[] now = { 1, 1 };

            foreach (var i in list)
            {
                if (i == "L")
                {
                    //왼쪽으로 이동 , y 좌표 now[1]이 1보다 큰 경우에만 왼쪽으로 한 칸 이동
                    if (now[1] > 1)
                        now[1]--;
                }
                else if (i == "R")
                {
                    //오른쪽으로 이동, y 좌표 now[1]이 n보다 작은 경우에만 오른쪽으로 한 칸 이동
                    if (now[1] < num)
                        now[1]++;
                }
                else if (i == "U")
                {
                    //위로 이동, x 좌표 now[0]이 1보다 큰 경우에만 위로 한 칸 이동
                    if (now[0] > 1)
                        now[0]--;
                }
                else if (i == "D")
                {
                    //아래로 이동, x 좌표 now[0]이 n보다 작은 경우에만 아래로 한 칸 이동
                    if (now[0] < num)
                        now[0]++;
                }
            }
            Console.WriteLine($"{now[0]} {now[1]}");
        }
    }
} 
