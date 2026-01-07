class Solution: 
    def palindromeInString(self, s: str) -> str:        
        start = end = 0
        for i in range(len(s)):
            l = r = i
            while s[l] == s[r] and l>=0 and r<len(s):
                if r - l > end - start:
                    start = l 
                    end = r 
                r += 1
                l -= 1
            
            l = i 
            r = i + 1
            while s[l] == s[r] and l>=0 and r<len(s):
                if r - l >  end - start:
                    start = l 
                    end = r 
                r += 1
                l -= 1

        return s[start: end + 1] 
        
