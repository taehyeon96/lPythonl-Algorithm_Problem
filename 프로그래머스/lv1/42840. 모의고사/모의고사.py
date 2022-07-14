def solution(answers):
    answer = [0,0,0]
    leng = len(answers)
    ans = []
    
    man1 = [i+1 for i in range(5)]*2000
    man2 = [2,1,2,3,2,4,2,5] * 1250
    man3 = [3,3,1,1,2,2,4,4,5,5]*1000
    
    for i in range(leng):
        if man1[i] == answers[i]:  answer[0] += 1
        if man2[i] == answers[i]:  answer[1] += 1
        if man3[i] == answers[i]:  answer[2] += 1
        
    indexer = answer.index(max(answer))
    
    for i in range(3):
        if answer[i] == answer[indexer]:
            ans.append(i+1)
            
    return ans