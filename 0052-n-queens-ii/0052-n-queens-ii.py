class Solution(object):
    def totalNQueens(self, n):
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def solve(row, board, count):
            if row == n:
                count[0] += 1
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1, board, count)

        board = [-1] * n
        count = [0]
        solve(0, board, count)
        return count[0]