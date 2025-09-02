# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def __init__(self):
        self.memo = []

    def test_word(self, s: str, wordDict: List[str], i: int):
        if i == len(s):
            return True

        # (3) self.memo here serves more as a "short-circuit" for bad branches
        # - i.e if we landed at i again, we know there is NO WAY TO SEGMENT THE REMAINING SUBSTRING
        # - So instead of exploring, we just kill this branch
        if self.memo[i] == False:
            return False

        for word in wordDict:
            # (2) This basically checks every word in ["car", "ton", "sing", "cart"]
            # - See if we can match any word from this point onwards --> "cart/car"?
            # - If we can, we also need to CONTINUE DOWN THE BRANCH "cart|onsing"
            # - Does "onsing" work for any word in the dictionary?
            if (
                i + len(word) <= len(s)
                and s[i : i + len(word)] == word
                and self.test_word(s, wordDict, i + len(word))
            ):
                return True

        # (3) False, we were unable to segment the string from index i onwards
        self.memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Let's use the example "cartonsing" with ["car", "ton", "sing", "cart", "carousel"]
        # (1) In DP, think of what does "dp[i]" means (where i is typically an index in the array)
        # - This problem unfortunately does not allow for "2 states" (like House Robber)
        # - When we start at index i=0, we can choose EITHER "car", "cart" or "carousel" (3 choices)
        # - Hence, for this, "i" is whether we CAN reach a valid segmentation for the REMAINING substring s[i:len(s)]
        self.memo = [True] * len(s)
        return self.test_word(s, wordDict, 0)
