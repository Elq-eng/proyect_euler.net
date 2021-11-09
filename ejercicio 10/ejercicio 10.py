x = list(range(1,2000001))
count = 0
value = []
for n in x: 
    if n%2 != 0:
        for v in x:
            y = n%v
            if y == 0:
                count += 1
            if count >= 3:
                break;
            elif count == 1 and v >= 200:
                break;
        if count <= 2:
            value.append(n)
        count = 0
    


print(sum(value))
#%%
count = 0;
newValue = [];
for x in value: 
    for v in range(1,(x+1)):
        result = x%v
        if result == 0:
            count += 1
        if(count >= 3):
            pass
    if(count == 2 ):
        newValue.append(x);
    count = 0
    print(x)
        
print(newValue)


# resultado 142913828922