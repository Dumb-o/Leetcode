class Solution():
    def lengthOfLongestSubstring(self, s:str) -> str:
        words = []
        count = 0 
        max_count = 0 

        for word in s:
            if word not in words:
                words.append(word)
                count += 1
                max_count = count if count > max_count else max_count
            else:
                index = words.index(word)
                del words[:index+1]
                words.append(word)
                count = len(words)
        
        return max_count