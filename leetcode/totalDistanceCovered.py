class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        ans = 0
        while mainTank >= 5 and additionalTank > 0:
            ans +=  5
            mainTank -= 5
            mainTank += 1
            additionalTank -= 1
        
        rem_fuel = 10* mainTank
        ans = (ans*10) + rem_fuel
        return ans
    
solution = Solution()
firstQuestion = solution.distanceTraveled(5,1)
print(firstQuestion)
