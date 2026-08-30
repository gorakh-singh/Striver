class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(1,n-i+1):
                print(j,end="")
            print()
x=Solution()
x.pattern6(4)
