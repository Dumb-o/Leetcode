#.copy wasnt introduced to python till 3.3, use prices[:] instead if you have an older version
class Solution(object):
    def maxProfit(self, prices):
        finding_the_best = prices.copy()
        finding_the_best.sort()
        
        best_purchase_cost = finding_the_best[0]
        
        filtered_price = prices.copy()

        for price in prices:
            print(price)
            if price != best_purchase_cost:
                filtered_price.remove(price)
            else:
                break

        try:
            filtered_price.sort()
            best_selling_cost = filtered_price[-1]
            return best_selling_cost - best_purchase_cost
        except:
            return 0
        
stock = [7,1,5,3,6,4]
solution = Solution()
firstQuestion = solution.maxProfit(stock)
print(firstQuestion)
