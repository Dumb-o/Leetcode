class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        while n>=1:
            n = n/4.0
            if n ==1.0:
                return True
        return False


solution = Solution()
print(solution.isPowerOfFour(16))
