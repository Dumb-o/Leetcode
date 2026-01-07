class Solution:
    def reverse(self, x: int) -> int:
        sign = '-' if x < 0 else "+"
        rev = str(abs(x))[::-1]

        val = int(sign + rev)

        if abs(val) > 2147483648:
            return 0
        else: 
            return val
