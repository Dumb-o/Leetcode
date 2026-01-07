# class Solution():
#     def consecutive_ones(nums:list):
        
#         lst_index = len(nums) - 1
#         count = 0
#         lst_check = 0
        
#         for index, num in enumerate(nums):
#             if (num == 0) or (index == lst_index and num ==1):
#                 check_count = index - lst_check
#                 lst_check = index
#                 count  = max(count, check_count)
#         return count 

class Solution():
    def consecutive_ones(self, nums:list) -> int:
        max_count = 0 
        current_count = 0 

        for num in nums: 
            if num == 1:
                current_count += 1 
                max_count = max(current_count, max_count)
            else: 
                current_count = 0
        return max_count

