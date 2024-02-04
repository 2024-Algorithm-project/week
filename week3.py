# 3주차 알고리즘 문제
setInput = input()
setInput = setInput.split(' ')
setInput = list(map(int, setInput)) # 정수로 변환

xRange = []
yRange = []
for i in range(1, setInput[0]+1):
  xRange.append(i*setInput[1])
  yRange.append(i*setInput[2])

for i in range(1, setInput[0]+1):
  result = ''
  if i in xRange: 
    result+='A'
  if i in yRange:
    result+='B'
  if i not in xRange and i not in yRange:
    result+='N'
  print(result)