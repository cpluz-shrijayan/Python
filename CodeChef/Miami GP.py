for _ in range(int(input())):
    x,y=map(int,input().split())
    print("Yes" if (x*1.07)>=y else "No")
