class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for right in range(l, n + 1):
            for length in range(l, r + 1):
                left = right - length

                if left < 0:
                    continue

                curr_sum = prefix[right] - prefix[left]

                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float('inf') else -1