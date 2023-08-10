/**
 * https://leetcode.com/problems/group-anagrams/submissions/?envType=study-plan-v2&envId=top-100-liked
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const hashTable = {}
    for (let i = 0; i < strs.length; i++) {
        // Hash = Sorted string (in alphabatical order)
        // If string[i] is an anagram of string[x], the same sorting matter will yield the same "hash"
        const sortedString = strs[i].split("").sort().join("")
        if (sortedString in hashTable) hashTable[sortedString].push(strs[i])
        else hashTable[sortedString] = [strs[i]]
    }

    const outputArray = []
    for (const sortedStr in hashTable) {
        outputArray.push(hashTable[sortedStr])
    }
    return outputArray
};