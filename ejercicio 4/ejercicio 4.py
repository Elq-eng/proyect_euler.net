# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# maximo valor 999;

# hacer el nuero encontrando los maximos y minimos 
result3 =[]
for x in range(1,999):
    for y in range(1,999):
        result = x*y
        result1 = str(result)
        result2 = list(result1)
        
        if (len(result2) == 6 ):
           
            if(result2[0] == result2[5] and result2[1] == result2[4] and result2[2] == result2[3]):
                 
                 result3.append(result)
        
result3.sort()
print(result3)