class Solution:

    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        cnt = 0
        a = ord('a')
        dq = [deque() for _ in range(26)]
        for i in range(len(words)):
            c = ord(words[i][0]) - a
            dq[c].append([i,0])
        for c in s:
            x = ord(c) - a
            sz = len(dq[x])
            for _ in range(sz):
                i, j = dq[x].popleft()
                j += 1
                if len(words[i]) == j:
                    ans += 1
                else:
                    dq[ord(words[i][j]) - a].append([i,j])
        return ans