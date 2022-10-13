lst=list(map(int,input().split()))
c=0
for i in range(0,4):
    if lst[i]>=10:
      c+=1
print(c)
