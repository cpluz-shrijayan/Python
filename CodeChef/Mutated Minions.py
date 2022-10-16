try:
  for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))[:a]
    kk=0
    for i in l:
      if (i+b)%7==0:
        kk+=1
      else:
        continue
    print(kk)
except:
    pass
