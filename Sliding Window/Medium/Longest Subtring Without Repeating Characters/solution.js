/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/?envType=study-plan-v2&envId=top-100-liked
 * @param {string} s
 * @return {number}
 */

var lengthOfLongestSubstring = function (s) {
    let left = 0
    let right = 0
    let characterSet = {}
    let longestLength = 0

    // "Sliding Window"
    for (let i = 0; i < s.length; i++) {
        if (s[i] in characterSet) {
            if (characterSet[s[i]] >= left) left = characterSet[s[i]] + 1
            // When a repeated character is found:
            // 1. Move sliding window left-pointer to +1 of the (previous) repeated character
            // 2. Update that character's pointer to new character's pointer (see below)
            
            /* 
            CATCH 22: By right we should drop everything LEFT of the repeated char
            But this is SLOW. Instead, we can check if the PREVIOUS repeated char is "invalid"
            and ignore it if it is not "within the Sliding Window"
            */
        }
        right = i 
        characterSet[s[i]] = i // Update character pointer

        const newLength = right - left + 1
        if (newLength > longestLength) longestLength = newLength
    }


    return longestLength
};