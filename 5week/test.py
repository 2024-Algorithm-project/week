import random

# N과 M값 받음
N, M = map(int, input().split())
train = []

# 초반 열차 설정하기
while True:
    # N명에 맞게 2차원 배열 생성
    for _ in range(N):
        train.append([])

    # 출석번호 2차원 배열에 저장
    for i in range(len(train)):
        train[i].append(i+1)
    break

print(train)
print("한 학급에 {}명의 학생이 있습니다.".format(N))
print("게임 중에 총 {}번의 가위바위보가 진행되었습니다.".format(M))

game = ["가위", "바위", "보"]
n = 1
arr = []

while M != 0:

    # 출석번호 입력하기
    x_i, y_i = map(int, input().split())

    # 입력 출석번호가 선두인지 체크
    found = False
    for i in train:
        if x_i == i[0]:
            for i in train:
                if y_i == i[0]:
                    found = True
                    break
    # 선두일 경우
    if found:
        result_1 = random.choice(game)
        result_2 = random.choice(game)

        # 무승부인 경우
        if result_1 == result_2 :
            print("무승부이므로 다시 진행합니다.")
        # x_i가 이긴 경우
        elif (result_1 == "가위" and result_2 == "보") or (result_1 == "바위" and result_2 == "가위") or (result_1 == "보" and result_2 == "바위"):
            print(n, "번째 가위바위보에서는 출석 번호 {}번인 학생이 출석 번호 {}인 학생을 이겼습니다.".format(x_i, y_i))
            winner = x_i
            loser = y_i
            M -= 1
            print("남은 기회: ",M)
            n += 1

            for i in range(len(train)):
                for j in range(len(train)):
                    if(train[i][0] == loser):
                        arr.extend(train[i])
                        train[i].clear()
                        train[i].extend([0])
                        break
                    if(train[i][0] == winner):
                        train[i].extend(arr)
                        arr = []
                        break
                    else:
                        continue
        # y_i가 이긴 경우
        else:
            print(n, "번째 가위바위보에서는 출석 번호 {}번인 학생이 출석 번호 {}인 학생을 이겼습니다.".format(y_i, x_i))
            winner = y_i
            loser = x_i
            M -= 1
            print("남은 기회: ",M)
            n += 1

            for i in range(len(train)):
                for j in range(len(train)):
                    if(train[i][0] == loser):
                        arr.extend(train[i])
                        train[i].clear()
                        train[i].extend([0])
                        break
                    if(train[i][0] == winner):
                        train[i].extend(arr)
                        arr.clear()
                        break
                    else:
                        continue

    # 선두가 아닐경우
    else:
        print("선두가 아닙니다.")

longest_list = []
# 최종 열차 길이재기
for i in train:
    if len(i) > len(longest_list) and i[0]!=0:
        longest_list = i

print(longest_list[0],"번 학생이 최종 우승하였습니다.")