class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        cnt = 0
        num = 0
        arr2 = []
        for i in arr:
            if num != i:
                arr2.append(cnt)
                num = i
                cnt = 1
            else:
                cnt += 1
        arr2.append(cnt)
        cnt+= 1
        num = i
        arr2.sort()
        sum = len(arr)
        half = len(arr)//2
        answer = 0
        while True:
            sum -= arr2.pop()
            answer += 1
            if sum <= half:
                return answer
            
            