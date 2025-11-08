from typing import List


class LinearSearch:
    @classmethod
    def search(cls, nums: List[int], key: int) -> int:
        for index, num in enumerate(nums):
            if key == num:
                return index
        return -1
