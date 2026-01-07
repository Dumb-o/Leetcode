class Solution:
    def medianOfTwoSortedArrays(self, list1: list[int], list2: list[int]):
        final_list = list1 + list2 
        if len(final_list) % 2 == 0:
            left = len(final_list) / 2 - 1
            right  = len(final_list) / 2

            output = (final_list[left] + final_list[right]) / 2
        else:
            middle = (len(final_list) + 1) / 2
            output = final_list[middle]
        
        return output 
