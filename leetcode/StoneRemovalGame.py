#Sometimes my genius, I really dont understand it myself lol
class Solution(object):
    def canAliceWin(self, n):
        aliceWins = False
        i=10

        while n > 0:
            if n < i:
                return aliceWins
            aliceWins = not aliceWins
            n -= i        
            i -= 1
        return aliceWins
    
solution = Solution()
firstQuestion = solution.canAliceWin(12)
print(firstQuestion)
                   
        
        