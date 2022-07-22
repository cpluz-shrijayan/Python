for i in range(int(input())):
    n=int(input())
    s=n/2
    n1=n[:s-1]
    n2=n[s:]
    if n1==n2:
        print("YES")
    else:
        print("NO")
