from collections import deque

class Pair:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

class Solution:
    def isValid(self, image, row, col) -> bool:
        return True if 0 <= row < len(image) and 0 <= col < len(image[0]) else False

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rc, cc = len(image), len(image[0])
        visited = [[False]* cc for _ in range(rc)]

        current_color = image[sr][sc]
        image[sr][sc] = color
        visited[sr][sc] = True

        q = deque()
        q.append(Pair(sr, sc, current_color))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            pair = q.popleft()
            row, col, cell_color = pair.row, pair.col, pair.color

            for i in range(4):
                nrow, ncol = row + directions[i][0], col + directions[i][1]
                if self.isValid(image, nrow, ncol) and not visited[nrow][ncol] and image[nrow][ncol] == cell_color:
                    image[nrow][ncol] = color
                    visited[nrow][ncol] = True
                    q.append(Pair(nrow, ncol, cell_color))
                
        return image
