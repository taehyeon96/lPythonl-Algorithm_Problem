n = int(input())
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)
ans = 0

num = n

for i in range(n):
    ans = max(ans, arr[i]*num)
    num -= 1
    
print(ans)