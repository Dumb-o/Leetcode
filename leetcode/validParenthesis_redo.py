class Solution(object):
    def isValid(self,s):
        list = ["."] # This . is so fucking important else list[-1] gonna give error
        for c in s:
            if c == "(" or c == "{" or c == "[":
                list.append(c)
            elif c == ")" and list[-1] == "(":
                list.pop()
            elif c == "}" and list[-1] == "{":
                 list.pop()
            elif c == "]" and list[-1] == "[":
                list.pop()
            else:
                return False
                           
        if len(list) == 1:
            return True
        else:
            return False
text = "]"
solution = Solution()
FirstQuestion = solution.isValid(text)
print(FirstQuestion)
