# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# =============================================================

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        a = []


        for item in tokens:
            if item == '+':
                a.append(a.pop() + a.pop())
            
            elif item == '-':
                p,q = a.pop(), a.pop()
                a.append(q-p)

            elif item == '/':
                p,q = a.pop(), a.pop()
                a.append(int(q/p))

            elif item == '*':
                a.append(a.pop() * a.pop())

            else:
                a.append(int(item))
        
        return a[0]



sol = Solution()

token = ["2","1","+","3","*"]

result = sol.evalRPN(token)

print(f'Result for token :{result}')