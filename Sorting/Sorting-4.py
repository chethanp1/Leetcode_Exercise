# 350. Intersection of Two Arrays II
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a Counter object for each list to count the occurrences of each element
        # Then, use the & operator to find the common elements between the two Counters
        # Finally, use the elements() method to return an iterator over the common elements
        return (Counter(nums1) & Counter(nums2)).elements()