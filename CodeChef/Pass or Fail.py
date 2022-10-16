def prf(n,x,p):
    if ((3*x)-(n-x))>=p:
        return "PASS"
    else:
        return "FAIL"
for _ in range(int(input())):
  n,x,p=map(int,input().split())
  print(prf(n,x,p))
