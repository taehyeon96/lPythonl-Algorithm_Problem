n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
if n <= 2:
    print(arr[0])
else:
    if n % 2 == 0:  # 짝수        
        print(arr[(n//2)-1])
    else:
        print(arr[n//2])