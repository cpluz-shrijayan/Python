for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))[:n]
    count=0
    for t in d:
        if t>=1000:
            count+=1 
    print(count)
