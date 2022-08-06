class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        answer = 0
        cnt = minutesToTest//minutesToDie + 1
        while cnt ** answer < buckets:
            answer += 1
        return answer