from collections import deque
import sys
input = sys.stdin.readline

# input data
n, m, k, x = map(int, input().split())
# 인접 리스트 생성!
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)                  # (중요) 방향그래프이므로 이렇게만 추가해야한다

visit = [-1]*(n+1)                      # (중요) 갈 수 없는 노드는 -1이 된다!

def bfs(x):
    que = deque()
    que.append(x)
    visit[x] += 1
    
    while que:
        x = que.popleft()
        for nx in graph[x]:
            if visit[nx] == -1:        # 연결된 노드 중 방문하지 않은 노드만
                que.append(nx)
                visit[nx] = visit[x] + 1

    if k not in visit:
        print(-1)
        return
    
    for i in range(1, n+1):
        if visit[i] == k:
            print(i)

bfs(x)