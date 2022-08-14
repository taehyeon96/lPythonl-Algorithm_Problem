import sys
input = sys.stdin.readline
n = int(input().strip())
arr = [input().strip() for _ in range(n)]

arr = sorted(list(set(arr)), key = lambda x:(len(x), x))
print("\n".join(map(str,arr)))