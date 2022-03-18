import array as arrayModule

def is_multiple(n, m):
  if m == 0: return False
  return n % m == 0

def is_even(k):
  # Cannot use the multiplication, modulo or division operators
  return k & 1 == 0

def min_max(data):
  if (len(data) == 1): return data[0]
  min=max=None
  for number in data:
    if min == None and max == None: min = max = number
    if number > max: max = number
    if number < min: min = number
  return (min, max)

def squares_less_than(n):
  total=0
  for integer in range(1, n):
    total+= integer * integer
  return total

def squares_comprehension(n):
  return sum(n * n for n in range(1, n))

def sum_of_odd_squares(n):
  total=0
  for integer in range(1, n):
    if n & 1 == 1: total+= integer * integer
  return total

def sum_of_odd_squares_comprehension(i):
  return sum(n * n for n in range(1, i) if i & 1 == 1)

compactArray = arrayModule.array('i', [2,5,6,10,25])
[print(item) for item in compactArray]
