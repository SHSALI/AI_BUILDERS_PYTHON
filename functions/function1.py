def my_function():
    print("Hello from my_function!")

    my_function() # call the function to execute the code inside the function
    
    temp1=77
    celsius1 = (temp1 - 32) * 5/9
    print(celsius1)
    
    temp2=32
    celsius2 = (temp2 - 32) * 5/9      
    print(celsius2)
    
    temp3=100
    celsius3 = (temp3 - 32) * 5/9
    print(celsius3)
    
    def fahrenheit_to_celsius(temp):
        celsius = (temp - 32) * 5/9
        return celsius  
    
    # parameters vs argument 
    # parameter : variable
    # argument : value passed to the function when calling it
    print(fahrenheit_to_celsius(77))
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(100))   
    
    def my_name(name , country="Bahrain"): # name is the parameter of the function my_name
        print("Hello " + name + " from " + country)
        
    my_name("Sayed Huussain Ali" , " Manama")  # print Sayed Hussain Ali from Bahrain
    #(Sayed Hussain Ali) is the argument passed to the function my_name and name is the parameter of the function my_name