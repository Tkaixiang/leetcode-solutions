/**
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */

// Sliding Window
// p = Anagram target [Length of all anagram strings]
var findAnagrams = function (s, p) {
    let anagramStarts = []

    let pObj = {}
    // Map p into an object
    for (let i = 0; i < p.length; i++) {
        if (p[i] in pObj) pObj[p[i]] += 1
        else pObj[p[i]] = 1
    }

    let currentSubString = {} // to ensure all characters are unique
    let currentSubStringSlice = ""
    for (let i = 0; i < s.length; i++) {
        if (s[i] in pObj) { 
            // Ensures that our "Sliding Window" always has VALID chars + RIGHT NUMBER of chars

            if (s[i] in currentSubString) { // Duplicate character
                if (currentSubString[s[i]] >= pObj[s[i]]) {
                    // Valid char > amount we need, restrict sliding window to discard previous repeated char
                    const foundIndex = currentSubStringSlice.indexOf(s[i])
                    // Remember to update our currentSubString counter as well before slicing off currentSubStringSlice
                    for (let x = 0; x < foundIndex; x++) {
                        currentSubString[currentSubStringSlice[x]] -= 1
                    }
                    currentSubStringSlice = currentSubStringSlice.slice(foundIndex + 1)
                }
                else currentSubString[s[i]] += 1 // We still need more of this char
            }
            else currentSubString[s[i]] = 1 

            currentSubStringSlice += s[i]
            if (currentSubStringSlice.length === p.length) anagramStarts.push(i - p.length + 1)
        }
        else {
            // Reset everything if invalid char encountered
            currentSubString = {}
            currentSubStringSlice = ""
        }

        

    }
    return anagramStarts
};