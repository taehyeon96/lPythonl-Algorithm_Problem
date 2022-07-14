from itertools import permutations

def is_prime_number(x):
    # 소수는 1보다 큰 자연수 중 1과 자신을 약수로 갖는 수
    if x == 1 or x == 0:                    
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    arr = list(map(int,numbers))
    leng = len(numbers)
    
    for j in range(1, leng+1):
        for i in permutations(arr, j):
            candidate = int("".join(map(str,i)))
            if is_prime_number(candidate):
                answer.append(candidate)
                
    return len(set(answer))