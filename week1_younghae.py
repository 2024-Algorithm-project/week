n, m, k = map(int, input().split())
data = list(map(int, input("n개의 자연수를 입력하시오").split()))

#정렬
data.sort(reverse=True)
#각각 가장 큰 수, 두번째로 큰 수
first = data[0]
second = data[1]

result = 0
while True:
     #가장 큰 수를 k만큼 더함 
    for i in range(k):
        if m == 0:
            break
        else:
            result += first
            m -= 1
    if m == 0:
        break
    else:
        result += second
        m -= 1
print(result)