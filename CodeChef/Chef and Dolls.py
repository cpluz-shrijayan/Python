for i in range(int(input())):
  dicts={}
  for i in range(int(input())):
    k=input()
    if k in dicts:
      dicts[k]+=1
    else:
      dicts[k]=1
  for k in dicts:
    if dicts[k]%2==1:
      print(k)
      
(r)

for _ in range(int(input())):
  l=[]
  for _ in range(int(input())):
      n=int(input())
      l.append(n)
  for i in l:
      if l.count(i)==1:
          print(i)
