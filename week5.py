# 5주차 알고리즘 문제
import sys

# 데이터 입력(두번재 입력부터는 엔터로 리스트 나눔)
data = []
n = int(input("입력할 데이터 행의 수 : "))
for i in range(n):
	data.append(list(map(int,sys.stdin.readline().split())))

# 가위바위보 열차 생성 
train = []
for i in range(data[0][0]):
  train.append([i+1])

# 가위바위보 승패 판정
for i in range(1, data[0][1]+1):
  for j in range(0, len(train)):
    if data[i][0] == train[j][0]:
      train[data[i][0]-1].extend(train[data[i][1]-1])
  for k in range(0, len(train)):
    if data[i][1] == train[k][0]:
      train[k] = [0]
      break
    
# 가장 긴 열차 판별(길이 중복 포함해서)
result = [train[0][0]]
for i in range(1, len(train)):
  if len(train[result[0]-1]) == len(train[i]):
    result.append(train[i][0])
  if len(train[result[0]-1]) < len(train[i]):
    result = [train[i][0]]

# 답 출력
for re in result:
  print(re)