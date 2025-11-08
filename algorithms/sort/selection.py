from typing import List


class SelectionSort:
    @classmethod
    def sort(cls, nums: List[int]) -> List[int]:
        sorted_nums = []
        nums_copy = nums[:]
        while nums_copy:
            minimum = min(nums_copy)
            sorted_nums.append(minimum)
            nums_copy.remove(minimum)
        return sorted_nums


class SelectionSortInPlace:
    @classmethod
    def sort(cls, nums: List[int]) -> None:
        nums_len = len(nums)
        for i in range(nums_len):
            minimum_index = i
            for j in range(i + 1, nums_len):
                if nums[j] < nums[minimum_index]:
                    minimum_index = j
            nums[i], nums[minimum_index] = nums[minimum_index], nums[i]
