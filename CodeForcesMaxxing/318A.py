n,p=map(int,input().split())
# li=[]
# for i in range(1,n+1):
#     if i%2!=0:
#         li.append(i)
# for i in range(1,n+1):
#     if i%2==0:
#         li.append(i)
# print(li-1)

if n%2==0:
    if p>n/2:
        print(2*(p-(n/2)))
    else:
        print(2*(n)+1)

if n%2!=0:
    if p>((n+1)/2):
        print(2*(p-((n+1)/2)))
    else:
        print(2*(n)+1)

