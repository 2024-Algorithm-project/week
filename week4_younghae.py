n, m = map(int, input().split())

i = 1
arr = []
while True:
    if(i == n):
        break
    else:
        distance = int(input())
        if(i<n-1):
            arr.append(distance)
        i += 1

result = 0
for a in arr:
    result += a

print(result)