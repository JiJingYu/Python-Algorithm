import numpy as np

from copy import copy


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs()
        print(board)
        print("hello, world")
        # board[:] = self.board[0]

    def validSudoku(self, board, i, j):
        for k in range(9):
            if (j != k and board[i][j] == board[i][k]) or (i != k and board[i][j] == board[k][j]):
                return False
        for c1 in range(3):
            for c2 in range(3):
                if (i // 3 * 3 + c1 != i or j // 3 * 3 + c2 != j) and board[i][j] == board[i // 3 * 3 + c1][
                                            j // 3 * 3 + c2]:
                    return False
        return True

    def dfs(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    for k in range(1, 10):
                        self.board[i][j] = str(k)
                        if self.validSudoku(self.board, i, j) and self.dfs():
                            return True
                        self.board[i][j] = '.'
                    return False
        return True


def foo():
    solution = Solution()
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    solution.solveSudoku(board)
    print(np.array(solution.board))
    # print(np.array(solveNQueens(8)))


if __name__ == '__main__':
    foo()