data = [1,2,3,4,5]
iterator = iter(data)
# print(next(iterator))
# print(next(iterator))


def factors(n):
    for k in range(1,n+1):
      if n % k == 0:
        yield k

factorsIt = factors(5)

print(next(factorsIt))
print(next(factorsIt))

def fibonacci():
  a=0
  b=1
  while True:
    yield a
    future = a + b
    a = b
    b = future