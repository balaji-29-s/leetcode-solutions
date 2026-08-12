class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<bool> used(26,false);
        string st;
        unordered_map<int,int> last;
        for(int i=0;i<s.size();i++){
            last[s[i]-'a']=i;
        }
        for(int i=0;i<s.size();i++){
            char ch=s[i];
            if(used[ch-'a']==true) continue;
            while(!st.empty()&&st.back()>ch&&last[st.back()-'a']>i){
                used[st.back()-'a']=false;
                st.pop_back();
            }
            st.push_back(ch);
            used[st.back()-'a']=true;
        }
        return st;
    }
};