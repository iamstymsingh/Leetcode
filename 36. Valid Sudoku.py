class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = collections.defaultdict(set)
        cset = collections.defaultdict(set)
        sset = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in rset[i] or board[i][j] in cset[j] or board[i][j] in sset[(i//3, j//3)]:
                        return False
                rset[i].add(board[i][j])
                cset[j].add(board[i][j])
                sset[(i//3, j//3)].add(board[i][j])
        return True