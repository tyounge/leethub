class Solution:

    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        cnt = 0
        alp = {j : i for i,j in enumerate('abcdefghijklmnopqrstuvwxyz')}
        idx = [0 for _ in range(len(words))]
        dq = [deque() for _ in range(26)]
        for i in range(len(words)):
            dq[alp[words[i][0]]].append(i)
        for c in s:
            x = alp[c]
            for _ in range(len(dq[x])):
                i = dq[x].popleft()
                idx[i] += 1
                j = idx[i]
                if len(words[i]) == j:
                    ans += 1
                else:
                    dq[alp[words[i][j]]].append(i)
        return ans