class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            print(str(i)*i)

x=Solution()
x.pattern4(4)