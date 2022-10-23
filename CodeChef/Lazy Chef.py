for _ in range(int(input())):
    x,m,d=map(int,input().split())
    a=x*m 
    b=x+d 
    print(min(a,b))
