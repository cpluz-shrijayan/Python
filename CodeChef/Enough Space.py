for _ in range(int(input())):
    n,x,y=map(int,input().split())
    print("YES" if n>=((x*1)+(y*2)) else "NO")
