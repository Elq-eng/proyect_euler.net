# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from math import pow

x = list(range(1,101))
print(x)
# resultado 1
result1 = pow(sum(x),2)
print(result1)
y = 0
#resultado2
for n in x:
  y = y + pow(n,2)
print(y)

result = result1 - y
print(result)