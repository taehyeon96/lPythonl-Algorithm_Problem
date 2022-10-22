# '''
# ### 문제 : SWEA 1949
# * [모의 SW 역량테스트] 등산로 조성
# * 링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98+SW+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1
#
# ### 메모
#
# * 등산로 부지는 n * n
#   - 최대한 긴 등산로를 만든다
#
# * 등산로 만드는 규칙
#   - 등산로는 가장 높은 봉우리에서 시작
#   - 높은 지형 -> 낮은 지형으로
#     - **동일 높이는 패스, 반드시 본인보다 낮은 지형으로만**
#   - 가로 또는 세로 방향으로 연결되어야함
#   - 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있음
#
# * n * n 지도와 최대 공사 가능 깊이 k가 주어지면, 만들 수 있는 가장 긴 등산로를 찾고 길이 출력
#   - DFS, BFS네
#
# * 예제 그림에서 **9가 제일 높은 봉우리, 총 3개임**
# * <중요> 이 문제의 가장 큰 변수는 "K"만큼 깎을 수 있다 (일반 DFS랑 다른점)
#   - k=1 일 떄, 한번 깎아줄 수 있잖아
#     - [4,3]의 9를 8로 깎아주면 등산로가 6이될수있음 (링크타고들어가서 봐봐)
# ---
# ### 고려사항
# * 시작 좌표가 여러 개일 수 있다(고점이 많음)
#   - 끝나는 지점에서 몇 번 왔는지 체크
#
# * 등산로를 한 번 허용하는 길이만큼 줄일 때 줄인것을 반영하되, 다른 등산로에게 영향을 주면 안됨!!
#   - 즉, 등산로 높이를 깎을 경우 temp변수로 원상복구시킴
#
# * deepcopy를 사용하면 오래 걸려서 visited를 바꿔주는 식으로 진행
# '''

direction = [(0,1), (0,-1), (1,0), (-1,0)]

def DFS(y, x, cnt, K_used):
    # cnt :
    # K_used : 깎아봤니 안깎아봤니 Flag (True, False)
    global max_length
    visited[y][x] = 1

    for dt in range(4):
        ny = y + direction[dt][0]
        nx = x + direction[dt][1]

        if ny < 0 or N <= ny or nx < 0 or N <= nx or visited[ny][nx] == 1:
            continue

        # 이전 높이보다 낮은 경우 => 방문처리 후 다음 위치에서 DFS(+1) => 돌아와서 방문 다시 0으로
        if map_info[ny][nx] < map_info[y][x]:
            visited[ny][nx] = 1
            DFS(ny, nx, cnt+1, K_used)
            visited[ny][nx] = 0
        # -------------------- 여기까진 기존 DFS랑 똑같음 --------------------
        # (중요_문제의 핵심 부분) 아직 안깎아봤고, 다음 위치 값에서 K번 깎았을 때 현재보다 작아질 수 있으면
        elif [ny][nx] - K < map_info[y][x] and K_used == False:
            # 백업해두고 깎아보자
            temp = map_info[ny][nx]
            map_info[ny][nx] = map_info[y][x] - 1   # 근데왜 1번만깎지??
            K_used = True
            visited[ny][nx] = 1

            DFS(ny, nx, cnt+1, K_used)

            # 돌아와서 다시 원상복구
            map_info[ny][nx] = temp
            K_used = False
            visited[ny][nx] = 0

    else:
        # DFS로 걸어온 길이의 max값을 계속해서 갱신
        max_length = max(max_length, cnt)
        # if max_length < cnt:
        #     max_length = cnt


T = int(input())
for tc in range(1, T+1):
    # 테케 별 실행
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]

    # (중요) nxn 배열 가장 큰 값 좌표 찾기 (start에 저장)
    start = []
    max_peak = 0
    for i in range(N):
        for j in range(N):
            # 내 max_peak보다 작은 애들은 스킵
            if map_info[i][j] < max_peak:
                continue

            # 만약 max_peak이 5인줄알고 5를 계속 넣다가, 8이 max인줄 알았으면 초기화 후 8이상을 넣어줌
            if map_info[i][j] > max_peak:
                start = []
            # max_peak보다 같으면 계속 넣어주고, 크면 초기화 후 계속 넣어주면 됨
            max_peak = map_info[i][j]        # 이때, max_peak은 계속 갱신
            start.append((i, j))

    # DFS 수행하자
    max_length = 0                             # <-- 함수안에서 global로 끌어옴
    for i in range(len(start)):
        sr, sc = start[i][0], start[i][1]      # start는 리스트고, i번째 [0]= i, i번째 [1]=j
        visited = [[0] * N for _ in range(N)]  # for문 돌 때마다 새로 갱신할라고

        DFS(sr, sc, 1, False)

    print(f'#{tc} {max_length}')


##################
# delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
# def DFS(r, c, cnt, K_used):
#     global max_length
#     visited[r][c] = 1
#     for dt in range(4):
#         nr = r + delta[dt][0]
#         nc = c + delta[dt][1]
#         if 0 > nr or nr >= N or 0 > nc or nc >= N or visited[nr][nc] == 1: continue
#         # 이전 등산로보다 낮을 경우
#         if map_info[nr][nc] < map_info[r][c]:
#             visited[nr][nc] = 1
#             DFS(nr, nc, cnt + 1, K_used)
#             visited[nr][nc] = 0
#         # 허용 깊이까지 깎을 수 있고, 아직 깎아본적 없을때
#         elif map_info[nr][nc] - K < map_info[r][c] and K_used == 0:
#             temp = map_info[nr][nc]
#             map_info[nr][nc] = map_info[r][c] - 1
#             K_used = 1
#             visited[nr][nc] = 1
#             DFS(nr, nc, cnt + 1, K_used)
#             K_used = 0
#             visited[nr][nc] = 0
#             map_info[nr][nc] = temp
#     else:
#         if max_length < cnt:
#             max_length = cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     map_info = []
#     for i in range(N):
#         map_info.append(list(map(int, input().split())))
#
#
#     # 가장 높은 봉우리 찾고 좌표 저장
#     start = []
#     max_peak = 0
#     for i in range(N):
#         for j in range(N):
#             if map_info[i][j] < max_peak: continue
#             if map_info[i][j] > max_peak:
#                 start = []
#             max_peak = map_info[i][j]
#             start.append((i, j))
#
#     max_length = 0
#     for i in range(len(start)):
#         sr, sc = start[i][0], start[i][1]
#         visited = [[0] * N for _ in range(N)]
#         DFS(sr, sc, 1, 0)
#     print(f'#{tc} {max_length}')