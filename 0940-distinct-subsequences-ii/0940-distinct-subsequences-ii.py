class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        last={}
        dp=[0]*(len(s)+1)
        dp[0]=1
        for i in range(1,len(s)+1):
            ch=s[i-1]
            dp[i]=2*dp[i-1]
            if ch in last:
                dp[i]-=dp[last[ch]-1]
            last[ch]=i
            dp[i]%=MOD
        return (dp[len(s)]-1)%MOD