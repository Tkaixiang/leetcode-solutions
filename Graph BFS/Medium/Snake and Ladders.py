# https://leetcode.com/problems/snakes-and-ladders/description/
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Map every tile into a hashmap instead
        tiles = {}
        counter = 1
        size_of_board = len(board) ** 2
        isGoingRight = True

        # =========== CREATING THE GRAPH ===========
        # Form the snakeboard into a directed graph (so we can use BFS more easily!)
        for row in range(len(board) - 1, -1, -1):
            # Alternate the direction after every row
            if isGoingRight:
                startTile = 0
                increment = 1
                endPoint = len(board[row])
                isGoingRight = False
            else:
                startTile = len(board[row]) - 1
                increment = -1
                endPoint = -1
                isGoingRight = True

            for col in range(startTile, endPoint, increment):
                current_board_tile = board[row][col]

                count_until = 6
                if counter + count_until >= size_of_board:
                    # Approaching the end
                    count_until = size_of_board - counter
                tiles[counter] = {
                    "connection": [counter + x for x in range(1, count_until + 1, 1)]
                }  # Creates an array of counter + [1..6]
                if current_board_tile != -1:
                    # We encountered either a snake or ladder at this tile, time to add in a shortcut
                    tiles[counter]["shortcut"] = current_board_tile

                counter += 1

        # =========== BFS EXPLORATION ===========
        queue_to_visit = deque(
            [(1, 0)]
        )  # Visit queue for BFS, we start with tile 1 and dice rolls 0
        visited_in_dice_rolls = {}
        while queue_to_visit:
            index_to_visit, dice_rolls = queue_to_visit.popleft()

            node = tiles[index_to_visit]
            if (
                index_to_visit not in visited_in_dice_rolls
                or dice_rolls < visited_in_dice_rolls[index_to_visit]
            ):
                # We have yet to visit the node OR, we can visit this node in LESS dice rolls!
                visited_in_dice_rolls[index_to_visit] = dice_rolls

                for connected_node_index in node["connection"]:
                    # Roll to a destination, then apply at most one snake/ladder on THAT destination
                    landing = connected_node_index
                    if "shortcut" in tiles[landing]:
                        landing = tiles[landing]["shortcut"]
                        used_shortcut = True
                    else:
                        used_shortcut = False

                    # We need to +1 even if since we HAVE YET TO INCREMENT FROM OUR CURRENT DICE POSITION
                    # So all these connections are +1
                    queue_to_visit.append((landing, dice_rolls + 1))

        return (
            visited_in_dice_rolls[size_of_board]
            if size_of_board in visited_in_dice_rolls
            else -1
        )
