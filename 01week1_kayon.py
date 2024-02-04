#1주차 알고리즘(1)
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

first_num = num_list[n-1]

second_num = num_list[n-1]

third_num = num_list[n-1]

result = 0


while True:
 for i in range(k):
        if(m==0):
            break
        result += first_num
        m -=1

        if (m == 0):
            break
        result += second_num
        m -= 1

        print(result)