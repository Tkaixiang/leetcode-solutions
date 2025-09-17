# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])

        visited = [
            [False] * width for _ in range(height)
        ]  # We need to use for for operator here to make DEEP COPIES
        numElements = height * width
        elements = []
        row = 0
        col = 0
        nextDirection = "right"

        counter = 0
        while counter < numElements:
            visited[row][col] = True
            elements.append(matrix[row][col])
            counter += 1

            if nextDirection == "right":
                # Check if we will go out of bounds or next element is visited
                nextCol = col + 1
                if nextCol >= width or visited[row][nextCol]:
                    # Change to down
                    nextDirection = "down"
                    row += 1
                else:
                    col = nextCol
            elif nextDirection == "down":
                nextRow = row + 1
                if nextRow >= height or visited[nextRow][col]:
                    nextDirection = "left"
                    col -= 1
                else:
                    row = nextRow
            elif nextDirection == "left":
                nextCol = col - 1
                if nextCol < 0 or visited[row][nextCol]:
                    nextDirection = "up"
                    row -= 1
                else:
                    col = nextCol
            else:  # up
                nextRow = row - 1
                if nextRow < 0 or visited[nextRow][col]:
                    nextDirection = "right"
                    col += 1
                else:
                    row = nextRow
        return elements
