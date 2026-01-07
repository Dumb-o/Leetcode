class Solution(object):
    def lengthOfLastWord(self, s):
        sentence = s.strip()
        words = sentence.split(" ")
        return len(words[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))

a = "     a        hello       "
b = a.strip()
print(b)
