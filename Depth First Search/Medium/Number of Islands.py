class Solution:
    def exploreIsland(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        currentPlot = grid[row][col]
        if currentPlot == "0":
            return  # We reached the sea

        grid[row][col] = "0"  # DESTROY THIS PLOT OF LAND!! (We visited it basically)
        # Onwards PIRATES!
        self.exploreIsland(row - 1, col, grid)  # Down
        self.exploreIsland(row + 1, col, grid)  # Up
        self.exploreIsland(row, col + 1, grid)  # Right
        self.exploreIsland(row, col - 1, grid)  # Left

    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        for row in range(0, len(grid), 1):
            for col in range(0, len(grid[row]), 1):
                currentPlot = grid[row][col]
                if currentPlot == "1":  # We found land!
                    numIslands += 1
                    self.exploreIsland(row, col, grid)

        return numIslands
