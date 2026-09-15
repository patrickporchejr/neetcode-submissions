class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in '[({':
                stack.append(c)

            if c in '])}':
                if len(stack) == 0:
                    return False

                if stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        