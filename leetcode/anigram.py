class Solution():
    def isAnagram(self, a, b):
        list_a =[]
        list_b = []

        for i in a:
            if b.index(i) == True:
                b.remove(i)
            else:
                return False
        return True
    
        for i in a:
            list_a.append(i)
        list_a.sort()
    
        for i in b:
            list_b.append(i)
        list_b.sort()

        if list_a == list_b:
            return True
        else:
            return False

solution = Solution()
firstQuestion = solution.isAnagram("hehe","eehh")
print(firstQuestion)
