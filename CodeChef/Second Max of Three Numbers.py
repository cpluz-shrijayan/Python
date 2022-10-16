for _ in range(int(input())):
    a=list(map(int,input().split()))[:3]
    a.sort()
    print(a[-2])
