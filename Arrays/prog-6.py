# 46. Permutations
# # Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use the permutations() function from the itertools module to generate all permutations of the input list
        return list(permutations(nums))