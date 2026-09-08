s,n=map(int,input().split())
h=[]
hi=[]
b=[]
bi=[]
for i in range (n):
    l=list(map(int,input().split()))
    hi.append(l)
flag=0
while flag<1 and len(hi)!=0:
    sf = min(hi, key=lambda x: (x[0], -x[1]))
    if sf[0]<s:
        s+=sf[1]
        hi.remove(sf)
    else:
        flag=1

if flag==1:
    print("NO")
else:
    print("YES")

