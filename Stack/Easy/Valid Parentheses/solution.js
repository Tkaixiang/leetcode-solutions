/**
 * https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {string} s
 * @return {boolean}
 */

// Stack: FILO (First In Last OUt)
// [()]


const openingBrackets = new Set()
openingBrackets.add("{")
openingBrackets.add("[")
openingBrackets.add("(")

const closingToOpeningMap = {
    "}": "{",
    "]": "[",
    ")": "(",
}

var isValid = function(s) {
    const arrayStack = []

    for (let i = 0; i < s.length; i++) {
        if (openingBrackets.has(s[i])) arrayStack.push(s[i])
        else if (s[i] in closingToOpeningMap) {
            // is a closing bracket, check if correct type as last opening bracket encountered
            if (arrayStack.length > 0 && closingToOpeningMap[s[i]] === arrayStack[arrayStack.length - 1]) arrayStack.pop() // remove last opening bracket
            else return false    
        }
    }

    // Check if all opening brackets are accounted for
    // E.g "([]" should return false
    if (arrayStack.length === 0) return true
    else return false
};