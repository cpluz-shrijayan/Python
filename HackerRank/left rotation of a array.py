n,d=map(int,input().split())
a=list(map(int,input().split()))[:n]
for i in range(1,d+1):
    a.append(a[0])
    a.pop(0)
print(*a)
