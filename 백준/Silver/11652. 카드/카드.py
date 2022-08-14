# 호석 정답
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]

a.sort()

maximum = a[0]
maxCnt = 1        # 현재 max값을 저장 (a[0] 1번 등장 ~>초기화)
curCnt = 1        # 두 번째 값부터 등장 횟수 카운팅용

# 미리 정렬해놓고 두 번째 데이터부터 counting 시작 (-->정렬문제!!)
for i in range(1, n):    
    if a[i] == a[i-1]:
        curCnt += 1         # 같은 경우 ++
    else:
        curCnt = 1          # 값이 바뀌면 카운팅 1부터
        
    # max 체크
    if maxCnt < curCnt:
        maxCnt = curCnt;    # max값의 카운팅값
        maximum = a[i]      # max값 저장

print(maximum)