n = int(input())
move = input().split()

#초기값
x,y = 1,1

for i in move:
    if y != 1 and i == 'L':
        y -= 1
    elif y != n and i == 'R':
        y += 1
    elif x != 1 and i == 'U':
        x -= 1
    elif x != n and i == 'D':
        x += 1

print(x,y)