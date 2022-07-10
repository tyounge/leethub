class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int x[2] = {0,0};
        for(int i = 2 ;i<=n;i++){
            if(i&1){
                x[1] = min(x[0]+cost[i-1], x[1]+cost[i-2]);
            }
            else{
                x[0] = min(x[0]+cost[i-2], x[1]+cost[i-1]);
            }
        }
        return x[n&1];
    }
};