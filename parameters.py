# Parameters in python functions

def greet():
    print("Hello, g")
    print("What's good?")
    print("What's gucci?")

# This method greets the user with the name passed in the arguments
def greet_with_name(name):
    print(f"Hello,  {name}")
    print(f"What's good {name}?")
    print(f"What's gucci {name}?")


greet_with_name("mark")

# the difference between parameters and arguments is 
# that parameters are declared on the functions and 
# arguments are implemented when calling the function 
# e.g. greet_with_name(name) <- parameter | greet_with_name("pedro") <- argument