def sums(d,n):
  for i in range(d):
    n=n*(n+1)/2
  return int(n) 

for _ in range(int(input())):
  d,n=map(int,input().split())
  print(sums(d,n))
