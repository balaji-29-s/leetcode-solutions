class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        sort(nums.begin(),nums.end());
        int maxlen=1;
        int n=nums.size();
        int len=1;
        for(int i=n-2;i>=0;i--){
            if(nums[i+1]==nums[i]){
                continue;
            }
            else if(nums[i]+1==nums[i+1]){
                len++;
            }
            else{
                len=1;
            }
            maxlen=max(len,maxlen);
        }
        return maxlen;
    }
};