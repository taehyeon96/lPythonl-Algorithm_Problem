def solution(brown, yellow):
    answer = []
    
    x = brown // 2
    cnt = 0
    
    for i in range(1, x+1):
        if (x - 2) * cnt == yellow:
            return [x, cnt + 2]
        else:
            cnt += 1
            x -= 1