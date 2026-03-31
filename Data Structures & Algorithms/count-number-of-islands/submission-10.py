class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [0,1],[-1,0], [0,-1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):

            q = deque()
            grid[r][c] = "0"
            q.append([r,c])

            while q:
                rowPos, colPos = q.popleft()
                
                for x,y in directions: #bounds check
                    if (rowPos+x < rows and colPos+y < cols and rowPos+x >= 0 and colPos+y >= 0 ) and grid[rowPos + x][colPos + y] == "1":
                        grid[rowPos + x][colPos+y] = "0"
                        q.append([rowPos+x, colPos+y])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
        

        return islands