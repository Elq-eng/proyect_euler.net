# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
x = list(range(1,10001))
count = 0
value = []
for n in x: 
    for v in x:
        y = n%v
        if y == 0:
            count += 1
    if count <= 2:
        value.append(n)
    count = 0
print(value)

#%%

from decimal import Decimal
value = list(range(1,10001))


target = 600851475143

process = []
for item in value:
     x = target/item
     test = Decimal(x) % 1
     if(test == 0):
         process.append(item)
print(process)