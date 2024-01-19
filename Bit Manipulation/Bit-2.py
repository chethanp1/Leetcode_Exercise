# 191. Number of 1 Bits

# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')  # Convert the integer to its binary representation and count the occurrences of '1'