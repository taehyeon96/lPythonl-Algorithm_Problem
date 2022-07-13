text = input()

ans = ''
tmp = ''

text = list(text)
while text:
    now = text.pop(0)

    if now == '<':          
        ans += tmp[::-1] + now
        tmp = ''
        now = text.pop(0)
        while now != '>':     
            ans += now
            now = text.pop(0)
        ans += '>'
    else:
        if now != ' ':
            tmp += now
        else:
            ans += tmp[::-1] + now
            tmp = ''
        
print(ans+tmp[::-1])