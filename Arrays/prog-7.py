#
# 34. Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        if target in nums:
            for i in range(0,n):
                if nums[left]==nums[right]:
                    return [left,right]
                elif nums[left]<target:
                    left+=1
                else:
                    right-=1
        else:
            return [-1,-1]  