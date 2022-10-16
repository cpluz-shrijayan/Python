def age(x,y,a):
    if a>=x and a<y:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    x,y,a=map(int,input().split())
    print(age(x,y,a))
