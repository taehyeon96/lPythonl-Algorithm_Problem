import sys
arr = sys.stdin.readline()
leng = len(arr)

num = '-1'
plus = 0
minus = 0

for i in range(leng-1, -1, -1):
    if arr[i].isdigit():
        if num == '-1':                 # 숫자 처음인 경우
            num = str(arr[i])
        else:                           # 처음이 아닌 경우
            num = str(arr[i]) + num
            
    else:
        if arr[i] == '+':
            plus += int(num)
            num = '-1'                  # 숫자 처음으로
        elif arr[i] == '-':
            minus += int(num) + plus   # 현재 숫자와 히스토리(plus)를 더해줌
            plus = 0
            num = '-1'                  # 숫자 처음으로

print(plus + int(num)-minus)