# n=int(input())
# li=list(map(int,input().split()))
# x=[]
# c=0
# for i in range(n):
#     if i not in x:
#         sum=li[i]
#         x.append(i)
#         if sum<4:
#             for j in range(n):
#                 if j not in x and j>i:
#                     sum+=li[j]
#                     if sum<=4:
#                         x.append(j)
#                     else:
#                         sum=sum-li[j]
#             c+=1       
#         else:
#             c+=1
# print(c)
n=int(input())
li=list(map(int,input().split()))
d={}
taxi=0
d[1]=li.count(1)
d[2]=li.count(2)
d[3]=li.count(3)
d[4]=li.count(4)

taxi = d[4]


taxi += d[3]
d[1] = max(0, d[1] - d[3])

taxi += d[2] // 2
if d[2] % 2 != 0:
    taxi += 1
    d[1] = max(0, d[1] - 2) 


if d[1] > 0:
    taxi += (d[1] + 3) // 4

print(taxi)
