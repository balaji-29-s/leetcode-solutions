class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n=nums.size();
        int mini=INT_MAX;
        int maxi=INT_MIN;
        int mn;
        int mx;
        for(int i=0;i<n;i++){
            if(nums[i]<mini){
                mini=nums[i];
                mn=i;
            }
            if(nums[i]>maxi){
                maxi=nums[i];
                mx=i;
            }
        }
        int left=min(mn,mx);
        int right=max(mn,mx);
        int front=right+1;
        int rear=n-left;
        int both=left+1+(n-right);
        return min(front,min(rear,both));
    }
};