n, x, y = map(int, input().split())

i = 1
while True:
    if(i == n+1):
        break
    if(i % x == 0):
        print("A")
        i += 1
    elif(i % y == 0):
        print("B")
        i += 1
    elif(i % x == 0 and i % y == 0):
        print("AB")
        i += 1
    else:
        print("N")
        i += 1

#출력은 for문 돌리면 될듯
#y의 배수번째 응모자라는데 왜 3, 6에서 B가 나오는건가여? 사실 Y는 3인가여?