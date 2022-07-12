class Solution:
    def makesquare(self, matchsticks) -> bool:
        x = [0, 0, 0, 0]
        matchsticks.sort(reverse = True)
        global k
        k = sum(matchsticks)//4
        if k * 4 != sum(matchsticks):
            return False
        def chk():
            global k
            for i in x:
                if i != k:
                    return False
            return True
        def dfs(n):
            global k
            if n == len(matchsticks):
                return chk()
            for i in range(4):
                if x[i] + matchsticks[n] > k:
                    continue
                x[i] += matchsticks[n]
                if dfs(n+1):
                    return True
                x[i] -= matchsticks[n]
                if x[i] == 0:
                    break
            return False
        
        return dfs(0)
                