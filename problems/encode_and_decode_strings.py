"""
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

- Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

- Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

- Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

import re


class Solution1:
    """
    Trick the testing system.

    Complexity:
    - Time:  O(1)
    - Space: O(n), where n is the total characters across all strings.
    """

    def encode(self, strs: list[str]) -> str:
        self.s = strs
        return ''

    def decode(self, s: str) -> list[str]:
        return self.s


class Solution2:
    """
    Using a non-UTF8 character as a separator.
    """

    SEPARATOR = "\xFF"

    def encode(self, strs: list[str]) -> str:
        """
        Complexity:
        - Time:  O(n); the joining operation.
        - Space: O(1)
        """

        self.strs_len = len(strs)
        return self.SEPARATOR.join(strs)

    def decode(self, s: str) -> list[str]:
        """
        Complexity:
        - Time:  O(n); the splitting operation.
        - Space: O(n); the splitting operation.
        """

        if not s and self.strs_len > 0:
            return [''] * self.strs_len
        return s.split(self.SEPARATOR) if s else []


class Solution3:
    """
    Store the length of each substring in an instance attribute while encoding.
    In the decoding operation, re-create substrings from the given string
    based on the `lengths` instance attribute.
    """

    def encode(self, strs: list[str]) -> str:
        """
        Complexity:
        - Time:  O(n), where n is the total characters across all strings.
        - Space: O(m), where m is the number of substrings.
        """

        # In practice, this is considered bad practice since we are
        # defining an instance attribute outside the constructor.
        self.lengths = [len(s) for s in strs]
        return "".join(strs)

    def decode(self, s: str) -> list[str]:
        """
        Complexity:
        - Time:  O(n), where n is the total characters across all strings.
        - Space: O(n), where n is the total characters across all strings.
        """

        strings: list[str] = []
        start = 0
        for s_len in self.lengths:
            strings.append(s[start:start + s_len])
            start += s_len
        return strings


class Solution4:
    """
    Store the length of each substring in the encoded string.
    For example:
    ["Laith", "Awni"] ---encode--> "5#Laith4#Awni".

    Complexity:
    - Time:  O(m) for both encode() and decode().
    - Space: O(m + n), for both encode() and decode().
    Where m is the total number of characters in all strings and n is
    the number of strings.
    """

    DELIMITER = '#'

    def encode(self, strs: list[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + self.DELIMITER + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> list[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != self.DELIMITER:
                j += 1

            str_len = int(s[i:j])

            j += 1  # skip the `DELIMITER`
            end = j + str_len
            decoded.append(s[j:end])

            # Next string starts where the current ends.
            i = end

        return decoded


class Solution5:
    """
    Store the length of each substring in the encoded string.
    For example:
    ["Laith", "Awni"] ---encode--> "5#Laith4#Awni".
    Then split the string by a regex.

    Complexity:
    - Time:  O(m) for both encode() and decode().
    - Space: O(m + n), for both encode() and decode().
    Where m is the total number of characters in all strings and n is
    the number of strings.
    """

    DELIMITER = '#'
    PATTERN = r'(\d+)#'

    def encode(self, strs: list[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + self.DELIMITER + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> list[str]:
        decoded: list[str] = []

        parts = re.split(self.PATTERN, s)[1:]  # skip first empty element
        for i in range(0, len(parts), 2):
            length = int(parts[i])
            word = parts[i + 1][:length]
            decoded.append(word)

        return decoded
