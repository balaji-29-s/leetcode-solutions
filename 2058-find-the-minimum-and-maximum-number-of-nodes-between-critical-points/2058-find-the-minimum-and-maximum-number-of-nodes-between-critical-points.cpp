/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int first=-1;
        int pos=2;
        int prevcritical=-1;
        int mindist=INT_MAX;
        int maxdist=INT_MIN;
        ListNode*prev=head;
        ListNode*curr=head->next;
        while(curr&&curr->next){
            ListNode*nextnode=curr->next;
            if((prev->val<curr->val&&nextnode->val<curr->val)||(prev->val>curr->val&&nextnode->val>curr->val)){
                if(first==-1){
                    first=pos;
                }
                if(prevcritical!=-1){
                    mindist=min(mindist,pos-prevcritical);
                }
                prevcritical=pos;
            }
            prev=curr;
            curr=nextnode;
            pos++;
        }
        if(first==-1||prevcritical==first){
            return {-1,-1};
        }
        maxdist=prevcritical-first;
        return {mindist,maxdist};
    }
};