class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {}
        brackets['{'] = '}'
        brackets['['] = ']'
        brackets['('] = ')'

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or brackets[stack.pop()] != c:
                    return False
        return len(stack) == 0