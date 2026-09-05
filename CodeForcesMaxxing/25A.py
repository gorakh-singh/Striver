n=int(input())
l=list(map(int,input().split()))
x=[]
t=[]
for i in range(n):
    if l[i]%2==0:
        x.append(i)
    else:
        t.append(i)

if len(x)==1:
    print(x[0]+1)
else:
    print(t[0]+1)

