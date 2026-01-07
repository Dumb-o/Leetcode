class Solution(object):
    def fizzBuzz(self, n):
        fb = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                fb.append("FizzBuzz")
            elif i % 3 == 0:
                fb.append("Fizz")
            elif i % 5 == 0:
                fb.append("Buzz")
            else:
                fb.append(str(i))
        return fb 

solution = Solution()
print(solution.fizzBuzz(5))       
