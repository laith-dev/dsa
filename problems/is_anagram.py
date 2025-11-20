"""
- Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

- Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

- Example 2:
Input: s = "rat", t = "car"
Output: false

- Constraints:
1 <= s.length, t.length <= 5 * 10 ** 4
s and t consist of lowercase English letters.
"""

from collections import Counter


class Solution1:
    """
    Brute force; compare the sorted version of each string.

    Complexity:
    - Time:  O(nlogn + mlogm) where n and m are the lengths of s and t respectively.
    - Space: O(n + m) where n and m are the lengths of s and t respectively.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution2:
    """
    Using hash tables; count each character in `s` then for each character in `t`, if it
    doesn't exist in `s` or its count is 0, then they are not anagrams.

    Complexity:
    - Time:  O(n)
    - Space: O(k), where k is the number of unique characters in `s`.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)

        for char in t:
            if char not in s_counter or s_counter[char] == 0:
                return False
            s_counter[char] -= 1

        return True


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution4:
    """
    Complexity:
    - Time:  O(n)
    - Space: O(1)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
