# sets , unchangeable , unordered , no duplicate values
set1 = {1,2,3,4,5,6}
print(type(set1))
print(len(set1))
print(set1)

# add new item
set1.add(7)
set1.add(8)
print(set1)

cars_set={ 'BMW ', 'Mercedes' , 'GMC' , 'FORD' ,'LEXUS'}
set1.update(cars_set)
print(set1)

# Remove new item 
set1.remove('GMC')
set1.remove(2)
print(set1)

# set1.remove('Toyota')
# print(f"Remove result: {set1}")   # Raise error if item DNE..............

# Discard
set1.discard('Toyota')
print(f"Discard result: {set1}") # does not raise error if item DNE...........

#pop
set1.pop() # Remove randon item frm the set --- it only works well with the index
print(set1)

set1.clear()
print(set1)

del set1    # Not defined because it aleardy will be deleted from the (.clear).....
print(set1) 
