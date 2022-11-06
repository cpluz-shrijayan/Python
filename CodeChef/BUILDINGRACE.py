for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    m=a/x 
    n=b/y 
    if m<n:
        print("Chef")
    elif m>n:
        print("Chefina")
    else:
        print("Both")
        
