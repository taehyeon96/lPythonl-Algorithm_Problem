from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
sorted_num = Counter(arr)
a = sorted_num.most_common(1)
print(a[0][0])