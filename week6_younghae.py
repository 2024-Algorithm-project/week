N, M = map(int, input("세로 크기와 가로 크기를 순서대로 입력하시오").split())
A, B, d = map(int, input("캐릭터의 좌표와 바라보는 방향을 입력하시오").split())

#게임 맵 생성
game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visit = 1 #처음 위치 선언
trun = 0 #회전 횟수

while True:
    #왼쪽으로 90도 회전
    d -= 1
    if d == -1: 
        d = 3
    x = A + dx[d]
    y = B + dy[d]
    if game_map[x][y] == 0: #육지인 경우
        A, B = x, y
        game_map[x][y] = 2
        visit += 1
        trun = 0
    else:
        trun += 1
    if trun == 4: #네 방향 모두 이미 가 봤거나 바다인 경우
        #뒤로 한 칸 이동
        d -= 2
        if d < 0:
            d += 4
        x = A - dx[d]
        y = B - dy[d]
        if game_map[x][y] == 1: #바다인 경우 멈춤
            break
        else:
            trun = 0

#방문한 칸 수 출력
print(visit)