/**
 * https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-100-liked
 * @param {string} s
 * @param {string} t
 * @return {string}
 */

var minWindow = function (s, t) {
    let subStringSlice = ""
    let subStringCounter = {}
    let fullTCounter = {}

    // Map t into an object
    for (let i = 0; i < t.length; i++) {
        if (t[i] in fullTCounter) fullTCounter[t[i]] += 1
        else fullTCounter[t[i]] = 1
    }
    

    let minSubString = ""
    let minSubStringLength = Infinity // We need the initial length to be very large (while still maintaining the initial best solution is an empty string "")
    let requiredCharsCount = 0 
    // OPTIMISATION: Use a counter to keep track of required characters instead of checking subStringCounter on every iteration
    for (let i = 0; i < s.length; i++) {
        subStringSlice += s[i]

        // Encountered a required character (of t)
        if (s[i] in fullTCounter) {
            if (s[i] in subStringCounter) {
                subStringCounter[s[i]] += 1
                if (subStringCounter[s[i]] <= fullTCounter[s[i]]) requiredCharsCount += 1
            }
            else {
                subStringCounter[s[i]] = 1
                requiredCharsCount += 1
            }


            // Check if we have all the characters required
            if (requiredCharsCount === t.length) {
                let finalSliceValue = 0

                
                // 1. Try to reduce window size from the left
                // 2. Check every time we encounter a required character (of t)
                // 3. Break if removing that character leads to an invalid sub-string
                for (let x = 0; x < subStringSlice.length; x++) {
                    if (subStringSlice[x] in fullTCounter) {
                        if (subStringCounter[subStringSlice[x]] <= fullTCounter[subStringSlice[x]]) requiredCharsCount -= 1
                        subStringCounter[subStringSlice[x]] -= 1

                        if (requiredCharsCount !== t.length) {
                            finalSliceValue = x
                            
                            subStringCounter[subStringSlice[x]] += 1
                            if (subStringCounter[subStringSlice[x]] <= fullTCounter[subStringSlice[x]]) requiredCharsCount += 1
                            break
                        }
                    }
                }
                subStringSlice = subStringSlice.slice(finalSliceValue)
                
                if (subStringSlice.length < minSubStringLength) {
                    minSubString = subStringSlice
                    minSubStringLength = subStringSlice.length
                }
            }
        }
    }

    return minSubString

};