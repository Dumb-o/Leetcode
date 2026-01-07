class Solution(object):
    def isPalindrome(self,x):
        isPalinedrome = False
        checker = []
        
        x = str(x)
        for numbers in x:
            checker.append(numbers)

        palinedrome_checker = checker[::-1]
        
        if checker == palinedrome_checker:
            isPalinedrome = True
            return isPalinedrome
        else:
            return isPalinedrome

solution = Solution()
firstQuestion = solution.isPalindrome(123)
print(firstQuestion)  

        