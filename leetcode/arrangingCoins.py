class Solution(object):
    def arrangeCoins(self, n):
        i=1
        rows = 0
        if n == 1:
            return 1
        
        while True:
            if n - i >= 0:
                rows+=1
                n-=i
                i+=1
            else:
                return rows

solution = Solution()
print(solution.arrangeCoins(3))
