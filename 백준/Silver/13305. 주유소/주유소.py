n = int(input())
road = list(map(int, input().split()))      # range(n-1)
station = list(map(int, input().split()))    # range(n)

ans = road[0] * station[0]  # 무조건 계산되는 값 (for문은 비교를 위해 1부터 시작할 것임)
min_cost_idx = 0

for i in range(1, n-1):
    # 앞에 min값보다 작다면
    if station[min_cost_idx] > station[i]:        
        min_cost_idx = i
    ans += (road[i] * station[min_cost_idx])
        
print(ans)