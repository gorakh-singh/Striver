s=input()
lis=list(s)
lis1=list("hello")
t=0
flag=10
for a in lis:
    if a==lis1[t]:
        t+=1
        if t==len(lis1):
         flag=0
         break
if flag==10:
    print("NO")
else:
    print("YES")
 