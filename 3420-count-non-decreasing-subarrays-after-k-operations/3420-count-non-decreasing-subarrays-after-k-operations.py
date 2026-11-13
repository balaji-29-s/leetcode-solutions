
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dq = deque()

        cost = 0
        ans = 0
        r = n - 1

        for l in range(n - 1, -1, -1):

            x = nums[l]

            cnt = 1
            total = x
            removed_cost = 0

            # Merge groups whose maximum <= x
            while dq and dq[0][0] <= x:

                mx, c, s = dq.popleft()

                removed_cost += mx * c - s

                cnt += c
                total += s

            # Update operation cost
            cost -= removed_cost
            cost += x * cnt - total

            dq.appendleft([x, cnt, total])

            # Shrink window if cost exceeds k
            while cost > k:

                last = nums[r]

                mx, c, s = dq[-1]

                cost -= mx - last

                dq[-1][1] -= 1
                dq[-1][2] -= last

                if dq[-1][1] == 0:
                    dq.pop()

                r -= 1

            # Count valid subarrays
            ans += r - l + 1

        return ans
