class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)
        if n == '9'*len(n):
            return '1' + '0' * (len(n)-1) + '1'
        if n <= '1' + '0' * (len(n)-2) + '1':
            return '9' * (len(n)-1)
        
        n = [int(i) for i in n]
        
        sml = [0] * len(n)
        s = 0
        e = len(n)-1
        while s <= e:
            for i in range(9):
                sml[s] += 1
                if s != e:
                    sml[e] += 1
                if sml >= n:
                    sml[s] -= 1
                    if s!= e:
                        sml[e] -=1
                    break
            s += 1
            e -= 1
        
        bg = [9] * len(n)
        s = 0
        e = len(n) - 1
        while s <= e:
            for i in range(9):
                bg[s] -= 1
                if s != e:
                    bg[e] -= 1
                if bg <= n:
                    bg[s] += 1
                    if s!=e:
                        bg[e] += 1
                    break
            s += 1
            e -= 1
            
        n = ''.join([str(i) for i in n])
        sml = ''.join([str(i) for i in sml])
        bg = ''.join([str(i) for i in bg])
        
        
        if int(bg) - int(n) < int(n) - int(sml):
            return bg
        return sml