n=int(input())
for _ in n:
    x,y=map(int,input().split())
    flag=0
    while x>0 or flag>1:
        x1=[int(i) for i in f"{x:b}"]
        y1=[int(i) for i in f"{y:b}"]
        if len(y1)>len(x1):
            y-=1




