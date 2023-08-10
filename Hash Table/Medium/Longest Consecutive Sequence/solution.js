/**
 * https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function (nums) {
    const hashTable = new Set(nums) // O(n) to map it at the start
    let largestSequence = 0

    // REMEMBER: O(3n) === O(n) since CONSTANT FACTORS are ignored in Big O Notation
    for (let i = 0; i < nums.length; i++) {
        // Trick: Only iterate to find the longest streak at the begining of a streak
        if (!(hashTable.has(nums[i] - 1))) {
            let tempNum = nums[i]
            let currentSequence = 1
            while (true) {
                tempNum += 1
                if (hashTable.has(tempNum)) currentSequence += 1
                else break
            }

            if (currentSequence > largestSequence) largestSequence = currentSequence
        }
    }

    return largestSequence
};