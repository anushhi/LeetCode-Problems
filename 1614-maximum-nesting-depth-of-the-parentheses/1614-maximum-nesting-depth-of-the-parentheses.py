class Solution:
    def maxDepth(self, s: str) -> int:
        result_depth = 0
        current_depth = 0
        for i in s:
            if i == "(":
                current_depth += 1
            elif i == ")":
                if current_depth >= result_depth:
                    result_depth = current_depth
                current_depth -= 1
        return result_depth