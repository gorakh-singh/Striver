n=int(input())
x=[]
flag=0
m=0
for i in range(n):
    name=input()
    if name in x:
        while flag!=1:
            name=name+m
            if name in x:
                flag=1
            else:
                print(name)
    else:
        x.append(name)
        print("OK")
