from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
S = []
B = []

for _ in range(n):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)
    
answer = 1000000000    
for i in range(1, n+1):   # 최소 하나이상 선택(만약 에러라면 0부터 n+1까지)    
    for cases in combinations(list(range(n)), i):   # (중요) 배열의 인덱스로 combination하는 방법     
        s = 1
        b = 0    
        
        for j in cases:
            s *= S[j]
            b += B[j]
            
        answer = min(answer, abs(s-b))

print(answer)