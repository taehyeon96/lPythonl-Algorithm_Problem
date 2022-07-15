from collections import deque
import sys
input = sys.stdin.readline

def bfs(check, graph, start,n):
    child = [[] for _ in range(n+1)]
    
    que = deque([start])
    check[start] = True
    
    while que:
        v = que.popleft()
        
        for i in graph[v]:
            if not check[i]:
                que.append(i)
                child[v].append(i)   # 부모에 대한 자식 넣기
                check[i] = True
                
    return child
    
n = int(input())
graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

# 그래프 생성
for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 부모에 대한 자식을 찾았음
child = bfs(check, graph, 1,n)       

# 역으로 바꾸기 (자식의 부모 인덱스 반환)
parent = [[] for _ in range(n+1)]

for i in range(1, len(child)):
    for j in child[i]:
        parent[j].append(i)
        
# 출력
for i in range(len(parent)):
    if parent[i]:
        print(*list(map(int,parent[i])))