# 7주차 알고리즘 문제
'''
내가 생각하는 제외하는 방법

가정 1.
일단 적당히 내림차순으로 정렬되어 있다는것을 가정
가정 2.
필요 없는건 튀는 수(너무 값이 높거나 낮은 수)

방법
적당히 내림차순으로 주어진 배열 안에서 매우 튀는 수(너무 높은수, 너무 낮은 수)를 제외해서 내림차순으로 만든다.
'''
number = list(map(int, input()))
soldiers = list(map(int, input().split(' ')))

counter = []

def exceptTooBig(arr):
    global counter
    rtn = arr
    while True:
        maxVal = max(rtn) 
        if rtn[0] != maxVal:
           rtn.pop(rtn.index(maxVal))
           counter.append(maxVal)
        else:
            break   
    return rtn


def exceptTooSmall(arr):
    global counter
    rtn = arr
    while True:
        minVal = min(rtn) 
        if rtn[len(rtn)-1] != minVal:
            rtn.pop(rtn.index(minVal))
            counter.append(minVal)
        else:
            break   
    return rtn

def exceptNotUses(arr):
    global counter
    rtn = arr
    while len(rtn)-2:
        check = rtn[0]
        rtn.pop(0)
        while True:
            if rtn.count(check) == 0:
                check -= 1
                if check == 0 : 
                    break
                continue
            if rtn.index(check) == 0:
                break
            else:
                while range(0, rtn.index(check)):
                    counter.append(rtn[0])
                    del rtn[0]
                break
    return rtn

soldiers = exceptTooBig(soldiers)
soldiers = exceptTooSmall(soldiers)
soldiers = exceptNotUses(soldiers)

print(len(counter))