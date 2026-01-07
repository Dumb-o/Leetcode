class Solution(object):
    def findNumbers(self, nums):
        check = 0
        for num in nums:
            nu = str(num)
            if len(nu) % 2 == 0:
                check += 1
        return check

solution = Solution()
print(solution.findNumbers([123,321,1321,3213]))
