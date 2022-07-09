class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        priority_queue<int> q1, q2;
        vector<int> v;
        v.push_back(nums[0]);
        q1.push(nums[0]);
        for(int i=1;i<nums.size();i++){
            if(i>k) q2.push(v[i-k-1]);
            while(!q2.empty() && q1.top() == q2.top()){
                q1.pop();
                q2.pop();
            }
            v.push_back(q1.top() + nums[i]);
            q1.push(v.back());
        }
        return v.back();
    }
};