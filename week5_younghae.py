n, m = map(int, input("학생 인원수와 가위바위보 개수를 순서대로 입력하시오").split())
train = []

#학생 인원수만큼 2차원 배열 생성
for i in range(n):
    train.append([i+1])

trun = 1
lose = []
#가위바위보
while True:
    if(trun > m):
        break
    else:
        x_i, y_i = map(int, input("출석 번호를 입력하시오").split())
        for i in range(len(train)):
            for j in range(len(train)):
                if(train[i][0] == y_i):
                    lose.extend(train[i]) #패배한 배열 요소 추가
                    train[i].clear() #초기화
                    train[i].extend([0]) #값이 존재하지 않기 때문에 0 추가
                    break
                if(train[j][0] == x_i):
                    train[j].extend(lose) #패배한 배열 요소를 승자 배열에 추가
                    lose.clear() #다음 턴에서 새로운 값 추가를 위해 비우기
                    break
        trun += 1

#열차 길이 비교
longer = []
for i in train:
    if(len(longer) < len(i)):
        longer.clear() #새로 값 추가하기 위해 초기화
        longer.extend([i])
    elif(len(longer) == len(i)): #중복이 있는 경우
        longer.extend([i])

#출력
for l in longer:
    print(l[0])