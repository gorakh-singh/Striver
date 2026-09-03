class Solution:
    def pattern9(self, n):
        for i in range(1,n+1):
            print(" "*(n-i)+"*"*(2*i-1))
        for i in range(n):
            print(" "*(i)+"*"*(2*n-1-(2*i)))
       

x=Solution()
x.pattern9(4)