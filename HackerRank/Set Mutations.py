na=int(input())
a=set(map(int,input().split()))
nb=int(input())
for i in range(nb):
    s=list(input().split())
    l=set(map(int,input().split()))
    if(s[0]=='update'):
        a.update(l)
    elif(s[0]=='intersection_update'):
        a.intersection_update(l)
    elif(s[0]=='difference_update'):
        a.difference_update(l)
    else:
        a.symmetric_difference_update(l)
print(sum(a))

