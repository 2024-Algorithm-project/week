# 5주차 알고리즘 문제
# 맵의 세로 크기 N, 가로 크기 M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 게임 캐릭터의 현재 좌표 (x, y)와 바라보는 방향 direction을 입력받기
x, y, direction = map(int, input().split())

# 방문한 칸의 수를 셀 변수
visited = 0

# 맵 정보 입력받기
game_map = []
for _ in range(N):
    game_map.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 현재 위치 방문 처리
visited += 1
game_map[x][y] = 2

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
turn_num = 0

# 시뮬레이션 시작
while True:
    # 왼쪽으로 회전
    turn_left()
    # print(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= M:
        continue
    if ny < 0 or ny >= N:
        continue
    print('nx : ',str(nx))
    print('ny : ',str(ny))

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if game_map[nx][ny] == 0:
        x = nx
        y = ny
        visited += 1
        turn_num = 0
        game_map[x][y] = 2
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        if turn_num < 4:
            turn_num += 1
            continue
        # 네 방향 모두 갈 수 없는 경우
        if (game_map[x-1][y] == 1 and game_map[x][y-1] == 1 and game_map[x][y+1] == 1 and
                game_map[x+1][y] == 1):
            break
        # 바라보는 방향을 유지한 채로 한 칸 뒤로 가기
        else:
            check_back = 0
            # 뒤로 갈 수 있다면 이동하기
            for i in range(4):
              turn_left()
              nx = x - dx[direction]
              ny = y - dy[direction]
              if game_map[nx][ny] == 2:
                  x = nx
                  y = ny
                  continue
            # 뒤가 바다로 막혀있는 경우
            else:
                # print('exit2')
                # print('x : ',str(x))
                # print('y : ',str(y))
                # print(game_map)
                break

# 결과 출력
# print(x)
# print(y)
print(visited)

"""
2시간 넘게 붙잡고 있었어서 포기
왔던 길 되돌아 가는 부분에서 문제가 있음, 
1칸짜리 되돌아 가는건 작동 되나 
2칸이상 되돌아 가는 것은 불가능
out of range 에러 아직 해결 못함
"""