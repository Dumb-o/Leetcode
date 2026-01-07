# double pointer may work
class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        p_a = 0 
        p_b = len(a) - 1
        while p_a < p_b:
            if a[p_a] in "AEIOUaeiou":
                while p_a < p_b and a[p_b] not in "AEIOUaeiou":
                    p_b -= 1
                if p_a == p_b:
                    break
                a[p_a], a[p_b] = a[p_b], a[p_a]
                p_b -= 1 
            p_a += 1
        return "".join(a)