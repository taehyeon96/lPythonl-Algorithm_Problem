import sys

ans = []
for _ in range(int(sys.stdin.readline())):
    ans.append(list(map(int, sys.stdin.readline().split())))  
ans.sort(key = lambda x: (x[0], x[1]))

for i in ans:
    print(" ".join(map(str,i)))