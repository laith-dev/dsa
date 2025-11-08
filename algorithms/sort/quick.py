from typing import List


class QuickSort:
    @classmethod
    def sort(cls, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data

        smaller, equal, greater = [], [], []
        pivot = data[-1]
        for item in data:
            if item < pivot:
                smaller.append(item)
            elif item == pivot:
                equal.append(item)
            else:
                greater.append(item)

        return cls.sort(smaller) + equal + cls.sort(greater)


class QuickSortInPlace:
    @classmethod
    def sort(cls, data: List[int], low: int = None, high: int = None) -> None:
        if low is None:
            low = 0
        if high is None:
            high = len(data) - 1

        if low < high:
            pivot_index = cls.partition(data, low, high)
            cls.sort(data, low, pivot_index - 1)
            cls.sort(data, pivot_index + 1, high)

    @classmethod
    def partition(cls, data: List[int], low: int, high: int) -> int:
        pivot = data[high]

        # Greater item pointer.
        i = low
        for j in range(low, high):
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1

        data[i], data[high] = data[high], data[i]

        return i
