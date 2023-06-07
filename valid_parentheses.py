def is_valid_parentheses(s):

  stack = []
  opening_brackets = ["(", "[", "{"]
  closing_brackets = [")", "]", "}"]
  bracket_map = { ")" : "(", "]" : "[", "}" : "{"}

  for char in s:
    if char in opening_brackets:
      stack.append(char)
    elif char in closing_brackets:
      if len(stack) == 0 or stack.pop() != bracket_map[char]:
        return False

  return len(stack) == 0


print(is_valid_parentheses("()[]"))
