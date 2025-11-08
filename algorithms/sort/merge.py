from typing import List


class MergeSort:
    @classmethod
    def sort(cls, data: List[int]) -> List[int]:
        data_len = len(data)
        if data_len <= 1:
            return data

        mid_index = data_len // 2
        left = cls.sort(data[:mid_index])
        right = cls.sort(data[mid_index:])

        return cls.merge(left, right)

    @classmethod
    def merge(cls, left: List[int], right: List[int]) -> List[int]:
        """Merges sorted lists, retaining the order."""

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            left_item = left[i]
            right_item = right[j]

            if left_item <= right_item:
                merged.append(left_item)
                i += 1
            else:
                merged.append(right_item)
                j += 1

        # Copy remaining items in left or right, if any.

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


class MergeSortInPlace:
    @classmethod
    def sort(cls, data: List[int]) -> None:
        if len(data) <= 1:
            return

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        cls.sort(left)
        cls.sort(right)

        cls.merge(data, left, right)

    @classmethod
    def merge(cls, original: List[int], left: List[int], right: List[int]) -> None:
        i = j = k = 0

        while i < len(left) and j < len(right):
            left_item = left[i]
            right_item = right[j]

            if left_item <= right_item:
                original[k] = left_item
                i += 1
            else:
                original[k] = right_item
                j += 1
            k += 1

        # Copy remaining items in left or right, if any.

        while i < len(left):
            original[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            original[k] = right[j]
            j += 1
            k += 1
