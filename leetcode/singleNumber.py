class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i=0
        while i!= len(nums):
            try:
                print(i)
                if nums[i] == nums[i+1]:
                    i += 2
                else:
                    return nums[i]
            except: 
                return nums[-1]
            
solution = Solution()
list1 = [1,1,2,2,3,3,4,4,5,4,4,74,74]
firstQuestion = solution.singleNumber(list1)
print(firstQuestion)
