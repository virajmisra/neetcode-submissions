class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]