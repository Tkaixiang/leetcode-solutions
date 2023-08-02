/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 * https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/?envType=study-plan-v2&envId=top-100-liked
 */
var searchMatrix = function(matrix, target) {
    // Start at top right
    rowPointer = 0
    colPointer = matrix[0].length - 1
    while (true) {
        const current = matrix[rowPointer][colPointer]
        if (current === target) return true
        
        // Discard current COLUMN
        // Everything down this column > target (and we have searched everything above of this element in the col),
        // hence this column does not contain our target
        if (target < current) colPointer -= 1 
        // Discard current ROW
        // Everything before this row < target (and we have searched everything right of this element in the row),
        // hence this column does not contain our target
        else if (target > current) rowPointer += 1

        if (colPointer < 0 || rowPointer < 0 || colPointer >= matrix[0].length || rowPointer >= matrix.length) break
        
    }

    return false
};