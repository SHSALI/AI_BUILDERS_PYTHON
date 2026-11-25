cars=["Toyota", "Honda", "Ford", "BMW"]

for car in cars:
    print(car)
    
for car in cars:
    if car == "Honda":
        break
    print(car)   
    
newlist=[x for x in cars if x != "Honda"] #list comprehension .......(same but just in one line)
print(newlist)

for x in "Toyota":
    print(x)

for i in range(5):
    print(i)    

adj=["fast", "reliable", "affordable", "luxurious"]    
cars=["Toyota", "Honda", "Ford", "BMW"]    
for i in adj:
    for j in cars:
        print(i, j) #criteria outer loop take all item on inner loop each iteration .........

newlist = [x for x in range(10) if x % 2 == 0] #list comprehension
print(newlist)

newlist = [x for x in range(10) if x % 2 != 0 ] #list comprehension
print(newlist)