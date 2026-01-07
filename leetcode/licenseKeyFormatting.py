class Solution(object): 
    def licenseKeyFormatting(self, s, k):
        license = s.upper()
        j = 0
        characters = license.split("-") #List
        final = ""
        for word in characters[::-1]:
            for i in word[::-1]:
                final = i + final 
                j += 1
                if j == k:
                    final = "-" + final
                    j = 0
        try:
            if final[0] == "-":
                final = final[1:]
        except:
            pass
        return final

           
solution = Solution()
print(solution.licenseKeyFormatting("4sad-123-ad-1",5))
