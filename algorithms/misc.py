def longest_common_subsequence(s1: str, s2: str) -> int:
    """
    Find and return the length of the Longest Common Subsequence
    between `str1` and `str2`.

    A subsequence of a string is a new string generated from
    the original string with some (or none) characters deleted
    without changing the relative order of the remaining characters.
    For example, `ace` is a subsequence of 'abcde'.

    This solution uses a 2D Dynamic Programming approach.

    Check out this YouTube video for the explanation:
    https://www.youtube.com/watch?v=Ua0GhsJSlWM
    """
    # n * m matrix where n is len(s1) and m is len(s2).
    matrix = [
        [0 for _ in range(len(s2) + 1)]
        for _ in range(len(s1) + 1)
    ]

    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                matrix[i][j] = 1 + matrix[i + 1][j + 1]
            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])

    return matrix[0][0]
