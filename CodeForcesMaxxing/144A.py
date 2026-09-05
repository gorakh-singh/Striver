c=0
def maxi(l,ind):
    l[ind],l[ind-1]=l[ind-1],l[ind]
    return l

def mini(l,ind):
    l[ind],l[ind+1]=l[ind+1],l[ind]
    return l

n=int(input())
l=list(map(int,input().split()))
print(min(range(len(l)), key=lambda i: (l[i], -i)))

while min(range(len(l)), key=lambda i: (l[i], -i))!=(n-1) or l.index(max(l))!=0:
    if min(range(len(l)), key=lambda i: (l[i], -i))!=(n-1):
        c=c+1
        l=mini(l,min(range(len(l)), key=lambda i: (l[i], -i)))
    if l.index(max(l))!=0:
        c=c+1
        l=maxi(l,l.index(max(l)))



print(c)
print(l)