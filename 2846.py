N = int(input())
height = list(map(int,input().split()))

temp = 0
list = []

for i in range(1,N):
    if height[i] > height[i-1]:
        temp += height[i]-height[i-1]
        if i == N-1:
            list.append(temp)
        else:
            list.append(temp)
            temp = 0

print(max(list))