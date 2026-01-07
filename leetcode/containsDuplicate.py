class Solution():
    def containsDuplicate(self, nums):
        nums.sort()
        
        new_list = list(zip(nums,nums[1:]))
        result = any(a==b for a,b in new_list)
        return result
            
solution = Solution()
print(solution.containsDuplicate([1,2,3,4,1]))
