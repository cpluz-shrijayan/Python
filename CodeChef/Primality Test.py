for _ in range(int(input())):
    n=int(input())
    flag=0
    if n>1:
      for i in range(2,n+1):
        if(n%i)==0:
            flag+=1
    if(flag==1):
      print("yes")
    else:
      print("no")
