class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {}
        pairs[')'] = '('
        pairs[']'] = '['
        pairs['}'] = '{'
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False
        return len(stack)==0