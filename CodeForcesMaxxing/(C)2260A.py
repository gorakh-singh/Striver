n=int(input())
c=0
for i in range(n):
    t=int(input())
    li=list(map(int,input().split()))
    if li.count(0)>1:
        while li[0]!=0 or li[t-1]!=0:
            ind1=li.index(0)
            ind2=min(range(len(li)), key=lambda i: (li[i], -i))
        
            if li[0]!=0:
                li[ind1],li[0]=li[0],li[ind1]
                c+=1
            if li[t-1]!=0:
                li[ind2],li[t-1]=li[t-1],li[ind2]
                c+=1
        if li[0]==0 and li[t-1]==0:
            print(c)
            c=0
    else:
        print(-1)
    

