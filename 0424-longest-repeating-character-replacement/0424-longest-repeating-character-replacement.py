class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        maxfreq=0
        mp={}
        maxlen=1
        while right<len(s):
            mp[s[right]]=mp.get(s[right],0)+1
            maxfreq=max(maxfreq,mp[s[right]])
            if (right-left+1)-maxfreq>k:
                mp[s[left]]=mp.get(s[left],0)-1
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen