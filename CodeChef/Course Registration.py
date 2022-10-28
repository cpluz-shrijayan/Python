for _ in range(int(input())):
    n,m,k=map(int,input().split())
    print("Yes" if (m-k)>=n else "No")
