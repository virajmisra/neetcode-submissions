class Solution:
    def isValid(self, s: str) -> bool:
        m = {}
        m[')'] = '('
        m[']'] = '['
        m['}'] = '{'
        stack = []

        for c in s:
            if c not in m.keys():
                stack.append(c)
            else:
                if not stack or stack.pop() != m[c]:
                    return False
        return len(stack) == 0
            