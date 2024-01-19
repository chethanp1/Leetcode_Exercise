# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        reverse = 0  # Initialize the variable to store the reverse of the number
        sign = -1 if x < 0 else 1  # Determine the sign of the number
        x = abs(x)  # Get the absolute value of the number
        while x:
            digit = x % 10  # Get the last digit of the number
            reverse = reverse * 10 + digit  # Add the last digit to the reverse
            x /= 10  # Remove the last digit from the number
        result = sign * reverse  # Apply the original sign to the reversed number
        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            return 0  # Return 0 if the reverse overflows
        return result  # Return the reversed integer