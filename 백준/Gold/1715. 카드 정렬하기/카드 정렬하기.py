import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

heapq.heapify(arr)   # 리스트릴 힙으로 변환(-> pop 시 min값 출력)

ans = 0

# 힙에 데이터 2개 이상 있어야 돌릴 수 있다.
while len(arr)-1 != 0:
    a = heapq.heappop(arr)   # min값 두 개를 추출
    b = heapq.heappop(arr)
    
    ans += a+b               # min값 두 개 더해주고
    heapq.heappush(arr, a+b) # 힙에 더한값 새롭게 넣는다 (= 기존 값과 비교가 필요하므로)
    
print(ans)