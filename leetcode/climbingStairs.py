#Sum of fibonacci sequence but first num is 1 and second num is 2 and range n-2 because idk, its needed lol

class Solution(object):
    def fibonacci(self,n):
        first_num = 0
        second_num = 1
        if n<2:
            return first_num
        elif n ==2:
            return second_num
        
        for i in range(n-1):
            num = first_num + second_num
            first_num = second_num
            second_num = num
        return num

    def climbStairs(self, n):
        first_num = 1
        second_num = 2
        if n < 2:
            return first_num 
        elif n == 2:
            return second_num
        for i in range(n-2):
            num = first_num + second_num
            first_num = second_num
            second_num = num
        return num

solution = Solution()
firstQuestion = solution.fibonacci(5)
print(firstQuestion)
secondQuestion = solution.climbStairs(5)
print(secondQuestion)
