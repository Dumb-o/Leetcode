class Solution:
    def moveZeroes(self,List):
        i = 0
        for num in List:
            i += num
        if i==0:
            return List

        for num in List:
            if num == 0:
                List.remove(num)
                List.append(num)

        return List

solution = Solution()
list = [0,1,0,3,12]
firstQuestion = solution.moveZeroes(list)
print(firstQuestion)

