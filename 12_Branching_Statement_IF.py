"""
                                     IF STATEMENT
                                     ‾‾‾‾‾‾‾‾‾‾‾‾
When coding, it is common to want certain parts of the code to be executed only when
certain conditions are met. For example, when creating a function, it can be set so
that, if the  input argument is an even number, perform certain task, but if the input
argument is an off number, do something else, or do nothing at all.

The [IF] statement is a code construct that executes blocks of code only under certain
conditions, represented as logical expressions.

>>> if [logical expression]:
>>>     [indented code  block]

When the [IF] keyword is used, Python will interpret an [IF] statement is present, and
determine if the associated logical expression is [True]. If it is, then the indented
code block will be executed.

It is possible to set that a block of code must behave in more than one way, when there
are several conditions to consider, which can be done by the [ELIF] keyword (Else If).

Finally, if the block of code is meant to perform a task even when the previous
condition/s are [False], the keyword [ELSE] must be used, to represent the case of a task
being needed even if previous conditions are not met.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create the function \'check_num\', which prints out if a number is an Integer '
      'or a floating\npoint number, positive or negative, odd or even, and if the '
      'absolute value of the number\nis lower than 10, between 10 and 50, or larger '
      'than 50.\n')

print('def check_num(x):')

print('\n    # check if x is int or float')
print('    if type(x) is int:\n'
      '        print(\'1- The entered number is an Integer.\'')
print('    else:\n'
      '        print(\'1- The entered number is a Float.\'')

print('\n    # check if x is positive, negative or zero.')
print('    if x > 0:\n'
      '        print(\'2- The entered number is Positive.\'')
print('    elif x < 0:\n'
      '        print(\'2- The entered number is Negative.')
print('    else:\n'
      '        print(\'2- The entered number is Zero.\'')

print('\n    # check if x is odd or even')
print('    if x % 2 == 0:\n'
      '        print(\'3- The entered number is Even.\'')
print('    else:\n'
      '        print(\'3- The entered number is Odd.\'')

print('\n    # check if abs(x) is lower than 10, between 10 and 50, or larger than 50')
print('    if abs(x) <= 10:\n'
      '        print(\'4- The absolute value of x is lower than or equal to 10.\'')
print('    elif 10 < abs(x) < 50:\n'
      '        print(\'4- The absolute value of x is between 10 and 50.\'')
print('    else:\n'
      '        print(\'4- The absolute value of x is greater than or equal to 50.\'')

def check_num(x):
    # check if x is int or float.
    if type(x) is int:
        print('1- The entered number is an Integer.')
    else:
        print('1- The entered number is a Float.')

    # check if x positive, negative or zero.
    if x > 0:
        print('2- The entered number is Positive.')
    elif x < 0:
        print('2- The entered number is Negative.')
    else:
        print('2- The entered number is Zero.')

    # check if x is off or even.
    if x % 2 == 0:
        print('3- The entered number is Even.')
    else:
        print('3- The entered number is Odd.')

    # check if abs(x) is lower than 10, between 10 and 50, or larger than 50.
    if abs(x) <= 10:
        print('4- The absolute value of x is lower than or equal to 10.')
    elif 10 < abs(x) < 50:
        print('4- The absolute value of x is greater than 10 but lower than 50.')
    else:
        print('4- The absolute value of x is greater than or equal to 50.')

print('\nNow execute the function with a couple example values:')

print('\ncheck_num(10):'), check_num(10)
print('\ncheck_num(205):'), check_num(205)
print('\ncheck_num(-45.5):'), check_num(-45.5)
print('\ncheck_num(0):'), check_num(0)

"""
Branching statements are the biggest operations involving Boolean values. Lets go over
Boolean and Comparison operations again:

BOOLEAN OPERATIONS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
- x OR y --> Program function will trigger if EITHER conditions 'x' or 'y' are [True]. If
  ‾‾‾‾‾‾   condition 'x' is not met, thus [False], the condition 'y' mights still be
           [True] to perform a certain action. If neither conditions 'x' nor 'y' are met,
           both comparison attempts will return the boolean value [False] and the program
           will not perform a certain action.

- x AND y --> Program function will trigger if BOTH conditions 'x' and 'y' are met, thus
  ‾‾‾‾‾‾‾  both comparison attempts returning the boolean value [True]. If either
           condition isn't met, the program will abstain from performing a certain action
           since the [AND] operator needs ALL conditions to be [True].

- if x --> In this case, 'x' already has a boolean value assigned to it. 'x' can either
  ‾‾‾‾     be [True] or [False], and the program will react according to it, by
           performing a certain action if the condition 'x' is [True]. The boolean value
           assigned to 'x' could be extrinsic, meaning that we already created a variable
           'x' with a [True] or [False] value; or intrinsic, meaning that 'x' could be an
           instant comparison like "two equals three", which returns the boolean value
           [False].

> NOT x --> Opposite to the previous case, the program will react by performing a certain
  ‾‾‾‾‾    action if the condition 'x' is [False]. In this case, 'x' still has a boolean
           value already assigned to it, either extrinsic or intrinsic.

COMPARISON OPERATIONS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
- x [<] y --> Returns [True] if 'x' is LOWER than 'y'.
  ‾‾‾‾‾‾‾
- x [<=] y --> Returns [True] if 'x' is LOWER than OR EQUAL to 'y'.
  ‾‾‾‾‾‾‾‾
- x [>] y --> Returns [True] if 'x' is GREATER than 'y'.
  ‾‾‾‾‾‾‾
- x [>=] y --> Returns [True] if 'x' is GREATER than OR EQUAL to 'y'.
  ‾‾‾‾‾‾‾‾
- x [==] y --> Returns [True] if 'x' is EQUAL to 'y'.
  ‾‾‾‾‾‾‾‾
- x [!=] y --> Returns [True] if 'x' is NOT EQUAL to 'y'.
  ‾‾‾‾‾‾‾‾
- x [is] y --> Returns [True] if 'x' is given the object identity of 'y'.
  ‾‾‾‾‾‾‾‾
- x [is not] y --> Returns [True] if 'x' is negated the object identity of 'y'.
  ‾‾‾‾‾‾‾‾‾‾‾‾
"""
