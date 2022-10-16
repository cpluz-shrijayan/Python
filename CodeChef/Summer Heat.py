def coconut(a,b,xa,xb):
    return int(xa/a+xb/b) 

for _ in range(int(input())):
    a,b,xa,xb=map(int,input().split())
    print(coconut(a,b,xa,xb))
