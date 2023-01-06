for i in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print("0")
    elif x>y:
        if (x-y)%2!=0:
            print(2+((x-y)//2))
        else:
            print((x-y)//2)
    else:
        print(y-x)
