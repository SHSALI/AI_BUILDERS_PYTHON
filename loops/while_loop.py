# while condition is true :
# execute this block of code

i = 0

while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
    
j =0 
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)    