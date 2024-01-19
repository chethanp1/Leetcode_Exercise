#
# 168. Excel Sheet Column Title
#
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
class Solution:
    def convertToTitle(self, cn: int) -> str:
        res = ""  # Initialize an empty string to store the result
        while cn:  # Continue the loop until the input integer is not zero
            r = cn % 26  # Calculate the remainder when dividing the input integer by 26
            if r == 0:  # If the remainder is 0, it represents the character 'Z'
                res += "Z"  # Append 'Z' to the result string
                cn -= 1  # Decrement the input integer by 1
            else:
                res += chr(r + 64)  # Append the corresponding character to the result string
            cn //= 26  # Update the input integer by dividing it by 26
        return res[::-1]  # Reverse the result string and return it