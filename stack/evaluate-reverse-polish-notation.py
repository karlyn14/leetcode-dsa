class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # ✅ Use integer division truncating toward zero
                    stack.append(int(a) // int(b) if (a * b) > 0 else -(abs(int(a)) // abs(int(b))))
            else:
                stack.append(int(token))

        return stack[0]
