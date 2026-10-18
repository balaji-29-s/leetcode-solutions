class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9+7
        n=len(nums)
        comb=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            comb[i][0]=1
            comb[i][i]=1
            for j in range(1,i):
                comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%mod
        def solve(nums):
            if len(nums)<=2:
                return 1
            root=nums[0]
            left=[x for x in nums[1:] if x<root]
            right=[x for x in nums[1:]if x>root]
            leftweight=solve(left)
            rightweight=solve(right)
            interleavings=comb[len(left)+len(right)][len(left)]
            return (interleavings * leftweight * rightweight) % mod
        ans=(solve(nums)-1)%mod
        return ans