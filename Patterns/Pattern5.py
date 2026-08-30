class Solution:
    def pattern5(self, n):
        for i in range(n):
            print("*"*(n-i))

x= Solution()
x.pattern5(4)