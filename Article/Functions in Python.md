This is the basic understanding of functions. How it can be created and called.

(the below content is already verified with online resources still it may contain some mistakes, please mention in the comments if it is so)
What is a function in python?
A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

def my_function():
 print(“Hello from a function”)
Calling a Function
To call a function, use the function name followed by parenthesis:

def my_function():
 print(“Hello from a function”)
my_function()
Output :

Hello from a function
Defining functions
Built-in functions are great, but we can only get so far with them before we need to start defining our own functions. Below is a simple example.

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
This creates a function called least_difference, which takes three arguments, a, b, and c.

Functions start with a header introduced by the def keyword. The indented block of code following the : is run when the function is called.

return is another keyword uniquely associated with functions. When Python encounters a return statement, it exits the function immediately and passes the value on the right-hand side to the calling context.

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)
Output :

9 0 1
Example Program :
Here we have called a function in the main function then inside that another function is called then with that output the function processes its output.

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n'
)
Output :

5
25
To contact — Email | Linkedin | Github | Kaggle | Website
