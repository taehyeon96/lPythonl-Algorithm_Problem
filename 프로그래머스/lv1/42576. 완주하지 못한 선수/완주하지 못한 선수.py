def solution(participant, completion):
    answer = ''
    leng = len(participant)
    
    participant.sort()
    completion.sort()
    completion.append('0')
    for i in range(leng):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
            
    return answer