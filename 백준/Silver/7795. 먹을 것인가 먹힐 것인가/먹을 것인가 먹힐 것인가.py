# 방법 3 : bisect_left를 사용해서, 찾고자 하는 값의 lower_bound를 검색
from bisect import bisect_left

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bisect_left(B, a))  # a보다 하나 작은 값의 인덱스를 찾아서 그 인덱스를++ 
    print(cnt)