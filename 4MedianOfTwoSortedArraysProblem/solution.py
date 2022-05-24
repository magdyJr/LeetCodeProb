from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #sorting the 2 arrays and mergin in new list
        newList=sorted(nums1+nums2)
        #gets position of the median
        median =int(len(newList)/2)
        # if new list len is divide by 2 we return the sum divide by 2 of the num in median position
        #and the previous number
        if len(newList) % 2 == 0:
            return (newList[median]+newList[median-1])/2
        # else we return the num in the median pos
        else:
            return float(newList[median])

#Testcases
sol=Solution()
print(sol.findMedianSortedArrays([1,3],[2]))
print(sol.findMedianSortedArrays([1,3],[2,4]))