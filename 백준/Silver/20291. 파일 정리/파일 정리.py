from collections import Counter

arr = [input() for i in range(int(input()))]

ans = []
for i in arr:
    _, key = i.split('.')
    ans.append(key)
    
c = sorted(dict(Counter(ans)).items())
for i in c:
    print(i[0], i[1])