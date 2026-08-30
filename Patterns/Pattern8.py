class Solution:
    def pattern8(self, n):
        for i in range(n):
            print(" "*(i)+"*"*(2*n-1-(2*i)))
x=Solution()
x.pattern8(4)