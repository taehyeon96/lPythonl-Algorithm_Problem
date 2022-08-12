from itertools import combinations
import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
for j in range(1, len(arr)+1):
    for i in combinations(arr, j):
        if sum(i) == s:
            ans += 1
print(ans)