# R-1.1
def is_multiple(n, m):
  if m == 0: return False
  return n % m == 0

# R-1.2
def is_even(k):
  # Cannot use the multiplication, modulo or division operators
  return k & 1 == 0

# R-1.3
def min_max(data):
  if (len(data) == 1): return data[0]
  min=max=None
  for number in data:
    if min == None and max == None: min = max = number
    if number > max: max = number
    if number < min: min = number
  return (min, max)

# R-1.4
def squares_less_than(n):
  total=0
  for integer in range(1, n):
    total+= integer * integer
  return total

# R-1.5
def squares_comprehension(n):
  return sum(n * n for n in range(1, n))

# R-1.6
def sum_of_odd_squares(n):
  total=0
  for integer in range(1, n):
    if n & 1 == 1: total+= integer * integer
  return total

# R-1.7
def sum_of_odd_squares_comprehension(i):
  return sum(n * n for n in range(1, i) if i & 1 == 1)
