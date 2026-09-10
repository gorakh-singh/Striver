# def rem(li,ind):
#     for i in range(ind):
#         li.pop(ind)
#     return li

# def incre(li,ind):
#     for i in range(ind):
#         li[i]+=1
#     return li

# def addi(li,ind):
#     sum=0
#     for i in range(ind):
#         sum+=li[i]
#     return sum


# n=int(input())
# flag=0
# for _ in range (n):
#     n1=int(input())
#     li=list(map(int,input().split()))
#     mck=[0]*n1
#     ans=[]
#     flag=0
#     l2=sorted(li)
#     mck2=l2
#     for i in range(n1-1):
#          if l2[0]!=l2[i]:
#             x=i 
#             break
#     while flag<=1:
#         if len(mck2)>1:
#             for i in range(len(mck2)):
#                 if mck2[0]!=mck2[i]:
#                     x=i 
#                     break
#             if x==len(mck2):
#                 while mck2[x]!=addi(mck,x-1):
#                     mck=incre(mck,x)
#                     print(ans)
#                     print(mck)
#                 if len(mck)==1:
#                     flag=10
#                 elif mck2[x]==addi(mck,x-1):
#                     ans.extend(mck)
#                     mck2[len(mck)-1]=mck2[len(mck2)-1]-addi(mck,x)
#                     mck=rem(mck,x)
#                     mck2=rem(mck2,x)
#                     print(ans)
#                     print(mck)
#                     print(mck2)
#             else:
#                 while mck2[x]!=addi(mck,x-1):
#                     mck=incre(mck,x)
#                     print(ans)
#                     print(mck)
#                 if len(mck)==1:
#                     flag=10
#                 elif mck2[x+1]==addi(mck,x):
#                     ans.extend(mck)
#                     mck2[len(mck)-1]=mck2[len(mck2)-1]-addi(mck,x)
#                     mck=rem(mck,x)
#                     mck2=rem(mck2,x)
#                     print(ans)
#                     print(mck)
#                     print(mck2)
#         else:
#             flag=10
#             break
        
        

                
# print(ans)
            
