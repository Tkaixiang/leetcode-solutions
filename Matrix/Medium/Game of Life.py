class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # <2 neighbours: Live -> Die
        # (Live) 2-3 Neighbours: Live
        # >3 Neighbours: Live -> Die
        # (Dead) 3 Neighbours: Die -> Live

        # IN-PLACE EDIT SOLUTION:
        # 0 -> Was dead, still dead
        # 1 -> Was alive, still alive
        # 2 -> Was Dead, now alive
        # 3 -> Was alive, now dead

        for row in range(0, len(board), 1):
            for col in range(0, len(board[row]), 1):
                # Go through neighbours of this cell - return the number of alive cells
                # =============================================
                # This should technically be abstracted to a method
                # However, doing so fails Leetcode's memory rankings lmao
                num_neighbours = 0
                for x in range(max(row-1, 0), min(row+2, len(board)), 1):
                    for y in range(max(col-1, 0), min(col+2, len(board[0])), 1):
                        if (x == row and y == col):
                            continue # Skip current cell
                        if (board[x][y] == 1 or board[x][y] == 3):
                            num_neighbours += 1
                # =============================================

                if board[row][col] == 1: # Cell is alive
                    if (num_neighbours > 3 or num_neighbours < 2):
                        board[row][col] = 3 # Was alive, now dead
                else: # Cell is dead
                    if num_neighbours == 3:
                        board[row][col] = 2 # Was dead, now alive
        
        # Now replace 2 and 3 states with their final states
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 3:
                    board[row][col] = 0
        
                 


        
