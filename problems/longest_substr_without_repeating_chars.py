"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous non-empty sequence of characters within a string.

- Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

- Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

- Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

- Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution1:
    """
    Complexity:
    - Time:  O(n ** 3)
    - Space: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        longest_start_index = 0

        temp = ''
        index = 0
        while len(s) > index:
            char = s[index]
            if char not in temp:
                temp += char
                index += 1
            else:
                if len(temp) > len(longest):
                    longest = temp
                    if longest_start_index:
                        longest_start_index = index

                    index = longest_start_index + 1
                else:
                    index = index - len(temp) + 1

                temp = ''

        if len(temp) > len(longest):
            longest = temp

        return len(longest)


class Solution2:
    """
    Complexity:
    - Time:  O(n ** 2)
    - Space: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        temp = ''
        for index in range(len(s)):
            for sub_index in range(index, len(s)):
                char = s[sub_index]
                if char not in temp:
                    temp += char
                else:
                    if len(temp) > len(longest):
                        longest = temp
                    temp = ''
                    break

        if not longest:
            longest = temp

        return len(longest)
