/**
 * https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const spiral_order = []
    const rows = matrix.length
    const cols = matrix[0].length
    const totalElements = rows * cols
    let rowPointer = 0
    let colPointer = 0
    
    let direction = "right"

    // Proceed in X direction until hit boundary/hit a visited element
    while (true) {
        spiral_order.push(matrix[rowPointer][colPointer])
        matrix[rowPointer][colPointer] = false // mark element as visited

        if (spiral_order.length === totalElements) break
        
        if (direction === "up" && matrix[rowPointer-1][colPointer] === false) {
            direction = "right"
        }
        else if (direction === "right") {
            if (colPointer+1 === cols || matrix[rowPointer][colPointer+1] === false) direction = "down"
        }
        else if (direction === "down") {
            if (rowPointer+1 === rows || matrix[rowPointer+1][colPointer] === false) direction = "left"
        }
        else if (direction === "left") {
            if (colPointer === 0 || matrix[rowPointer][colPointer-1] === false) direction = "up"
        }

        if (direction === "right") colPointer += 1
        else if (direction === "down") rowPointer += 1
        else if (direction === "up") rowPointer -= 1
        else colPointer -= 1
    }
    
    return spiral_order
};