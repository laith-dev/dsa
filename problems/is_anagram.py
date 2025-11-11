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


class Solution1:
    """
    Brute force; compare the sorted version of each string.

    Complexity:
        - Time:  O(nlogn + mlogm) where n and m are the lengths of s and t respectively.
        - Space: O(n + m) where n and m are the lengths of s and t respectively.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
