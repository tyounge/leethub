class Solution:

    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        cnt = 0
        alp = {j : i for i,j in enumerate('abcdefghijklmnopqrstuvwxyz')}
        idx = [0 for _ in range(len(words))]
        dq = [[] for _ in range(26)]
        for i in range(len(words)):
            dq[alp[words[i][0]]].append(i)
        for c in s:
            x = alp[c]
            y = dq[x][:]
            dq[x] = []
            for i in y:
                idx[i] += 1
                j = idx[i]
                if len(words[i]) == j:
                    ans += 1
                else:
                    dq[alp[words[i][j]]].append(i)
        return ans