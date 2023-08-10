/**
 * https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const hashTable = {}
    let output = []

    // "One-pass Hash Table" Solution
    // 1. Store the numbers into a hash table (object)
    // 2. While iterating through, find the <complement of the target value vs nums[i]>
    // 3. The complement is guarunteed to be somewhere before N iteration since a solution always exists
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if (complement in hashTable) {
            output.push(hashTable[complement])
            output.push(i)
            break
        }
        hashTable[nums[i]] = i // <---- NOTE: Need to place after to avoid nums[i] being used twice
        
    }

    return output
};