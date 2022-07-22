for i in range(int(input())):
    n=input()
    s=len(n)/2
    n1=n[:int(s)]
    n2=n[int(s):]
    if n1==n2:
        print("YES")
    else:
        print("NO")
