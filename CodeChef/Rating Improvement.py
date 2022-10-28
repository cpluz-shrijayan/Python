for _ in range(int(input())):
    x,y=map(int,input().split())
    print("YES" if y>=x and y<=x+200 else "NO")
