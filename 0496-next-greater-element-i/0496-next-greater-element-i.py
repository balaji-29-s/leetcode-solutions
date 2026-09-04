class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        mp={}
        ans=[]
        for i in range (len(nums2)-1,-1,-1):
            while st and st[-1]<nums2[i]:
                st.pop()
            mp[nums2[i]]=-1 if not st else st[-1]
            st.append(nums2[i])
        for i in nums1:
            ans.append(mp[i])

        return ans