class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        answer = []
        alp = [0 for _ in range(26)]
        for word in words2:
            alp2 = [0 for _ in range(26)]
            for c in word:
                alp2[ord(c)-ord('a')] += 1
            for i in range(26):
                alp[i] = max(alp[i], alp2[i])

        for word in words1:
            alp2 = [0 for _ in range(26)]
            for c in word:
                alp2[ord(c) - ord('a')] += 1
            f = True
            for i in range(26):
                if alp[i] > alp2[i]:
                    f = False
                    break
            if f:
                answer.append(word)
        
        return answer