for _ in  range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))[:n]
    a=0
    b=0
    for i in p:
        a+=i
        if i>k:
            b+=k 
        else:
            b+=i 
    print(a-b)
