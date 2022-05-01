"""
                                    USER INPUTS
                                    ‾‾‾‾‾‾‾‾‾‾‾
Getting user Inputs is often necessary to name variables or to generate/complement the
functionality of a Python code.

To get user Inputs, the [INPUT] keyword must be used, followed by a prompt indicating
the user what to input.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Lets name the variable \'User_name\' after a user Input, by using\n'
      '[User_name = input(\'Please, enter your name: \')]')
User_name = input('\nPlease, enter your name: ')
print('\nThen print the variable concatenating it to the String: "Hello, [User_name], '
      'welcome to Python."')
print('\n--> Hello, ' + User_name + ', welcome to Python.')

"""
As the example above showed when ran, the program execution will be interrupted every
time it needs an input from the user. This makes sense, since no variables or functions
must be left unused in a program, and if the code requires a user input at any point, it
will most likely fulfill one of those purposes.

It is important to take into account, that by default, all user inputs are interpreted as
Strings. If we wanted the user to input a Number (as Integer or Float) and then use it as
one, we must convert that Data type into the correct one.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Ask the user for number, so that the program can perform an arithmetic '
      'operation with it.')
print('The formula is the same as before: [num1 = input(\'Enter an integer: \']')
num1 = input('\nEnter an integer: ')
print('\nNow, to use the user input as a number, convert it by either using the '
      '[int] or [float] keywords:\n\'Your number multiplied by 2 equals, '
      '[int(num1)*2]')
print('\n--> Your number multiplied by 2 equals', int(num1)*2)

"""
In this case, if the user entered an invalid value (which can happen, depending on the
data type required to perform an arithmetic operation or execute a specific function),
the program would crash and raise a ValueError. To prevent this from happening, because
a good program never crashes, we must use Input-Validation statement/functions, which
we will be able to create after seeing the "Catching Errors" file, by using [TRY] and
[EXCEPT] statements.
"""