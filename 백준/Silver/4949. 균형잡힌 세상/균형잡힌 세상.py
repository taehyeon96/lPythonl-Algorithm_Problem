'''
()와 []
같은 것과만 짝을 이루어야 함, 1:1매칭만 가능

결론 : 균형잡혔는지 아닌지만 판별 yes no
    -> [(]) 이거도 no                   ~> 숫자 +-할 경우 이거 못잡음
    -> 아무겂도 없는 '   ' 는 yes
    
각 줄은 마침표'.'로 끝남
입력 종료조건으로 '.'가 들어옴

[]랑 ()같이 관리하는 스택 만들어서 
[,(일경우 append
],)일경우 스택[-1]이 [냐(냐 같지 않으면 바로 return "no" // 같으면 pop()
'''
import sys
def solution(text):
    stack = []
    
    for i in text:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack: return "no"     # 처음이 닫는괄호인 경우
            
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                return "no"
            
        elif i == ']':
            if not stack: return "no"     # 처음이 닫는괄호인 경우
            
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                return "no"
            
    if not stack:
        return "yes"
    else:
        return "no"

text = sys.stdin.readline()
#text = input()
while text != '.':    
    print(solution(text))
    text = input()