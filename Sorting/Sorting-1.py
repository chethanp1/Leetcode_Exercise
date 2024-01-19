# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}  # Initialize an empty dictionary to store the frequency of each character
        for char in s:  # Iterate through each character in the input string
            d[char] = d.get(char, 0) + 1  # Update the frequency count of the character in the dictionary

        # Sort the dictionary based on the frequency count in descending order
        sortedList = sorted(d.items(), key=lambda x: x[1], reverse=True)

        res = ''  # Initialize an empty string to store the sorted characters
        for tupleEle in sortedList:  # Iterate through the sorted list of tuples
            res = res + tupleEle[0] * tupleEle[1]  # Append the character to the result string based on its frequency

        return res  # Return the sorted string