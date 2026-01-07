class Solution(object):
    def addDigits(self, num):
        while num >=10:
            str_num = str(num)
            l_num = []
            for i in str_num:
                j = int(i)
                l_num.append(j)
            num = sum(l_num)    
        return num

solution = Solution()
print(solution.addDigits(123))
