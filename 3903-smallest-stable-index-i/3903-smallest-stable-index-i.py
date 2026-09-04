class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        ans=-1
        for i in range(n):
            mini=min(nums[i:])
            maxi=max(nums[0:i+1])
            if maxi-mini<=k and i<n:
                ans=i
                break
        return ans
