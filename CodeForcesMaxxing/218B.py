p,f=map(int,input().split())
l=list(map(int,input().split()))
mini=0
maxi=0
x=0
y=0
s=sorted(l)
d=sorted(l)
for i in range(p):
    s=sorted(s)
    while s[f-1-x]==0:
        x+=1
    maxi+=s[f-1-x]
    s[f-1-x]=s[f-1-x]-1
    


for i in range(p):
    d=sorted(d)
    while d[y]==0:
        y+=1
    mini+=d[y]
    d[y]=d[y]-1

print(maxi,mini)
