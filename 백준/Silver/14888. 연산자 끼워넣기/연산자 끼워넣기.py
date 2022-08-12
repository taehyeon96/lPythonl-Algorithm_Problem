'''
제출용
'''
from itertools import permutations
import sys
input = sys.stdin.readline

leng = int(input())
arr = list(map(int, input().split()))
tmp = list(map(int, input().split()))

operator = []     # max length = leng - 1
total_operator = []

for i in range(4):
    if tmp[i] > 0:
        for _ in range(1, tmp[i]+1):
            if i == 0:
                operator.append('+')
            elif i == 1:
                operator.append('-')
            elif i == 2:
                operator.append('*')
            elif i == 3:
                operator.append('//')

for i in permutations(operator, leng-1):    # 모든 경우의 수 다 해봐야함
    total_operator.append(list(i))    
    
answers = []

for op in range(len(total_operator)):
    ans = arr[0]
    for i in range(1, leng):
        if total_operator[op][i-1] == '+':
            ans += arr[i]
        elif total_operator[op][i-1] == '-':
            ans -= arr[i]
        elif total_operator[op][i-1] == '*':
            ans *= arr[i]
        elif total_operator[op][i-1] == '//':
            ans = int(ans / arr[i])    # 소수일 경우, 소수점 뒤에 내용은 다 없애줘야함            
    answers.append(ans)
        
print(max(answers))
print(min(answers))