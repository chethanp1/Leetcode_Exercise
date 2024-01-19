# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        # Define a dictionary to map each digit to a string of corresponding letters
        counter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        c = len(digits)
        if c == 0:
            return []  # Return an empty list if the input is empty
        if c == 1:
            return list(counter[digits[0]])  # Return the list of letters for the single input digit
        # Generate the combinations based on the input digits
        ff = [x + y for x in counter[digits[0]] for y in counter[digits[1]]]
        if c == 2:
            return ff  # Return the combinations for two input digits
        if c == 3:
            ff = [x + y for x in ff for y in counter[digits[2]]]  # Return the combinations for three input digits
        if c == 4:
            fg = [x + y for x in counter[digits[2]] for y in counter[digits[3]]]
            ff = [x + y for x in ff for y in fg]  # Return the combinations for four input digits
        return ff  # Return the generated combinations