arr = [int(input()) for _ in range(int(input()))]

arr.sort(reverse=True)

cnt = 0
ans = 0

for i in arr:
    cnt += 1        
    if cnt == 3:   # 하나씩 꺼내서 3번째면 PASS
        cnt = 0
    else:
        ans += i   # 하나씩 꺼내서 3번째가 아닌 수만 더해준다
print(ans)