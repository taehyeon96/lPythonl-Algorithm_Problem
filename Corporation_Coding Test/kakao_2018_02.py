'''
# 카카오 2018 공채 코테 2번 : 다트 게임
* 링크 : https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
* 난이도 : 하

### 메모
* 다트게임을 하자

다트판에 **3번**의 다트를 던져 합계로 실력을 겨룸

점수계산 로직을 짜야함
1. 인당 총 3번 기회

2. 각 기회에서 얻을 수 있는 점수 0 ~ 10
* (주의) 10점이 포함되어있음 <-- 이거땜에 내가 split() 구현을 못함

3. 보너스 제곱 영역이 존재
* 점수마다 반드시 하나씩 존재 (하나씩만!)
* Single(S) : 점수의 1제곱 (pow(점수, 1))
* Double(D) : 점수의 2제곱 (pow(점수, 2))
* Triple(T) : 점수의 3제곱 (pow(점수, 3))

4. 상 옵션이 존재
* 점수마다 둘 중 하나만 존재하거나 아얘 없을수도 있다. <====(중요)
  - 아얘 공란임 -> " " 도 아니고 "" 인거임 (없음!)
* 스타상(*) : 해당 점수와 바로 전에 얻은 점수를 각각 2배로
* 아차상(#) : 해당 점수만 마이너스로 바꿈

5. 스타상(*) 특징
* 첫 번째 기회에서 발생했을 경우
  - 첫 번째 스타상만 2배
* 다른 스타상(*) 효과에 중첩 가능
  - 중첩되면 점수가 총 4배가 됨
* 아차상(#)과도 중첩 가능
  - 이 경우, 중첩된 아차상 점수는 -2배

---
### 입출력
* 입력 : "점수 | 보너스 | [옵션]"으로 이루어진 문자열 3세트

* 출력 : 계산해서 점수 출력

---
### 알고리즘 및 방법
* split()함수를 쓰면 쉬울거같은딩
  - 문제점 : 상 옵션이 없을 수도 있다는점!!
    - 0도 아니고 " "도 아니고 걍 ""임 없음 ~> 뭘 기준으로 split()할까
  - 숫자는 반드시 있으니까 숫자로 쪼갤까

* isalpha(), isdigit() => isalnum() 알넘!!!
'''

dart = input()

def sol(dart):
    spliter = []
    split_sub = []
    flag = False

    for i in dart:
        print(i, spliter, split_sub)
        if flag == True:
            if i.isalnum():
                spliter.append(split_sub)
                split_sub = []
                split_sub.append(i)
            else:
                split_sub.append(i)
                spliter.append(split_sub)
                split_sub = []
            flag = False

        else:
            if i.isdigit():
                split_sub.append(i)
            elif i.isalpha():
                split_sub.append(i)
                flag = True

    print(i, spliter, split_sub)
    print(spliter)

print(sol(dart))



# 방법 1 : 일반적인 풀이법
dart = input()
def sol1(dart):
    ans = []
    # 10점인 경우를 위해 0이오는 경우를 체크해야함 (참고로 enum()에 1을주면 인덱스가 1부터 시작)
    for idx, i in enumerate(dart, 0):
        if i == 'S':
            # ans에 ^1 을 해주는데, ans에 append()가 이미 되어있을테니 [-1]에 ^1를 수행 (중요)
            ans[-1] **= 1
        elif i == 'D':
            ans[-1] **= 2
        elif i == 'T':
            ans[-1] **= 3
        elif i == '*':
            ans[-1] *= 2
            # 2번째 세트부터는 지금까지 계산한거에 곱하기
            if len(ans) == 2:
                ans[-2] *= 2
        elif i == '#':
            ans[-1] *= -1
        # 전부 아니고 숫자일경우 => 숫자만 저장!! 기호는 저장할 필요 X
        else:
            # 10인경우와 아닌경우 구분 (중요)
            if dart[idx:idx+2] == '10':
                ans.append(10)

            # 이거 뭔소린지 계속 이해 못했는데, 맨첨에 dart[idx-1]이면 dart[-1]인거임 (idx=0이니까)
            # 쨌든 dart[idx-1] [idx] 조합이 '10'만 아니면 되는거
            elif dart[idx-1:idx+1] != '10':
                ans.append(int(i))

        print(dart[idx-1], dart[idx])
    return sum(ans)

print(sol1('1D2S#10S'))

# 방법 2 : 정규표현식
# - 숫자를 기준으로 잘라주기 (중요중요)
# - 패턴 = re.compile(r'()()()')  <-- 이렇게 그룹핑한다!!!
# - 패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
#   - 앞에는 0~9까지 나올 수 있고, 10도 나올 수 있다.
#   - 중간은 SDT 중 하나가 나올 수 있다. => ~중 하나는 대괄호 [] 로 묶어줘야한다
#   - 마지막 *# 중 하나가 나올 수 있다. => ~중 하나 : [] 글구 나올수도, 안나올수도 있다는 ? 를 추가해줘야한다

import re
def sol2(dart):
    패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    ans = []
    계산식 = {
        'S' : lambda 값:값,
        'D' : lambda 값:값**2,
        'T' : lambda 값:값**3
    }

    for 숫자, 승수, 상 in 패턴.findall(dart):
        # findall()로 총 3개의 패턴(3분할)이 나옴(for문 3번돈다)
        print(숫자, 승수, 상)

        if 승수 == 'S':
            점수 = 계산식['S'](int(숫자))
        elif 승수 == 'D':
            점수 = 계산식['D'](int(숫자))
        elif 승수 == 'T':
            점수 = 계산식['T'](int(숫자))

        if 상 == '*':
            점수 *= 2
            if ans:
                ans[-2] *= 2
        elif 상 == '#':
            점수 *= -1
        # 전부 아니고 숫자일경우 => 숫자만 저장!! 기호는 저장할 필요 X

        ans.append(점수)
    return sum(ans)

print(sol2('1D2S#10S'))



