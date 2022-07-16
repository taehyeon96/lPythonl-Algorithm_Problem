from collections import Counter

def solution(nums):
    answer = []
    
    n = len(nums)
    r = n//2
    
    cnt = dict(Counter(nums))
    return min(r, len(cnt))