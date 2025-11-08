from typing import List


class BinarySearch:
    @classmethod
    def recursive(cls, nums: List[int], key: int, low: int = None, high: int = None) -> int:
        if low is None:
            low = 0
        if high is None:
            high = len(nums) - 1

        if low > high:
            return -1

        mid = low + (high - low) // 2  # safer than (high + low) // 2
        current = nums[mid]
        if key == current:
            return mid
        elif key > current:
            return cls.recursive(nums, key, mid + 1, high)
        else:
            return cls.recursive(nums, key, low, mid - 1)

    @classmethod
    def iterative(cls, nums: List[int], key: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2  # safer than (high + low) // 2
            current = nums[mid]
            if key == current:
                return mid
            elif key > current:
                low = mid + 1
            else:
                high = mid - 1
        return -1
