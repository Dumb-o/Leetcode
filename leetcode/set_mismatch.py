class Solution:
    def setMismatch(self, nums: list[int]):
        nums.sort()
        check = 0 
        missed_number = -1 #as missed_num = num 
        repeated_number = 0
        
        for num in nums: 
            repeated_number = num if num - check == 0 else repeated_number
            missed_number = num if num - check == 2 else missed_number
            check = num

        if missed_number == -1:
            if nums[0] != 1:
                missed_number = 1
            else:
                missed_number = len(nums)
        return ([repeated_number, missed_number])