#
# 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.
class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')  # Convert the integer to its binary representation
        n = n.zfill(32)  # Pad the binary string with leading zeros to make it 32 bits long
        return int(n[::-1], 2)  # Reverse the binary string and convert it back to an integer