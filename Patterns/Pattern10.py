class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            print("*"*i)
        for i in range(1,n):
            print("*"*(n-i))

x=Solution()
x.pattern10(4)


