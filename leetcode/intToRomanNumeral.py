class Solution(object):
    dic = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    def romanToInt(self, s):
        list = []
        rlist = []

        str(s)
        for num in s:
            list.append(int(s))
        
        list.reverse()
        
        while len(list) < 4:
            list.append(0)

        list.reverse()

        thousandth = num[0]
        hundreth = num[1]
        tenth = num[2]
        solo = num[3]

        
solution = Solution()
s = 202
FirstQuestion = solution.romanToInt(s)