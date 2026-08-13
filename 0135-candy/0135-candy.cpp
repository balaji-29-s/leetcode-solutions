class Solution {
public:
    int candy(vector<int>& ratings) {
        int candies=1;
        int i=1;
        int n=ratings.size();
        while(i<n){
            if(ratings[i]==ratings[i-1]){
                candies++;
                i++;
                continue;
            }
            int peak=1;
            while(i<n&&ratings[i]>ratings[i-1]){
                peak++;
                candies+=peak;
                i++;
            }
            int down=1;
            while(i<n&&ratings[i]<ratings[i-1]){
                candies+=down;
                down++;
                i++;
            }
            if(peak<down){
                candies+=(down-peak);
            }
        }
        return candies;
    }
};