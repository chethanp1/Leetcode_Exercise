# 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1

        while True:
            if x == n:
                return True
            elif x > n:
                return False

            x <<= 1