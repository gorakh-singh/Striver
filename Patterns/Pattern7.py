class Solution:
    def pattern7(self, n):
        for i in range(1,n+1):
            print(" "*(n-i)+"*"*(2*i-1))
x=Solution()
x.pattern7(2)