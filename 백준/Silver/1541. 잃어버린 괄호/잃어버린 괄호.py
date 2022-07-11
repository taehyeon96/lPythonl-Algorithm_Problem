a = input().split('-')          # '-'로 split()해서 큼직큼직 잘라줌 = 괄호 작업!!!
num = []

for i in a:
    cnt = 0
    s = i.split('+')           # (  )로 묶인 것에 대해서    
    for j in s:               # sum()을 해줌
        cnt += int(j)
        
    num.append(cnt)            # sum()한 각 숫자를 리스트에 저장
    
n = num[0]                     # sum()한 것 중 첫 번째 값에서 나머지 전부 빼줄거
for i in range(1, len(num)):
    n -= num[i]
    
print(n)