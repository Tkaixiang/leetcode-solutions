/**
 * @param {string} s
 * @return {string}
 * https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=top-100-liked
 */

 var decodeString = function(s) {
    const numberStack = [] // Used to store the numbers encountered and used
    const danglingStringStack = [] // Used to store "dangling strings" if their strings are not computed immediately
    let isNumber = false
    let currentNumber = "" 
    let currentString = "" 
    let finalOutputString = ""
    for (let i = 0; i < s.length; i++) {

        if (s[i].charCodeAt(0) <= 57 && s[i].charCodeAt(0) >= 48) {
            isNumber = true
            currentNumber += s[i]

            if (currentString.length > 0) {
                danglingStringStack.push(currentString)
                currentString = ""
            }
        }
        else {
            // if previously a number (i.e this is a "[")
            if (isNumber) {
                numberStack.push(parseInt(currentNumber))
                currentNumber = ""
                isNumber = false
            }
            else if (s[i] === "]") {
              currentString = currentString.repeat(numberStack.pop())

              // Basically checks if the current LAYER === current dangling string
              // >= because Dangling Strings occur if there are strings before any encoded strings
              if (danglingStringStack.length > 0 && danglingStringStack.length >= numberStack.length) currentString = danglingStringStack.pop() + currentString
              if (numberStack.length === 0) {
                  finalOutputString += currentString
                  currentString = ""
              } // If no more nesting operations, add to finalOutput
            } 
            else currentString += s[i]
        }
    }


    return finalOutputString + currentString // handle trailing strings
};