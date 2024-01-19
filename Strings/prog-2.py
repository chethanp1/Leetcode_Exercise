# 242. Valid Anagram
# # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# # # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        # Count the frequency of characters in string s
        for x in s:
            count[ord(x) - ord('a')] += 1

        # Decrement the frequency of characters in string t
        for x in t:
            count[ord(x) - ord('a')] -= 1

        # Check if any character has non-zero frequency
        for val in count:
            if val != 0:
                return False

        return True