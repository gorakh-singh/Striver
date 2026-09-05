n=int(input())
x=[]
for i in range(n):
    name=input()
    if name in x:
        m=1
        flag=0
        while flag!=1:
            t=name+str(m)
            if t in x:
                t=name
                m+=1
              
            else:
                print(t)
                x.append(t)
                flag=1
    else:
        x.append(name)
        print("OK")

#-------------------ALTERNATE--------------------------#
#dictionery uses hashing in python so searching se more efficient and fast
#the above method would also work but is very slow in case of large n 

n=int(input())
x={}

for _ in range(n):
    name=input()
    if name in x:
        new=name+str(x[name])
        while new in x:
            x[name]=+1
            new=name+str(x[name])
        print(new)

        x[name]+=1
        x[new]=1
    else:
        x[name]=1
        print("OK")
