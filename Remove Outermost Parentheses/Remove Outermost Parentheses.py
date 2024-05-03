class Solution:
  def removeOuterParentheses(self, s: str) -> str:
    res = ""
    stack = []

    for i in s:

      if i == '(':
        if stack:
          res = res + i
        stack.append(i)

      elif i == ')' and len(stack) == 1:
        stack.pop()

      elif i == ')' and len(stack) > 1:
        stack.pop()
        res = res + i

    return res
