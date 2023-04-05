s = "1326#"
alpha = "abcdefghijklmnopqrstuvwxyz"
returs = ''

i = len(s)-1

while i>=0:
    if s[i] == '#':
        # print()
        returs += str(alpha[int(s[i-2]+s[i-1])-1])
        i-=3
    else:
        # print(alpha[int(s[i])-1])
        returs += str(alpha[int(s[i])-1])
        i-=1
print(returs[::-1])