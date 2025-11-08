from collections import Counter

"""
- Problem:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

- Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

- Example 2:
Input: nums = [1], k = 1
Output: [1]

- Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

- Constraints:
1 <= nums.length <= 10 ** 5
-10 ** 4 <= nums[i] <= 10 ** 4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


class Solution1:
    """
    Count each number, sort based on the count and return the first `k` numbers.

    Complexity:
    - Time:  O(nlogn)
    - Space: O(n)
    """

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        counts_sorted = sorted(counts, key=lambda num: counts[num], reverse=True)
        return counts_sorted[:k]
