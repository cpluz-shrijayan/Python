for _ in range(int(input())):
    n=int(input())
    if n%5!=0:
        c=-1
    else:
        c=n//10
        c+=(n%10)/5
    print(int(c))
