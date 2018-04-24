import collections

class Solution:
    # BFS 广度优先搜索
    def solve(self, board):
        # 构建队列
        queue = collections.deque([])
        # 搜索最外围的 “O”，添加到队列中
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            # 逐层向里搜索，如果与 ‘O’连通，则标记为“D”
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))

        # 已标记为D的，变换为O，其余的变换为X
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
        return board


class Solution2:
    # BFS
    def solve(self, board):
        queue = collections.deque([])
        # height, weight = len(board), len(board[0])
        # 把最外层的“O”添加到队列中
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == 'O':
                    queue.append([i, j])
        print(queue)
        # BFS
        while queue:
            i, j = queue.popleft()
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'D'
                queue.append([i + 1, j])
                queue.append([i, j + 1])
                queue.append([i - 1, j])
                queue.append([i, j - 1])

        # 标识
        #"""
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'
        #"""
def foo():
    solution = Solution2()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(solution.solve(board))
if __name__ == '__main__':
    foo()