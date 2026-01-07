class Solution(object):
    def isFascinating(self, n):
        second = 2*n
        third = 3*n
        
        n = str(n)
        second = str(second)
        third = str(third)
        fourth =  n + second + third
        
        if len(fourth) > 9:
            return False

        for i in range(1,10):
            if str(i)in str(fourth):
                check = True
            else:
                return False
        
        return check

solution = Solution()
firstQuestion = solution.isFascinating(267)
print(firstQuestion)
