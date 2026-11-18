class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {"]":"[", "}":"{", ")":"("}
        for r in s:
            if r in closetoopen:
                if stack and stack[-1] == closetoopen[r]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(r)
        return not stack