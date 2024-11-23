class Pair:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Solution:
    def isValid(self, image, row, col) -> bool:
        return True if 0 <= row < len(image) and 0 <= col < len(image[0]) else False

    def numIslands(self, grid: List[List[str]]) -> int:
        rc, cc = len(grid), len(grid[0])
        visited = [[False]* cc for _ in range(rc)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()


        island_count = 0
        for r in range(rc):
            for c in range(cc):
                if grid[r][c] == "1" and not visited[r][c]:
                    island_count += 1
                    visited[r][c] = True
                    q.append(Pair(r, c))

                    while q:
                        pair = q.popleft()
                        row, col = pair.row, pair.col
                        for i in range(4):
                            nrow, ncol = row + directions[i][0], col + directions[i][1]
                            if self.isValid(grid, nrow, ncol) and not visited[nrow][ncol] and grid[nrow][ncol] == '1':
                                visited[nrow][ncol] = True
                                q.append(Pair(nrow, ncol))
        return island_count