from array_stack import ArrayStack

def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise."""
  left_delimiters = '({['
  right_delimiters = ')}]'

  Stack = ArrayStack()

  for c in expr:
    if c in left_delimiters:
      Stack.push(c)
    elif c in right_delimiters:
      if Stack.is_empty():
        return False
      if right_delimiters.index(c) != left_delimiters.index(Stack.pop()):
        return False

  return Stack.is_empty()

print(is_matched('()(())'))
print(is_matched('4 + ()((5 + 6))'))
print(is_matched(')(())'))
print(is_matched('(2 + 1 {[ ])}'))