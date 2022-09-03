from collections import deque
from itertools import combinations
import copy                         # 깊은복사 : copy.deepcopy()
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
main_graph = [list(map(int, input().split())) for _ in range(n)]
graph = copy.deepcopy(main_graph)
q = []
zero = []
answer = []

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# bfs 구현
def bfs(que, graph):    
    sub_num = 0            # 0의 개수 체크
    # 바이러스 이동
    while que:
        y, x = map(int, que.popleft())        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny and ny<n and 0<=nx and nx<m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                que.append((ny, nx))
                
    # 해당 bfs가 끝났으면 0의 개수 체크
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                sub_num += 1
                
    return sub_num

# 바이러스 위치를 저장하자(bfs 시작용 위치 저장)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i,j))      
        elif graph[i][j] == 0:
            zero.append((i,j))
            
# 브루트포스로 0인 곳만 3개의 벽을 세워보자 (= walls[0] [1] [2]가 벽)
for walls in combinations(zero, 3):        # 중복필요없어서 combinations
    # (중요) 그래프 원상복구 -> 깊은복사!
    graph = copy.deepcopy(main_graph)
    que = deque(q)
    
    y1, x1 = map(int, walls[0])
    y2, x2 = map(int, walls[1])
    y3, x3 = map(int, walls[2])
    
    graph[y1][x1] = 1
    graph[y2][x2] = 1
    graph[y3][x3] = 1
    
    # 이제 bfs를 돌려 -> graph를 바이러스로 물들인다
    # bfs 끝나면 bfs 안에서 0이 존재하는지 브루트포스로 개수 센다 -> return 개수 -> ans.append
    answer.append(bfs(copy.deepcopy(que), graph))
    
print(max(answer))