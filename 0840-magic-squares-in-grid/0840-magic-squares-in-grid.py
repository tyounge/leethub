class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        answer = 0
        for i in range(r-2):
            for j in range(c-2):
                st = set()
                f = True
                sm = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]
                if sm != grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]:
                    f = False
                for a in range(3):
                    if sm != sum(grid[i+a][j:j+3]) or sm != sum(grid[q][j+a] for q in range(i,i+3)):
                        f = False
                for a in range(3):
                    for b in range(3):
                        st.add(grid[i+a][j+b])
                if f and len(st) == 9 and min(st) == 1 and max(st) == 9:
                    answer += 1
        return answer
                
                        