from itertools import combinations
import sys
input = sys.stdin.readline

leng = int(input())
S = [list(map(int, input().split())) for _ in range(leng)]
#S = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
#S = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]
#S = [[0, 5, 4, 5, 4, 5, 4, 5], [4, 0, 5, 1, 2, 3, 4, 5], [9, 8, 0, 1, 2, 3, 1, 2], [9, 9, 9, 0, 9, 9, 9, 9], [1, 1, 1, 1, 0, 1, 1, 1], [8, 7, 6, 5, 4, 0, 3, 2], [9, 1, 9, 1, 9, 1, 0, 9], [6, 5, 4, 3, 2, 1, 9, 0]]

ans = 999999
s = [i for i in range(len(S))]

for star in combinations(s, int(len(s)/2)):
    aa = 0
    bb = 0
    # start에는 인덱스 넘버들이 있음
    link = list(set(s) - set(star))
    
    for a in list(combinations(list(star), 2)):
        aa += S[a[0]][a[1]] + S[a[1]][a[0]]
        
    for b in combinations(list(link), 2):
        bb += S[b[0]][b[1]] + S[b[1]][b[0]]
        
    ans = min(ans, abs(aa-bb))

print(ans)