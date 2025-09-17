# https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def can_capture(self, row, col, board, is_explored, land_indexes):
        # We went out of bounds, that means it is a false as well
        # if (row < 0 or col < 0 or row >= len(board) or col >= len(board[row]))):
        #     return False

        cell = board[row][col]
        if row <= 0 or col <= 0 or row >= len(board) - 1 or col >= len(board[row]) - 1:
            # We reached the border regions
            if cell == "O":  # O on the border, we can't surround this region
                return False
            else:
                return True

        if cell != "O":
            return True  # Reached "X"
        if is_explored[row][col]:
            return True  # Explored this before

        is_explored[row][col] = True
        land_indexes.append((row, col))
        # If any branches return False, it means we can't surround
        up = self.can_capture(row + 1, col, board, is_explored, land_indexes)
        down = self.can_capture(row - 1, col, board, is_explored, land_indexes)
        right = self.can_capture(row, col + 1, board, is_explored, land_indexes)
        left = self.can_capture(row, col - 1, board, is_explored, land_indexes)
        return up and down and right and left

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        is_explored = [[False] * len(board[0]) for x in range(len(board))]

        for row in range(0, len(board), 1):
            for col in range(0, len(board[row]), 1):
                cell = board[row][col]
                if cell == "O":
                    land_indexes = []
                    # Found possible region to capture, AHOY!
                    if self.can_capture(row, col, board, is_explored, land_indexes):
                        for cell_to_remove in land_indexes:
                            row_x, col_x = cell_to_remove
                            board[row_x][col_x] = "X"
