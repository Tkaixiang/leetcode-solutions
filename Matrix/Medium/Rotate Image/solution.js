// https://leetcode.com/problems/rotate-image
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

 // [[1,2,3],[4,5,6],[7,8,9]]
 // [[7,4,1],[8,5,2],[9,6,3]]

 /* 
 ===== 2 TRANSFORMATIONS =====
 1. DIAGONAL TRANSFORMATION
 [1,2,3]     [1,4,7]
 [4,5,6] --> [2,5,8]
 [7,8,9]     [3,6,9]
 2. HORIZONTAL TRANSFORMATION
 [1,4,7]     [7,4,1]
 [2,5,8] --> [8,5,2]
 [3,6,9]     [9,6,3]
 */
 var rotate = function(matrix) {
    const n = matrix.length
    // 1. Diagonal transformation
    for (let row = 0; row < n; row++) {
        for (let column = row; column < n; column++) {
            // Start from "row" so as to avoid double swapping along the diagonal axis
            if (row === column) continue
            // Swap the element at [x, y] with the element at [y, x]
            const temp = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = temp
        }
    }

    // 2. Horizontal transformation
    const half_of_n = Math.floor(n/2)
    for (let row = 0; row < n; row++) {
        for (let column = 0; column < half_of_n; column++) {
            // End at half_of_n so as to avoid double swapping along the diagonal axis
            // Swap the element at [x, y] with the element at [max_x - x, y]
            const oppositeElement = matrix[row].length - 1 - column
            const temp = matrix[row][oppositeElement]
            matrix[row][oppositeElement] = matrix[row][column]
            matrix[row][column] = temp
        }
    }

    return matrix
};