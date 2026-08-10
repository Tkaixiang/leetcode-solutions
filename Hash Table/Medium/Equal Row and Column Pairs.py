# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # - Iterate rows and cols
        # - Create hash map of col string -> col index
        #   - Create row hashes [3,2,1]
        #   - Create col hashes [3,1,2]
        # - Iterate row hashes, for matching rows against cols:
        #   - Add pairs "unique matching_pairs" (deduplicates repeat pairs)
        # - Count num unique pairs lastly
        
        matching_pairs = {}
        col_hashes = {} # Row hash [1,1,1] -> Cols

        # Create col hashes
        for col in range(len(grid)):
            complete_col = []
            for row in range(len(grid)):
                complete_col.append(grid[row][col])
            
            col_hash = str(complete_col)
            if col_hash in col_hashes:
                col_hashes[col_hash].append(col)
            else:
                col_hashes[col_hash] = [col]
        
        # Iterate row-by-row, compute hash and search for matching hashes
        for row in range(len(grid)):
            current_row = grid[row]
            row_hash = str(current_row)
            if row_hash in col_hashes:
                # Match found!
                for col_index in col_hashes[row_hash]:
                    pair_hash = str([row,col_index]) # -> [row, col] standardised
                    matching_pairs[pair_hash] = 1 # De-duplicates (row,col pairs)

        return len(matching_pairs)


