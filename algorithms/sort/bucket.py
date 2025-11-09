class BucketSort:
    @staticmethod
    def sort(nums: list[int]) -> list[int]:
        if not nums:
            return nums

        n = len(nums)
        size = max(nums) / n
        buckets = [[] for _ in range(n)]

        for num in nums:
            index = int(num / size)
            index = index if index < n else n - 1
            buckets[index].append(num)

        for i in range(len(buckets)):
            buckets[i] = sorted(buckets[i])

        nums_sorted: list[int] = []
        for bucket in buckets:
            for num in bucket:
                nums_sorted.append(num)

        return nums_sorted


class BucketSortInPlace:
    @staticmethod
    def sort(nums: list[int]) -> None:
        if not nums:
            return

        n = len(nums)
        size = max(nums) / n
        buckets = [[] for _ in range(n)]

        for num in nums:
            index = int(num / size)
            index = index if index < n else n - 1
            buckets[index].append(num)

        for i in range(len(buckets)):
            buckets[i] = sorted(buckets[i])

        i = 0
        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1
