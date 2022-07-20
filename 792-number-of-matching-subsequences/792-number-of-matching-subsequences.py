class Solution:

    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        cnt = 0
        alp = {j : i for i,j in enumerate('abcdefghijklmnopqrstuvwxyz')}
        print(alp)
        dq = [deque() for _ in range(26)]
        for i in range(len(words)):
            c = alp[words[i][0]]
            dq[c].append([i,0])
        for c in s:
            x = alp[c]
            sz = len(dq[x])
            for _ in range(sz):
                i, j = dq[x].popleft()
                j += 1
                if len(words[i]) == j:
                    ans += 1
                else:
                    dq[alp[words[i][j]]].append([i,j])
        return ans