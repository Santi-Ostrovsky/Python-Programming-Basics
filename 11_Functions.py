"""
                                     FUNCTIONS
                                     ‾‾‾‾‾‾‾‾‾
Functions are sequences of instructions that perform a specific task, individual blocks
of code that run whenever called.

Every function has input an output parameters. Input parameters are all the data and
arguments a function can take or needs to complete its task; and Output parameters
are returned to the program by the function, the result of whatever the function was
meant to perform.

In earlier files, some built-in functions were used, such as [LEN()], which is used
to find the amount of index positions in a String or the amount of items in an iterable
Data type.

However, most programs will have custom-made functions, that serve the purpose of
performing a task multiple times, without having to type (or copy and paste) the same
block of code over and over along the program.

To define a function, the keyword [DEF] must be used, followed by the name of the
function (only lower case letters), a pair or parentheses where and finally, a
colon [:] to start an indentation.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Lets create a function \'hello_user\', and call it to automatically ask the '
      'user their name,\nand greet them.\n')

print('def hello_user():')
print('    username = input(\'Please, enter your name: \')\n'
      '    print(\'Hello, \' + username + \', welcome.\')')

print('\nThen call the function by typing the name of the function and its '
      'arguments:\n')

print('hello_user()')

def hello_user():
    username = input('\nPlease, enter your name: ')
    print('Hello, ' + username + ', welcome.')

hello_user()

"""
This was a very simple function, which only took a user input and printed it,
concatenated to a couple strings.

Whenever a function PRINTS an output, returns a String. If we wanted the function to
return a mathematical operation, for example, we must use [RETURN] keyword.

                                  RETURN STATEMENT
                                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Most times, individual blocks of code determined as functions, have to perform tasks,
not just print out a String. In this cases, functions will be taking information from
the program, like variables and other values, and RETURNING a result. For this to
happen, the [RETURN] statement is necessary, followed by whatever the function is
supposed to do, like perform a mathematical operation.

After the [RETURN] statement is used, no more code can be added to the function.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Lets create a function \'cube\', and print-call the result.\n')

print('def cube():')
print('    value = input(\'Enter an integer: \')\n'
      '    result = int(value) ** 3\n'
      '    return result')

print('\nInside the function, the variable \'value\' is named after a user input '
      '(integer), then\nanother variable \'result\' was defined where the '
      'arithmetic operation x**3 is performed,\nand finally returning the result '
      'variable to the program, to be displayed or used.')

print('\nIn this case, the function does not print anything on its own. So, in order '
      'for the result\nto be displayed in the console, the function has to be called '
      'through a [PRINT] statement.\n')

print('print(cube())')

def cube():
    value = input('\nEnter an integer: ')
    result = int(value) ** 3
    return result

print(cube())

"""
PRINT VS. RETURN
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
When a function's task is to print out a statement, the [PRINT] keyword will be used in
its code block to display whatever is needed to be printed out. However, when the
function's task is to return a value (no matter the type), the [RETURN] keyword will be
used instead.

If console returns 'NONE' as the result of a function when printed, it means that the
[RETURN] statement is needed. Console displays 'NONE' as the absence of value.


                            LOCAL VARIABLES & GLOBAL VARIABLES
                            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Variables inside and outside functions are in different 'scopes', meaning that if we
have the variable "user_name" in the main program, and we create another variable
"user_name" inside a variable, both variables will be valid and can have different
values assigned to them.

This is why the are two types of variables regarding their 'scope':
- GLOBAL --> Variables in the main program, outside functions.
- LOCAL --> Variables inside functions, not in the main program.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('LOCAL AND GLOBAL VARIABLES')
print('Lets create a variable \'name\' in the main program, and an identically called '
      'variable inside\nfunction \'hello\', then print both of them.\n')

print('\nname = \'Tom\'')

print('def hello():')
print('    name = \'Frank\'\n'
      '    print(\'Hello,\', name)')

print('\nThe function \'hello\' is set to print out a string with the variable '
      '\'name\', but when called,\nit will not print the same is what the program '
      'was commanded to print in the previous line:')

name = 'Tom'

def hello():
    name = 'Frank'
    print('Hello, ' + str(name) + '.')

print('\nprint(\'Hello,\', name) -->', 'Hello, ' + name + '.')
print('hello() ↓'), hello()

"""
Sometimes functions need to use global variables (variables in the main program) in
order to perform their tasks. In that case, the program has to be notified about the
function using said variables, by using the keyword [GLOBAL] at the beginning of the
function, followed by the variables that are being used (separated by a comma [,] if
more than one global variable is being used].
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('LOCAL AND GLOBAL VARIABLES')
print('Lets use the Global variable \'name\' inside a function by using the [GLOBAL] '
      'keyword.')

