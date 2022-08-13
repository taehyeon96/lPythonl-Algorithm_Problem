import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().split()) for _ in range(n)]

for i in range(n):
    for j in range(1, 4):
        arr[i][j] = int(arr[i][j])

arr.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])