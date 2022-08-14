# 방법 2 : bisect를 사용하고, 찾고자 하는 값의 앞에 데이터를 넣어줌
from bisect import bisect

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bisect(B, a-1))  # a보다 하나 작은 값의 인덱스를 찾아서 그 인덱스를++ 
    print(cnt)