print('\nname = \'Tom\'')

print('def example_function():')
print('    global name\n'
      '    name = \'Frank\'\n'
      '    print(\'Hello,\', name)')

print('\n\'example_function\' is set to print out a string with the global variable '
      '\'name\', but changing\nits value from \'Tom\' to \'Frank\'. Now, we the '
      'variable \'name\' is printed out of the function,\nits value will be '
      'permanently changed.')
print('The function is called first so it changes the value on the variable \'name\'.')

name = 'Tom'

def example_function():
    global name
    name =  'Frank'
    print('Hello, ' + str(name) + '.')

print('\nexample_function() ↓'), example_function()
print('[\'Hello, \' + name + \'.\'] -->', 'Hello, ' + name + '.')

"""
                                    NESTED FUNCTIONS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Once a function is created, it behaves just like any other Python built-in function.
It can be called from anywhere in the file, and any other function can call on it as
well. This allows the existence of NESTED FUNCTIONS, functions defined within another
functions (parent functions).

In this case, only parent functions are allowed to call the inner/nested function;
however, the nested function retains a separate memory block from its parent function.

We have already seen Global and Local variables. When Nested functions are present in
a program, a new type of variable exists: the NONLOCAL variables. Nonlocal variables
are those present in other functions inside the nest, but not in the main program.
So, the general scope of variables would be: GLOBAL > LOCAL > NONLOCAL.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('NESTED FUNCTIONS')
print('Lets create an \'outer_f\' function, and the nested \'inner_f\' function.')

print('\ndef outer_f():')
print('    print(\'- Outer Function print.\')\n'
      '\n'
      '    def inner_f():\n'
      '        print(\'- Inner Function print.\')\n'
      '\n'
      '    inner_f()\n')

print('Parent function \'outer_f\' prints out a statement, and then defines an inner '
      'function \'inner_f\',\nwhich prints another statement. Then the inner function '
      'is called inside the parent function\n(but outside itself) and when this last '
      'one is called, both functions will be executed.')

def outer_f():
    print('- Outer Function print.')

    def inner_f():
        print('- Inner Function print.')

    inner_f()

print('\nouter_f() ↓')
outer_f()

"""
                                    LAMBDA FUNCTIONS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Sometimes, we do not want to use the normal way to define a function, specially if that
function has only one line of code in it. In said case, an 'anonymous' Python function
can be used, which is a function defined without a name. This type of functions are
called LAMBDA FUNCTIONS, since they are defined using the [LAMBDA] keyword.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('LAMBDA FUNCTIONS')
print('Lets create a LAMBDA function to print out the square of any number:')

print('\nsquare = lambda x: x ** 2')

print('\nThe \'square\' variable can be called at any time with the number \'x\' '
      'as an argument and it\nwill perform as a regular function which task is to '
      'return the square of the argument number.')

square = lambda x: x ** 2

print('\nNow we call the variable \'square\' as if it was a function, and give it '
      'any number as argument.\n\'5\' will be used as an example.')

print('print(square(5)) -->', square(5))

"""
In the example LAMBDA function [square = lambda x: x ** 2], 'x' is the argument and
'x ** 2' is the expression that gets evaluated, operated and returned. The function
itself has no name, but still returns a function object.

It is equivalent to defining a function as follows:

def square(x):
    return x ** 2


                           FUNCTIONS AS ARGUMENTS TO FUNCTIONS
                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Sometimes, it is useful to pass as a function as a variable to another function. In
other words, use functions (built-in or custom made) as inputs in another function.

For example, there's a built-in function called 'max', which is used to find the
largest number among other values in an iterable Data type (list, set, tuple, etc.).

We could assign a variable the value of [max], turning the variable into said built-in
function.

>>> f = max
>>> print(f[100, 20, 300, 250])

--> 300
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('FUNCTIONS AS ARGUMENTS TO FUNCTIONS')
print('Lets use the function \'max\' as an input to the function \'max_plus_1\':')

print('\nf = max')

print('\ndef max_plus_1(x):'
      '    \nglobal f'
      '    \nreturn f(x) + 1')

f = max

def max_plus_1(iterable):
    global f
    return f(iterable) + 1

print('\nNow create a list of numbers to use as argument in the function.')
print('--> nums = [1000, 2000, 350, 4500, 10, 650]')
nums = [1000, 2000, 350, 4500, 10, 650]

print('\nprint(max_plus_1(nums)) -->', max_plus_1(nums))

"""
                                    BUILT-IN FUNCTIONS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Below, a list of some Python built-in functions in version 3.10.2. Full list on Python
