class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        brackets = {')':'(', '}':'{', ']':'['}
        stack = deque()

        for c in s:
            if c not in brackets:
                stack.append(c)
            elif not stack or stack.pop() != brackets[c]:
                return False

        return len(stack) == 0
