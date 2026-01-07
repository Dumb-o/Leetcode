class Solution:
    def splitWordsBySeparator(self,words,separator):
        final = []

        for word in words:
            a = word.split(separator)
            for wor in a:
                final.append(wor)

        for word in final:
            if word == "":
                final.remove(word)    
        return final

words = ["hello.World",".hehe."]

solution = Solution()
firstQuestion = solution.splitWordsBySeparator(words,".")    
print(firstQuestion)
