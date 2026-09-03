t = int(input())
for i in range(t):
    lis=list(map(int,input().split()))
    r=0
    flag=0
    while flag!=1:
        if len(lis)!=len(set(lis)):
            print(r)
            flag=1
        else:
            lis[lis.index(max(lis))]=max(lis)-1
            lis[lis.index(min(lis))]=min(lis)+1
            r+=1

