class Solution(object):
    def search(self, nums, target):
        try:
            return (nums.index(target))
        except ValueError:
            return -1
        

solution = Solution()

list = [1,2,4,5,2,34,24,23,42,34,23,4,234,2,3,52,35,52]
firstQuestion = solution.search(list, 5)
print(firstQuestion)

