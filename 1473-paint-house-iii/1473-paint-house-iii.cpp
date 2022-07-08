class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
    int dp[101][101][21];
    memset(dp, -1, sizeof(dp));
    dp[0][0][0] = 0;
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= target; j++) {
            for (int k = 1; k <= n; k++) {
                if (k != houses[i - 1] && houses[i - 1] != 0) continue;
                for (int l = 0; l <= n; l++) {
                    int c = 0;
                    if(houses[i-1] == 0) c = cost[i-1][k-1];
                    if (k != l) {
                        if (dp[i - 1][j - 1][l] != -1 && (dp[i - 1][j - 1][l] + c < dp[i][j][k] || dp[i][j][k] == -1)) dp[i][j][k] = dp[i - 1][j - 1][l] + c;
                    }
                    else if (dp[i - 1][j][l] != -1 && (dp[i - 1][j][l] + c < dp[i][j][k] || dp[i][j][k] == -1)) dp[i][j][k] = dp[i - 1][j][l] + c;
                }
            }
        }
    }
    int answer = 1e9;
    for (int i = 1; i <= n; i++) {
        if (i != houses[m - 1] && houses[m - 1] != 0) continue;
        if (dp[m][target][i] == -1) continue;
        answer = min(answer, dp[m][target][i]);
    }
        return (answer==1e9)?-1:answer;
    }
};