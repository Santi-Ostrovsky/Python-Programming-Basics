"""
                                     WHILE LOOPS
                                     ‾‾‾‾‾‾‾‾‾‾‾
While Loops are logic structures that allow to run through a specific block of code
several times, until a certain condition is met. They represent a set of instructions
that repeats itself for as long as the associated logical expression is True.

>>> while [logical expression]:
>>>     [indented code block]

When the Python interpreter reaches a While Loop, it first determines whether the
logical expression of the loop is True or False. If the expression is True, then the
code block is executed. Once and every time the code block is executed, the program
returns to the logical expression at the beginning of the statement and, if at any
point the logical expression becomes False, the loop is terminated.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create a While Loop that will run 5 times and print out every time it does.\n')

print('>>> x = 1')
print('>>> while x <= 5:')
print('>>>     print(\'Times the Loop has run:\', x)')
print('>>>     x += 1   # Expression equivalent to [x = x+1], needed to change the '
                      'value of \'x\'\n               so that the loop does not '
                      'run indefinitely.')

print('\nNow execute the loop:\n')

x = 1
while x <= 5:
    print('Times the loop has run:', x)
    x += 1

"""
                                      FOR LOOPS
                                      ‾‾‾‾‾‾‾‾‾
For Loops are sets of instructions that get repeated or iterated for every value in a
sequence. These loops always have a predefined begin and end, bounded by the sequence.

>>> for [looping variable] in [sequence]:
>>>     [indented code block]

The For Loop assigns the 'looping variable' to the first element of the sequence and
executes the code block. Then assigns the 'looping variable' to the second element
and executes the code block once again. This process is repeated until there are no
more elements in the sequence to assign.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create a For Loop that prints out every item in a list.\n')

print('>>> numbers = [1, 2, 3, 4, 5]')
print('>>> for num in numbers:')
print('>>>     print(\'-->\', num)')

print('\nNow execute the loop:\n')

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print('-->', num)

print('')
print('Now Create a For Loop that prints out every character of a String.\n')

print('>>> for letter in \'Banana\':')
print('>>>     print(\'-->\', letter)')

print('\nNow execute the loop:\n')

for letter in 'Banana':
    print('-->', letter)

"""
                                LOOP CONTROL STATEMENTS
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Using loops in Python automates and repeats tasks in an efficient manner. However
sometimes, there may arise a condition where we want to exit the loop completely,
skipping an iteration or ignoring certain conditions by doing so; terminate the loop
at a particular point in the execution without reaching the logical expression; avoid
the natural termination of said loop; or to do nothing at a particular instance when
the loop would otherwise be performing its task.

These actions can be done by using the Loop Control Statements [BREAK], [PASS] and
[CONTINUE].

                                    BREAK STATEMENT
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [BREAK] statement in Python is used to bring the control out of the loop when some
external condition is triggered, by inserting the 'break' keyword inside the loop body
(usually after an [IF] statement condition).
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Break a Loop that prints out every item in a list when it reaches a '
      'particular number.\n')

print('>>> numbers = [1, 2, 3, 4, 5]')
print('>>> for num in numbers:')
print('>>>     if num == 3:')
print('>>>         print(\'Found 3!\')')
print('>>>         break')
print('>>>     print(num)')

print('\nGoing step by step through the loop, it performs the following tasks:\n'
      '1- For every item in list \'numbers\'...\n'
      '2- Open IF condition: if item in \'numbers\' equals 3...\n'
      '3- Print out \'Found 3!\', and break the loop...\n'
      '4- In previous indentation, print out every item in the list as long as no '
      'other conditions are met.\n')

print('Now execute the loop:\n')

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print('Found 3!')
        break
    print(num)

"""
                                    PASS STATEMENT
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [PASS] statement is a null statement, but not ignored by the Python interpreter like
comments are. It is used as a placeholder, when the programmer does not know what code
to write, and may write it later.

Sometimes, the [PASS] statement is used when there is no code to be executed
but an empty code block is not allowed, like in loops, function or class definitions
and if statements. Using the [PASS] statement avoids the error of having no code where
a code block is required.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Define an empty function using the [PASS] statement:\n')

print('>>> def empty_function():')
print('>>>     pass')

def empty_function():
    pass

print('\nExecute function \'empty_function()\' -->  (nothing happens since the '
      'function is\n                                          empty, but '
      'the program does not crash).')

print('\nNow use [PASS] statement in a conditional statement:\n')

print('>>> a =  10')
print('>>> b =  20')
print('>>> if a < b:')
print('>>>     pass')
print('>>> else:')
print('>>>     print(\'b > a\')')

print('\nAnd execute the code block -->  (nothing happens since \'b\' is '
      '\n                                 always greater than \'a\')')

a = 10
b = 20
if a < b:
    pass
else:
    print('b > a')

"""
                                  CONTINUE STATEMENT
                                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [CONTINUE] statement forces the loop to skip the execution of iterations
after the it. Using the same example from the [BREAK] statement in a For loop,
contrary to breaking/terminating the loop, the [CONTINUE] statement will force
the code block to continue running until all iterations are executed in the loop.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Continue the count after founding the value \'3\' in previous example.\n')

print('>>> numbers = [1, 2, 3, 4, 5]')
print('>>> for num in numbers:')
print('>>>     if num == 3:')
print('>>>         print(\'Found 3!\')')
print('>>>         break')
print('>>>     print(num)')

print('Now execute the loop:\n')

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print('Found 3!')
        continue
    print(num)

"""
In this case, the [CONTINUE] statement allowed to skip the iteration '3' when the
condition [num == 3] was met, and still execute the rest of the loop, printing out
the remaining values from the list 'numbers'.


                                 NESTING FOR LOOPS
                                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
For loops go over each and every value in an iterate or given range/values. When the
Python interpreter is presented with a loop within a loop, it performs the same
operation, with all sequences simultaneously.

In the following example, the interpreter is presented with two different iterations,
and when given the structure of a nested For loop, it will resort to combine all
values in the first iterator with all values in the second one (and so on, if there
are more than two iterators/sequences). In this case, once a value in the fist list
has been paired to all values in the second list, the program moves on to the next
value in the first list, and so on.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Nesting two For loops.\n')

print('>>> numbers = [1, 2, 3]')
print('>>> letters = [\'A\', \'B\', \'C\']\n')

print('>>> for num in numbers:')
print('>>>     for letter in letters:')
print('>>>         print(num, \'-\', letter)')

print('\nNow execute the loop:\n')

numbers = [1, 2, 3]
letters = ['A', 'B', 'C']

for num in numbers:
    for letter in letters:
        print(num, '-', letter)

"""
                             RANGE() BUILT-IN FUNCTION
                             ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Even if it categorized as a function, rather than being one, [RANGE] is actually an
immutable sequence type. It functions as an iterator creation method, where its
arguments create parameters for other functions or variables to count over a certain
amount of steps.

[RANGE(x, y, z)] takes up to 3 arguments:
--> 'x' - Start count at value 'x'.
--> 'y' - End count at value 'y', not counting 'y'.
--> 'z' - In steps of 'z'.

If only one argument was entered, it would be taken as 'y' (range limit -1), and it
will start at Zero [0] by default.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('RANGE() --> Use For loop to print out all values in range(1, 10, 2)\n'
      '            (meaning: from 1 to 9 in steps of 2).\n')

print('>>> for num in range(1, 10, 2)')
print('>>>     print(\'-->\', num)\n')

print('Now execute:')

for num in range(1, 10, 2):
    print('-->', num)