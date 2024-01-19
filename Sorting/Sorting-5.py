#
# 349. Intersection of Two Arrays
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)  # Convert the two lists to sets
        return nums1 & nums2  # Find the common elements between the two sets using the & operator