class Solution(object):
    def isValid(self,s):
        s_count = s_end_count = m_count = m_end_count = b_count = b_end_count = 0
        for chars in s:
            if chars == "(":
                s_count += 1
            if chars == ")":
                s_end_count +=1
            if chars == "{":
                m_count += 1
            if chars == "}":
                m_end_count +=1
            if chars == "[":
                b_count += 1
            if chars == "]":
                b_end_count +=1
        
        if s_count == s_end_count and m_count == m_end_count and b_count == b_end_count:
            return True
        else:
            return False
solution = Solution()
word = "{}()["
FirstQuestion = solution.isValid(word)
print(FirstQuestion)
