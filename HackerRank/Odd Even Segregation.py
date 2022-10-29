n=int(input())
l=list(map(int,input().split()))[:n]
nl=[nums for nums in l if nums%2!=0] + [nums for nums in l if nums%2==0]
print(*nl)
