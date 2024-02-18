
# 3주차 알고리즘 문제
travelCourse = input('여행지크기입력: ')
travelCourse = int(travelCourse)

travelPlan = input('여행계획입력: ')
travelPlan = travelPlan.split(' ')

destination_x = 1
destination_y = 1

for i in range(len(travelPlan)):
  tmp_x = destination_x
  tmp_y = destination_y
  if travelPlan[i] == 'L' and tmp_x-1 > 0:
    tmp_x = tmp_x-1
  if travelPlan[i] == 'R' and tmp_x-1 <= travelCourse:
    tmp_x = tmp_x+1
  if travelPlan[i] == 'U' and tmp_y-1 > 0:
    tmp_y = tmp_y-1
  if travelPlan[i] == 'D' and tmp_x-1 <= travelCourse:
    tmp_y = tmp_y+1
  destination_x = tmp_x
  destination_y = tmp_y
  
print(str(destination_x)+' '+str(destination_y))