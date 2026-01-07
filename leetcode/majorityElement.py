class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        a = len(nums)//2
        return nums[a]
    
solution = Solution()
nums = [2,2,1,1,1,2,2]
FirstQuestion = solution.majorityElement(nums)
print(FirstQuestion)
