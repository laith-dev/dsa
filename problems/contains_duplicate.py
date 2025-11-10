"""
- Problem:
Given an integer array nums, return true if any value appears more than
once in the array, otherwise return false.

- Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

- Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

- Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution1:
    """
    Brute force; check every possible pair.

    Complexity:
    - Time:  O(n ** 2)
    - Space: O(1)
    """

    def has_duplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == nums[i]:
                    return True
        return False


class Solution2:
    """
    Using sorting; sort numbers and check whether there are two equally
    consecutive numbers.

    Complexity:
        - Time: Python uses `Tim` sort algorithm, hence, it's O(nlogn)
        - Space: O(n).
    """

    def has_duplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


class Solution3:
    """
    Using a hash set; convert the list into a set and compare lengths.

    Complexity:
        - Time:  O(n).
        - Space: O(n).
    """

    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution4:
    """
    Using a hash set; save seen numbers and check whether a new given number
    has already been seen.

    Complexity:
        - Time:  O(n).
        - Space: O(n).
    """

    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
