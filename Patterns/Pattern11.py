class Solution:
    def pattern11(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i%2!=0:
                    if j%2!=0:
                        print("1 ",end="")
                    else:
                        print("0 ",end="")
                else:
                    if j%2!=0:
                        print("0 ",end="")
                    else:
                        print("1 ",end="")
            print()


x=Solution()
x.pattern11(4)