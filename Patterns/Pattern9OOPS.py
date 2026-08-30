class Solution:
    def pattern9(self, n):
        def pattern7(self, n):
            for i in range(1,n+1):
                print(" "*(n-i)+"*"*(2*i-1))
        def pattern8(self, n):
            for i in range(n):
                print(" "*(i)+"*"*(2*n-1-(2*i)))
        pattern7(self, n)
        pattern8(self, n)

x=Solution()
x.pattern9(4)