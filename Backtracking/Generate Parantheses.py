# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generate(
        self, n_current_open, n_open_brackets_not_placed, current_str, output_list
    ):
        if n_current_open == 0 and n_open_brackets_not_placed == 0:
            # Closed properly
            output_list.append(current_str)

        # 1. Add an open bracket
        if n_open_brackets_not_placed > 0:
            self.generate(
                n_current_open + 1,
                n_open_brackets_not_placed - 1,
                current_str + "(",
                output_list,
            )
        if n_current_open > 0:
            # 2. Add a close bracket
            self.generate(
                n_current_open - 1,
                n_open_brackets_not_placed,
                current_str + ")",
                output_list,
            )

    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        # Key: n == number of "(" and ")" we can place
        # We must always start off with an open bracket "("
        # Afterwards, at each level, we can either:
        # - Add "(" if we still have unplaced open brackets
        # - Close with a ")" if there are unclosed open brackets
        # Once both of these are exhausted, we can add it to the list
        self.generate(0, n, "", output)

        return output
