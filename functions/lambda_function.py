# lambda arguments : expression

my_lambda = lambda x: x + 10   
print(my_lambda(5)) # 15

#multiple arguments
x = lambda a, b: a * b
print(x(5, 6)) # 30

def my_function(n):
    return lambda a : a * n # returns a lambda function that take one argument and multiply it by n

my_tripler = my_function(3) # 3 in value of n 

print(my_tripler(11)) # 33 (a value is 11 and n is 3 so 11*3 = 33)

cars = ["Toyota", "Honda", "Ford", "BMW"]
sorted_cars = sorted(cars, key=lambda x: len(x)) # sort the list based on the length of each string
print(sorted_cars) # ['Ford', 'BMW', 'Honda', 'Toyota']