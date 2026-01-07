class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        for i in nums:
            if nums[i] == nums[i+1]:

        return nums

solution = Solution()
here = [1,2,3,4,2,1,3,2]
firstQuestion = solution.removeDuplicates(here)
print(firstQuestion)



