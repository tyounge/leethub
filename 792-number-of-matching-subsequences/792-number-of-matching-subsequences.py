class Solution:

    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def chk(v, word):
            x = len(v)-1
            for c in word:
                x = v[x][ord(c)-ord('a')]
                if x == -1:
                    return False
            return True
        v = [[-1 for _ in range(26)] for _ in range(len(s)+1)]
        now = [-1 for _ in range(26)]
        for i, j in enumerate(reversed(s)):
            for k in range(26):
                v[i][k] = now[k]
            now[ord(j) - ord('a')] = i
        for i in range(26):
            v[len(s)][i] = now[i]
        ans=0
        for word in words:
            if chk(v, word):
                ans += 1
        return ans