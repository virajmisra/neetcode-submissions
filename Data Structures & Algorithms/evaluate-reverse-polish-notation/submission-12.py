class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                s = stack.pop()
                f = stack.pop()
                res = f - s
                stack.append(res)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                s = stack.pop()
                f = stack.pop()
                res = int(f/s)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
        