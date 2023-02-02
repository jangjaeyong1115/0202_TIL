import sys

word = list(map(str, sys.stdin.readline().rstrip()))
list = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        list.append("".join(first + second + third))

    print(min(list))