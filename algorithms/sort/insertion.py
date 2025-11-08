from typing import List


class InsertionSort:
    @classmethod
    def sort(cls, data: List[int]) -> List[int]:
        data_len = len(data)
        if data_len <= 1:
            return data

        data = data[:]
        for i in range(1, data_len):
            item = data[i]
            while i > 0 and item < data[i - 1]:
                data[i] = data[i - 1]
                i -= 1
            data[i] = item

        return data


class InsertionSortInPlace:
    @classmethod
    def sort(cls, data: List[int]) -> None:
        data_len = len(data)
        if data_len <= 1:
            return

        for i in range(1, data_len):
            item = data[i]
            while i > 0 and item < data[i - 1]:
                data[i] = data[i - 1]
                i -= 1
            data[i] = item
