#Test
class Solution():
    def minCost(self,days,cost):
        total_days = days[-1]-days[0]
        total_cost = 0
        total_set = []

        while total_days > 0:
            if total_days % 30 > 0:
                total_set.append("30")
                total_days -= 30
                print(total_days)

            elif total_days % 7 > 0:
                total_set.append("7")
                total_days -= 7
                print(total_days)

            elif total_days % 1 > 0:
                total_set.append("1")
                total_days -= 1
                print(total_days)

        for i in total_set:
            if i == "30":
                total_cost += cost[2]
            elif i == "7":
                total_cost += cost[1]
            else:
                total_cost += cost[0]

        print(total_cost)
        return total_cost    
        
solution = Solution()
days = [1,5,6,30,35]
cost = [2,7,15]
firstQuestion = solution.minCost(days,cost)
