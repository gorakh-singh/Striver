o=int(input())
for _ in range(o):
    a=[]
    g=[]
    c=0
    n,k=map(int,input().split())
    li=list(map(int,input()))
    for i in range(len(li)):
        g.append(li[i])
        if (i+1)%k==0:
            a.append(g)
            g=[]
    for i in a:
        if 0 not in i:
            c+=1
    print(c)



