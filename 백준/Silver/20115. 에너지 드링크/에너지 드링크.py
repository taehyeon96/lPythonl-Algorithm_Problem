import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
for i in range(n-1):
    arr[n-1] += (arr[i] * 0.5) # n번째가 제일 큰 녀석임
    
print(arr[-1])