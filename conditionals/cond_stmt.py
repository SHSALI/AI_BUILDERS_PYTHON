# a == b
# a > b
# a < b
# a >= b 
# a <= b 
# a != b 

# if condition is true :
# execute this block of code

# a = 10 
# b = 10
# if a > b :
#     print ( " a is greater than b")
# elif a < b :
#     print ( " a is less than b")
# else :
#     print ( " a is equal to b")

# x=9 
# if x > 10 :
#     print("x is greater than 10")
#     if x > 15 :
#         print("x is also greater than 15")
#     else :
#         print("x is not greater than 15")
# else:
#     print("x is not greater than 10")

age = 18
university_student = True

if age >= 18:
    if university_student: # == True 
        print("You are an adult and a university student") # cond 1 and cond 2 both are true
    else :
        print("You are an adult but not a university student") # cond 1 is true, but cond 2 is false , and same in the reverse side.....
    
else :
    print("You are not an adult")
