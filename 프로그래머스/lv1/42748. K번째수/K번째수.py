def solution(array, commands):
    answer = []
    
    for cc in commands:
        i, j, k = cc
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    
    return answer