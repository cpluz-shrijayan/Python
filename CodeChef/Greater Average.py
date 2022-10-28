import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print("yes" if math.ceil((a+b)/2)>c else "no")
