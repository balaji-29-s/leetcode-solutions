class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        for ch in s:
            mp[ch]=mp.get(ch,0)+1
        for ch in t:
            mp[ch]=mp.get(ch,0)-1
        for it in mp:
            if mp[it] != 0:
                return False
        return True   