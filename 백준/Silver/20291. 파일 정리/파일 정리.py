# 카운터 안쓰고 딕셔너리로만 푼 방법
n = int(input())

file = dict()
for _ in range(n):
    extend = (input().split('.'))[1]  # (중요) 입력받자마자 바로 확장자만 저장
    
    if not extend in file:
        file[extend] = 1               # 딕셔너리는 해당 키값이 idx임
    else:
        file[extend] += 1

sort_file = sorted(file.items())       # 키값(item값)을 기준으로 정렬

for key, val in sort_file:             # 딕셔너리 가져올 때 반드시!!
    print(key.rstrip(), val)