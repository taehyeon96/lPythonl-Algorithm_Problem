class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        s1 = s.lower()
        for i in s1:
            if i.isalpha() or i.isalnum():
                tmp.append(i)
        for i in range(1, (len(tmp)//2)+1):
            if tmp[i-1] != tmp[-i]:   # 하나라도 같지 않으면 return flase
                return False
        return True
        