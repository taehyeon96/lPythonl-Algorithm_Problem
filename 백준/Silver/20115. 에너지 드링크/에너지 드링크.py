import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort(reverse=True)

while len(arr) > 1:
    # 0번째가 제일 큰 것임, 브루트포스할수밖에 없음
    arr[0] += (arr[-1] * 0.5)
    arr.pop()
    
print(arr[0])