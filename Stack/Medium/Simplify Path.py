# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def simplifyPath(self, path: str) -> str:
        split_by_slashes = path.split("/")
        final_paths = []  # Works like a stack
        for possible_path in split_by_slashes:
            if possible_path == "..":
                if len(final_paths) > 0:
                    # "/../" should be just "/"
                    final_paths.pop()  # Remove the top of the stack
            elif possible_path == ".":
                continue  # just do nothing
            elif len(possible_path) > 0:
                # A valid path, append to final_paths
                final_paths.append(possible_path)

        return "/" + "/".join(final_paths)
