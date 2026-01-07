#Better way to moveZeroes
class Solution:
    def moveZeroes(self, List):
        anchor = 0
        for explorer in range(len(List)):
            if List[explorer] != 0:
                List[anchor], List[explorer] = List[explorer], List[anchor]
                anchor += 1
            