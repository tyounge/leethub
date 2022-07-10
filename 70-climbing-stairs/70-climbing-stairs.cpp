class Solution {
public:
    int climbStairs(int n) {
        int x[2] = {1,0};
        for(int i=1;i<=n;i++){
            x[i&1] = x[0] + x[1];
        }
        return x[n&1];
    }
};