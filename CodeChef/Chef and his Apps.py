for _ in range(int(input())):
    s,x,y,z=map(int,input().split())
    a=x+y 
    b=s-a
    if b>=z:
        print("0")
    elif b+max(x,y)>=z:
        print("1")
    else:
        print("2")
