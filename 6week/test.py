def turn_left(direction):
    return (direction - 1) % 4

# 입력 받기
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문한 위치 기록을 위한 맵 생성
visited = [[0] * m for _ in range(n)]
visited[x][y] = "x"  # 처음 위치 방문 처리

# 전체 맵 정보 입력 받기
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시뮬레이션 시작
count = 1  # 처음 위치를 카운트
turn_time = 0
while True:
    # 왼쪽으로 회전
    direction = turn_left(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == "x" and game_map[nx][ny] == 0:
        visited[nx][ny] = "x"
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면 이동하기
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

# 결과 출력
print(count)
