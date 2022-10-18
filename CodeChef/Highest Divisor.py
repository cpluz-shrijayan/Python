n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0 and i<10:
        l.append(i)
print(max(l))
