// https://leetcode.com/problems/longest-palindromic-substring
/**
 * @param {string} s
 * @return {string}
 */
const expand = (left, right, s) => {

    if (s[left] !== s[right]) return ""
    // handle EVEN palindromes since startLeft != startRight always
    // and we immediately move left/right once we enter the while loop
    while (true) {
        newLeft = left - 1
        newRight = right + 1
        if (newLeft < 0 || newRight >= s.length || s[newLeft] !== s[newRight]) return s.slice(left, right + 1)
        left = newLeft
        right = newRight
    }
}

var longestPalindrome = function (s) {
    if (s.length === 1) return s

    let longestPalindrome = ""
    // "Expand outwards from EACH character in string" method
    // "aba" - centre = "b", 1st == 3rd char [ODD PALINDROME]
    // "abba" - centre = "", 2nd == 3rd char, 1st == 4th char [EVEN PALINDROME]
    for (let i = 0; i < s.length - 1; i++) {
        const oddPalindrome = expand(i, i, s) // Takes centre as (i, i)
        if (oddPalindrome.length > longestPalindrome.length) longestPalindrome = oddPalindrome

        const evenPalindrome = expand(i, i + 1, s) // Takes centre as between (i, i+1) (i.e blank between 2 chars)
        if (evenPalindrome.length > longestPalindrome.length) longestPalindrome = evenPalindrome
    }
    return longestPalindrome
};