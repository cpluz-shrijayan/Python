for _ in range(int(input())):
  f=1
  n=int(input())
  for i in range(1,n+1):
    f*=i
  k=""
  k=str(f)
  print(len(k) - len(k.rstrip('0')))
