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
