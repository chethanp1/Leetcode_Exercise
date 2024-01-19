#
# 345. Reverse Vowels of a String
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # Convert the string to a list of characters
        n = len(s)  # Get the length of the list
        left = 0  # Initialize the left pointer
        right = n - 1  # Initialize the right pointer
        vowels = set('AEIOUaeiou')  # Define a set of vowels
        while left < right:  # Iterate through the list until the left and right pointers meet
            while left < right and s[left] not in vowels:  # Skip non-vowel characters on the left pointer
                left += 1
            while left < right and s[right] not in vowels:  # Skip non-vowel characters on the right pointer
                right -= 1
            s[left], s[right] = s[right], s[left]  # Swap the vowels at the left and right pointers
            left += 1  # Move the left pointer to the next character
            right -= 1  # Move the right pointer to the previous character
        s = ''.join(s)  # Convert the list of characters back to a string
        return s  # Return the reversed string