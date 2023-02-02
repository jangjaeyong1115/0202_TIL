N = int(input()) # 컵의 위치를 바꾼 횟수
cups = [1,2,3] 
for _ in range(N): # N번 반복
  x, y = map(int, input().split()) # x, y 값 받기
  c1 = cups.index(x) # x의 인덱스 가져오기
  c2 = cups.index(y) # y의 인덱스 가져오기
  cups[c1], cups[c2] = cups[c2], cups[c1] # 컵 위치 바꾸기

print(cups[0]) # 공이 들어있는 컵번호 출력



