n=input()
flag=0

if n[0].islower():
    for i in range(1,len(n)):
        if ord(n[i])>=65 and ord(n[i])<=90:
            flag=10
        else:
            flag=1 
            break
else:
    for i in range(len(n)):
        if ord(n[i])>=65 and ord(n[i])<=90:
            flag=10
        else:
            flag=1 
            break

if flag==10 and len(n)>1:
    n=n.swapcase()
    print(n)
elif len(n)==1:
    print(n.swapcase())
else:
    print(n)
