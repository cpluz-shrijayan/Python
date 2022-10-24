for _ in range(int(input())):
    g1,s1,b1,g2,s2,b2=map(int,input().split())
    a=g1+s1+b1
    b=g2+s2+b2
    print("1" if a>b else "2")
