class Solution(object):
    def twoSum(self,nums,target):
        a=-1
        b=-1
        for num in nums:
            a+=1
            b=-1
            for num2 in nums:
                b+=1
                if num + num2 == target and a!=b:
                    return(a,b)

nums = [1,2,3,4,5,6]
target = 11

solution = Solution()
FirstQuestion = solution.twoSum(nums,target)
print(FirstQuestion)
