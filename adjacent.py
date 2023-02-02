from pprint import pprint

n = 7
m = 7
graph = [[] for _ in range(n)]

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

pprint(graph)