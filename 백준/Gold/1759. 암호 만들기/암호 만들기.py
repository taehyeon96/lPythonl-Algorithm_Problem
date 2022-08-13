from itertools import permutations, combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
answer = []

for candidate in combinations(arr, l):
    is_vowels = False
    is_consonants = 0
    
    for i in candidate:
        if i in vowels:
            is_vowels = True
        else:
            is_consonants += 1
            
    if is_vowels == True and is_consonants >= 2:
        answer.append("".join(map(str,candidate)))
        
print("\n".join(answer))