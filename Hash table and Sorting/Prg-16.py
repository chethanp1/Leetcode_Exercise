# Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
    def addBinary(self, a, b):
        res,c= "",0  # Initialize the result and carry variables
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c!= 0:  # Iterate through the binary strings and the carry
            sum = c
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            res = str(sum % 2) + res  # Add the last digit of the sum to the result
            c=sum // 2  # Update the carry for the next iteration
        return res  # Return the sum as a binary string