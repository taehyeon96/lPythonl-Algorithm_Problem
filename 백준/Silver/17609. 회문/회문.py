'''
# 잘못 접근한 코드
def is_palindrome(a):
    if a == a[::-1]:        return True
    else:        return False

for _ in range(int(input())):
    text = input()
    is_not = True
    
    if is_palindrome(text):
        print(0)
        continue
    
    leng = len(text)
    for i in range(leng):
        if is_palindrome(text[:i]+text[i+1:]):
            print(1)
            is_not = False
            break
            
    if is_not:            
        print(2)
        is_not = True
'''

import sys

def secondCheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def firstCheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = secondCheck(word,left+1,right)
            check2 = secondCheck(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    word = sys.stdin.readline().rstrip("\n")
    left=0
    right=len(word)-1
    ans = firstCheck(word,left,right)
    print(ans)