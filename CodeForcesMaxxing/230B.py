# n=int(input())
# for i in range(n):
#     li=list(map(int,input().split()))
#     for k in li:
#         c=0
#         for o in range (1,k+1):
#             if k%o==0:
#                 c+=1
#         if c==3:
#             print("YES")
#         else:
#             print("NO")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



n=int(input())
li=list(map(int,input().split()))
for k in li:
    c=k**0.5
    if c*c== k and is_prime(c):
        print("YES")
    else:
        print("NO")
