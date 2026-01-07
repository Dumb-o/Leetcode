class Solution(object):
    def longestPalindrome(self, s):
        final = ""        
        for i in s[-1::-1]:
            final += i

        length = len(final)
        longest_palindrome = ""

solution = Solution()
print(solution.longestPalindrome("babad"))
