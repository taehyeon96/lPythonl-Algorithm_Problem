import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
ans = 0
for i in range(1, n):
    arr[i] += arr[i-1]

print(sum(arr))