documents > Built-in Functions: https://docs.python.org/3.10/library/functions.html

> ABS(x) - Returns the absolute value of the number 'x' (positive distance to zero).
           >>> abs(-2.3)
           --> 2.3

> BIN(x) - Converts the Integer 'x' to a binary string prefixed with "0b". The result
           is a valid Python expression.
           >>> bin(2500)
           --> 0b100111000100

> CALLABLE(x) - Returns the Boolean value [True] if the object 'x' appears callable,
           [False] otherwise. When [True], it is still possible that said call fails,
           but when [False] tha object call will never succeed.
           >>> text = 'example'
           >>> print(callable(text))
           --> True

> ENUMERATE(x, y=z) - Returns an enumerated tuples of iterable 'x', with optional
           argument 'y' (starting from) number 'z'.
           >>> seasons = ['Summer', 'Fall', 'Winter', 'Spring']
           >>> print(list(enumerate(seasons, start=1)))
           --> [(1, 'Summer'), (2, 'Fall'), (3, 'Winter'), (4, 'Spring')]

> FLOAT(x) - Converts the value 'x' into a floating point number.
           >>> number = 500
           >>> print(float(number))
           --> 500.0

> FORMAT(x, [y]) - Convert the value 'x' to a formatted representation, controlled by
           the format-spec 'y'.

> GLOBALS() - Returns a Dictionary implementing  the current module namespace.

> HEX(x) - Converts the Integer 'x' to a lowercase hexadecimal string prefixed
           with "0x".
           >>> print(hex(2500)
           --> 0x9c4

> ID(x) - Returns the ID of the object  'x'.

> INPUT(x)  - Used to get a user input on the prompt 'x'.
            >>>  username = input('Enter your name: ')
            --> Enter your name: [user input]

> LEN(x) - Returns the length (number of items) of the object 'x'.
           >>> print(len('Hello'))
           --> 5

> MAX(x) & MIN(x) - Return the greatest and lowest values in iterable object 'x' or
           the greatest and lowest values or 2 or more arguments, respectively.
           >>> print(max(2, 4, 6, 8))
           --> 8
           >>> print(min(2, 4, 6, 8))
           --> 2

> POW(x, y, z) - Returns 'x', raised by the power of 'y',  modulus operated by the
           optional argument 'z'.
           >>> print(pow(4, 3)
           --> 64

> PRINT(x) - Used to display any printable object.
           >>> print('Hello')
           --> Hello

> RANGE(x, y, z) - Built-in immutable sequence type, that returns a 'list' of values
           from 'x' to 'y' (not including y') in steps of 'z'. By default, ranges start
           at zero [0], so the function could take only once argument 'y' if the count
           is in steps of one.

> ROUND(x, y) - Returns the number 'x' rounded to the number of digits 'y' after the
           decimal point. If 'y' is omitted  or [NONE], returns the nearest integer
           to the number 'x'.
           >>> print(round(2.3653, 2))
           --> 2.37
           >>> print(round(55.5))
           --> 56

> SET(x) - Creates a SET object with elements taken from the iterable 'x'.
           >>> nums1 =  [1, 2, 3]
           >>> nums2 = set(nums1)
           >>> print(nums2)
           --> {1, 2, 3}

> SUM(x, /, y=z) - Returns the sum of the start count 'y' at number 'z', and the items
            from the iterable 'x' from left to right.
            >>> NumList = [1, 2, 3]
            >>> print(sum(NumList, start=5))
            --> 11
            (starts at 5, +1=6, +2=8, +3=11)
"""