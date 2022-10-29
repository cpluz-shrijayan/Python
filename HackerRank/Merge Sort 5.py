n=int(input())
l=list(map(int,input().split()))
nl=[]
while l:
    mini=l[0]
    for i in l:
        if i<mini:
            mini=i
    nl.append(mini)
    l.remove(mini)
print(*nl)
