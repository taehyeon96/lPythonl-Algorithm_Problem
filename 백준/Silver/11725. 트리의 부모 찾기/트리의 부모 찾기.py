import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
par = [-1]*(n+1)            # 부모를 저장하는 자식 배열

# 그래프 생성 - 나와 동일
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS로 
def dfs(n):
    for i in tree[n]:       # 현 상태(=부모)의 자식들 꺼내서
        if par[i] == -1:    # 자식을 방문 안했으면
            par[i] = n      # 자식을 방문처리(= 부모 넣어준다)
            dfs(i)          # 자식의 부모찾기 수행
            
dfs(1)
for i in range(2,n+1):
    print(par[i])
    
####################################################
from collections import deque

# def bfs(check, graph, start,n):
#     child = [[] for _ in range(n+1)]
    
#     que = deque([start])
#     check[start] = True
    
#     while que:
#         v = que.popleft()
        
#         for i in graph[v]:
#             if not check[i]:
#                 que.append(i)
#                 child[v].append(i)   # 부모에 대한 자식 넣기
#                 check[i] = True
                
#     return child
    
# n = int(input())
# graph = [[] for _ in range(n+1)]
# check = [False] * (n+1)

# # 그래프 생성
# for _ in range(n-1):
#     a, b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# # 부모에 대한 자식을 찾았음
# child = bfs(check, graph, 1,n)       

# # 역으로 바꾸기 (자식의 부모 인덱스 반환)
# parent = [[] for _ in range(n+1)]

# for i in range(1, len(child)):
#     for j in child[i]:
#         parent[j].append(i)
        
# # 출력
# for i in range(len(parent)):
#     if parent[i]:
#         print(int(str(parent[i])[1:2]))