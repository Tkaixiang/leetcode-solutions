/**
 * https://leetcode.com/problems/decode-string/submissions/?envType=study-plan-v2&envId=top-100-liked
 * @param {string} s
 * @return {string}
 */

// "Pop the stack and get all values" when encountering a closing bracket
// Push result of bracket back onto stack as a "raw string" to be re-used
var decodeString = function (s) {
    const stringStack = []
    for (let i = 0; i < s.length; i++) {
        
        if (s[i] === "]") {
            let currentString = ""
            // Pop stack until Opening Bracket "[" found
            while (true) {
                const poppedValue = stringStack.pop()
                if (poppedValue === "[") break
                else currentString = poppedValue + currentString
            }

            // Pop stack until full number is obtained
            let numberString = ""
            while (true) {
                // Avoid popping anything more than the number
                if (stringStack.length - 1 < 0) break
                const nextChar = stringStack.slice(-1)
                if (nextChar >= '0' && nextChar <= '9') {
                    numberString = stringStack.pop() + numberString
                }
                else break
            }
            stringStack.push(currentString.repeat(parseInt(numberString))) 
            // IMPORTANT - "resolves" the encoded string so that any further decoding can make use of it
        }
        else stringStack.push(s[i])
    }


    return stringStack.join("")
}; 