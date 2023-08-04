/**
 * https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=top-100-liked
 * @param {number[]} temperatures
 * @return {number[]} 
 */
var dailyTemperatures = function (temperatures) {
    const daysStack = []
    const output = Array(temperatures.length)
    for (let i = temperatures.length - 1; i >= 0; i--) {
        let numDays = 0
        while (daysStack.length > 0) {
            // larger than top of stack, pop stack
            const topOfStackDay = daysStack.slice(-1)[0]
            if (temperatures[i] >= topOfStackDay[0] ) {
                daysStack.pop()
            }
            // no longer larger, don't pop
            else {
                numDays = topOfStackDay[1] - i
                break
            }
        }
        daysStack.push([temperatures[i], i])
        output[i] = numDays
    }

    // IMPROVEMENT: Keep index (i) in daysStack and use it to access temperatures array when comparing [saves memory]
    return output
};