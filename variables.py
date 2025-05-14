#def right_justify(s):
    #spaces=70-len(s)
    #print(" " * spaces + s)
    
#right_justify("monty")

def do_twice(f):# function that takes a function as an argument
    f()
    f()
def print_spam():# function to be passed to do_twice
    print("spam")# function to be passed to do_twice
do_twice(print_spam)# calling do_twice with print_spam as an argument

def do_twice(f, value):# modified function that takes a function and a value as arguments
    f(value)# calling the function with the value
    f(value)
def print_twice(x):# function to be passed to do_twice
    print(x)
    print(x)
do_twice(print_twice, "spam")# calling do_twice with print_twice and a value

def do_four(f, value):# function that takes a function and a value as arguments
    do_twice(f, value)# calling do_twice with the function and value
    do_twice(f, value)# calling do_twice with the function and value
do_four(print_twice, "spam")# calling do_four with print_twice and a value


