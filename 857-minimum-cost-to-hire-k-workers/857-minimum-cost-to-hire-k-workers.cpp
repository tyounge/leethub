class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<double,int>> v;
        for(int i = 0; i< wage.size();i++){
            v.push_back({(double)wage[i]/quality[i], quality[i]});
        }
        sort(v.begin(),v.end());
        priority_queue<int> pq;
        int sum = 0;
        double ans = 1e18;
        for(int i = 0;i<wage.size();i++){
            pq.push(v[i].second);
            sum += v[i].second;
            if(i >= k){
                sum -= pq.top();
                pq.pop();
            }
            if(i+1 >= k){
                ans = min(ans,v[i].first * sum);
            }
        }
        return ans;
    }
};