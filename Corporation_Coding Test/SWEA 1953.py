'''
### SWEA 1953
* [모의 SW 역량테스트] 탈주범 검거
* 링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98+SW+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1

### 메모

* 터널끼리 연결된 경우 이동 가능
  - 탈주범이 있을 수 있는 위치의 개수를 계산해야함

* 탈주범은 시간당 1의 거리 움직일 수 있음
  - 즉 iter 1당 1칸 이동인듯
  - 그리고 탈주범은 현재칸에서 이동을 할수도, 안할수도 있음

* 지하 터널은 총 7종류의 터널 구조물로 구성 (이동가능방향)

* n * m 행렬

* 시작점이 주어지고 (예제에선 붉은 색 (r,c) = (2,1) ~> 벽 끝에서 시작이 아님!)
  - 경과된 시간이 주어졌을 때
  - 탈주범이 위치할 수 있는 **장소의 개수** 계산 (시작점인 맨홀 포함)
    - 이거 엄청 쉬운거아님? BFS아니냐?
    - visit[][] ++ 할필요도 없고 걍 yes or no만 체크하면 되는디?
  - 관건은 터널 구조물에 따른 이동위치 잘 고려해야함

---
### 핵심 고려사항

* BFS로 풀면 간단하긴 한데 (deque도 사용하자!)
  - **연결 상태**를 확인하는 과정을 제대로 생각해야한다!!!
  - ex) 파이프 타고 오른쪽으로 갈 수 있어서 갔는데
    - **+ |**  이런 모양이면 오른쪽 녀석은 ++하면 안된다!!!

  - 파이프의 다음 위치로 이동시킬 direction(x, y)에 각각 **'-'**를 붙이면 된다 (이 경우에만 ++)
    - ㄱ 같은 경우 ((0, -1), (1, 0))로 이동하자나
      - ㄱ으로 올 수 있는 경우 ((0, 1), (-1, 0)) 에서 옴..!!!!!!!!!!!
      - 즉, ㄱ을 거울로 위아래양옆으로 다 뒤집는다고 생각해

* graph의 이동과 파이프를 타고 이동하는 것을 잘 구분해야한다
  - 방법은 두 가지가 있음
  - 1) 기존에 알던 방식으로 graph이동 만들고
    파이프에 graph이동 인덱스를 연동시켜주는 것
```python
way = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌, 상, 우, 하
pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [1, 2], [3, 2], [3, 0], [1, 0]]
```
  - 2) 딕셔너리로 지정해버리는 방법
```python
tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}



```


---

'''

from collections import deque

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}

t = int(input())
for test in range(1,t+1):
    n, m, r, c, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    q = deque([(r, c)])
    visited[r][c] = 1
    cnt = 1

    while q:
        a, b = q.popleft()
        for dx, dy in tunnel[maps[a][b]]:
            nx = dx+a
            ny = dy+b
            if not 0<=nx<n or not 0<=ny<m :
                continue
            if (-dx, -dy) in tunnel[maps[nx][ny]]:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[a][b] + 1
                    q += [(nx, ny)]
                    if visited[nx][ny] <=l :
                        cnt += 1

    print('#{} {}'.format(test, cnt))
