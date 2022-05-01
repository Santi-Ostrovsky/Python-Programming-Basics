"""
                                    ERROR TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾
There are 3 basic types of Errors in Python: Syntax Errors, Runtime Errors (or
Exceptions) and Logical Errors.

SYNTAX ERRORS: Syntaxis is the set of rules that governs any language. In written and
‾‾‾‾‾‾‾‾‾‾‾‾‾‾  spoken language, rules can be bent or broken, however, in programming,
                these rules are rigid.

                A SyntaxError occurs when the programmer writes an instruction using
                incorrect syntax, making it impossible for Python to execute a command,
                thus always turning this kind of errors, fatal for the code.
                For example, "x = 1" would be the right syntax to assign the value of
                '1' to the variable 'x'. Similarly, "1 = x", would be incorrect.
                Flipping the values in the statement, tells the Python interpreter to
                equalize the first value to the second one, and numbers cannot have
                their values changed, so Python raises a SyntaxError with the following
                description: "Can't assign to literal", alongside the location in the
                code where the Error was found.

                The only solution to this kind of errors, is to re-write the code until
                the Python interpreter finds no more syntax mistakes in it, so that the
                entirety of the program can be executed.

RUNTIME ERRORS: Even if all the syntax is correct in the code, it may still cause errors
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ during its execution. These errors are called Exceptions or
                RuntimeErrors, and are usually harder to find, as they are mostly
                detected only after the program is run.

                These errors are not always fatal, meaning that there are ways to
                prevent the program from crashing when encountering said errors along
                the execution of the code. For example, there is nothing wrong with the
                statement "print(2 / 0)", however, this statement is commanding the
                Python interpreter to perform a division by zero [0], which cannot be
                done, and Python will stop the execution of the program by raising a
                ZeroDivisionError with the following description: "Division by zero",
                alongside the location in the code where the Error was found.

LOGICAL ERRORS: These errors are the most difficult to find and handle. Logic Errors do
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ not crash the program by raising execution errors or exceptions, and
                said program will run smoothly, but the output will not be the one
                expected.

                Logic Errors are those which prevent functions or codeblocks from
                performing the desired task, thus returning the wrong output, making the
                program obsolete. For example, lets create a function to add 2 numbers:

                >>> def sum():
                >>>     x = int(input('Enter first number: '))
                >>>     y = int(input('Enter second number: '))
                >>>     result = x * y
                >>>     return result

                As can be seen, there is nothing wrong with this function's syntax, and
                the only way a Runtime Error can be raised is by the user entering
                something else than an integer as either 'x' or 'y'. However, the aim of
                this function was to get the result of adding said variables, but when
                the result variable was defined, 'x' and 'y' were operated with '*'
                instead of '+', thus performing a multiplication between both values.

                Although Logic Errors seem unlikely to occur and/or easy to find, when
                programs become longer and more complex, these types of errors are easy
                to generate and notoriously difficult to find. When these errors do
                occur, the coder has no choice but to meticulously comb through each
                line of code until the problem is found.

                To avoid generating and help find Logical Errors, a series of good
                programming practices have to be taken into account, which we will talk
                about by the end of the file; and the Python DeBugger (PDB) can be used
                as well(Debugging is the process os systematically removing errors/bugs
                from a code, by stepping through it line by line, to find out any piece
                of code that might cause an error in the program's execution).


                                    CATCHING ERRORS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Runtime Errors, as explained above, are those which can interrupt a program along its
execution, and mostly depend on the relation between variables and functions, what can
easily cause a program to crash when user inputs are involved, for example.

This is why, it is often important to write code that can handle multiple types of
errors or exceptions. More specifically, prevent the occurrence of certain errors when
they might eventually happen, thus preventing the program to shut down.

To do this, a "TRY & EXCEPT" statements code block is needed, which will allow the
program to "catch" errors and take alternative actions in case an error does occur.
The correct basic syntax of a Try-Except block is the following:

>>> try:
>>>     [code block that might raise an Error]
>>> except:
>>>     [alternative action if the Error is raised]

When the [EXCEPT] statement is used, a specific type or error is usually entered so that
Python interpreter does not have to go over the entire list of both built-in and
custom-made exceptions to prevent the program from crashing.

That specific error type can also be given an alias (variable name), and displayed in
console as it, to inform the user about the occurrence of said error. For example:

>>> try:
>>>     user_input = float(input('Enter a decimal point number: '))
>>> except ValueError as err_1:
>>>     print('Error:', err_1)

In this example, the Try-Except block is being used to validate a user input, which
can only be a Float type number. If, when asked to input the value, the user inputs a
string, for example, instead of crashing and raising a ValueError, the program will
catch the error and display the following message in console: "Error: could not convert
string to float: '[input]'.

Most common built-in exceptions are:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
- ArithmeticError --> Base class for all arithmetic error, specifically OverflowError,
  ZeroDivisionError and FloatingPointError.

- ImportError --> Raised when the 'import' statement has trouble when loading a module.

- IndexError --> Raised when a sequence subscript is out of range.

- KeyError --> Raised when a mapping (Dictionary) key is not found among a set of
  existing keys.

- NameError --> Raised when a local or global name is not found.

- RuntimeError --> Raised when the detected error doesn't fall in any of the other error
  categories.

- SyntaxError --> Raised when the interpreter encounters a syntax error.

- TypeError --> Raised when an operation or function is applied to an object of
  inappropriate type.

- ValueError --> Raised when an operation or functions receive an argument that has
  the right type but an inappropriate value, and the situation is not described by a
  more precise exception, such as the IndexError.

LOOK UP COMPLETE LIST OF BUILT-IN EXCEPTIONS HERE (Ctrl + Click):
https://docs.python.org/3/library/exceptions.html#bltin-exceptions

'ELSE' & 'FINALLY' STATEMENTS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
So far, the basic Try-Except block was used. However, there are 2 more statements beside
[TRY] and [EXCEPT] that can be used in said block, to alter the way a task is performed:

- ELSE --> If there are no exceptions raised in the code, then the block following this
  ‾‾‾‾        statement will be executed. EXAMPLE:

              >>> try:
              >>>     result = 5 / x
              >>> except ZeroDivisionError:
              >>>     print('You can't divide by zero!')
              >>> else:
              >>>     print('The answer is:', result)

              If 'x' was any numerical value apart from 'zero' [0] (cannot perform
              division by zero), the ELSE clause would be executed, printing: "The
              answer is: [result]", like if it was commanded under the [TRY] statement.
              Otherwise, the exception ZeroDivisionError would be risen and the program
              would catch it, displaying the message "You can't divide by zero!", and
              the [ELSE] clause would not be executed.

- FINALLY --> The block following this statement will always be executed, regardless of
  ‾‾‾‾‾‾‾     any exceptions being raised or not. EXAMPLE:

              >>> try:
              >>>     result = 5 / x
              >>> except ZeroDivisionError:
              >>>     print('You can't divide by zero!')
              >>> else:
              >>>     print('The answer is:', result)
              >>> finally:
              >>>     print('The program reached its end.')

              Regardless of what value the variable 'x' has in this example, the FINALLY
              clause will always be executed by printing "The program has reached its
              end".

Below, an example TRY-EXCEPT block will be coded inside a While Loop, to create a
permanent user input validation method, which will return an exception message
continuously while the inputted value is not the desired one, only terminating the
program's execution once the right answer is given.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Try-Except loop to catch wrong user inputs until the right answer is given.\n')

print('>>>def enter_num():\n'
    '>>>    valid = True\n'
    '>>>    while valid:\n'
    '>>>        try:\n'
    '>>>            number = int(input(\'Enter a positive even integer: \'))\n'
    '>>>            if number < 0:\n'
    '>>>                print(\'I said positive!\')\n'
    '>>>                enter_num()\n'
    '>>>            elif number == 0:\n'
    '>>>                print(\'Zero is not positive!\')\n'
    '>>>                enter_num()\n'
    '>>>            elif number % 2 != 0:\n'
    '>>>                print(\'I said even!\')\n'
    '>>>                enter_num()\n'
    '>>>        except ValueError:\n'
    '>>>            print(\'That is not an integer!\')\n'
    '>>>            enter_num()\n'
    '>>>        else:\n'
    '>>>            print(\'You did it! Your number is:\', number)\n'
    '>>>        finally:\n'
    '>>>            print(\'The loop has terminated!\')\n'
    '>>>            break\n')

print('Now execute the function: enter_num()')

def enter_num():
    valid = True
    while valid:
        try:
            number = int(input('\nEnter a positive even integer: '))
            if number < 0:
                print('\nI said positive!')
                enter_num()
            elif number == 0:
                print('\nZero is not positive!')
                enter_num()
            elif number % 2 != 0:
                print('\nI said even!')
                enter_num()
        except ValueError:
            print('\nThat is not an integer!')
            enter_num()
        else:
            print('\nYou did it! Your number is:', number)
        finally:
            print('\nThe loop has terminated!')
            break

enter_num()
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

"""
                             GOOD PROGRAMMING PRACTICES
                             ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

TYPE CHECKING
‾‾‾‾‾‾‾‾‾‾‾‾‾
Python is a dynamically typed language, meaning that any variable can take on any data
type at any time. However, it is also a strongly typed language, meaning that once a
variable is assigned with a type, it cannot change in unexpected ways.

For example, the variable 'x' can be given the value '1', and immediately after given
the value of '5' (dynamically typed). But 'x' cannot be given the value '2 + "3"', as
the string "3" cannot be converted in runtime to the appropriate type -int or float-
(strongly typed).

In Python there is often no way to ensure that the user of a program will input
variables of the expected data type, so it is good practice to have functions to
type-check and validate the variables that the user inputs before continuing the
execution, and catching a potential error before it shuts the program down.

To do this, we could either use a structure like the previous example, or use the
built-in [isinstance([object], [type/s])] function, which returns [True] when a
specified object is of a specific type, allowing functions to perform their tasks.


PLAN YOUR PROGRAM
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
When writing an essay, it is important the writer has a structure and a direction they
intend to follow. To help making said structure more tangible, an essay usually starts
with an outline containing the main points addressed in the paper, for example.

This is even more important to do when programming, because computers do not interpret
what you want to code, but the literal translation of what you do type. When coding long
and complex programs, it is good practice to start with an outline addressing all the
tasks you want the program to perform and in which order they should be performed.
Basically, a feature guide for the code that represents the structure of the program.

Pre-planning will ensure that the program will be finished in time, much more
efficiently that a program that was not planned with much thought.

Rule of thumb: plan from top to bottom, then program from the bottom to the top. This
means, that you should first decide what the overall program is supposed to do,
determine what code is necessary to complete the main tasks, and then break those tasks
into small components until they become small modules that can be written with
confidence and no errors.


TEST FUNCTIONS OFTEN
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
When coding, especially in small modules, it is good practice to do it using test cases
after every finished codeblock, for which you expect the answer to be specific, and do
enough cases to be confident that the function of codeblock is, and will always work
properly.

This is especially important if subsequent modules in the program depend on or call the
previous modules, as their effectiveness relies on the effectiveness of previous code.


KEEP A CLEAN CODE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Like a good craftsman who keeps their work area as clean as possible, free of
unnecessary clutter, programmers should keep their code as clean as possible. There are
many strategies to do so, for example: Write code with the fewest amount of instructions
as possible:

                WRONG                 │               RIGHT
──────────────────────────────────────┼─────────────────────────────────────
  >>> y = x ** 2                      │ >>> y = (x ** 2) + (2 * x + 1)
  >>> y = y + 2 * x                   │
  >>> y = y + 1                       │
                                      │

Another way of keeping the code clean, is to use short and concise variable names such
as 'n', 'x' and 'i', instead of 'number_of_answers_given_by_the_user', which is just
too long, even though it is descriptive.

Finally, a very useful practice to keep a clean code, is to comment frequently. No
commenting or over-commenting are both bad practices, but having a concise and
imperative description of each function in the program helps to its readability.
Comments are done by typing [#] or triple quotes [''']/[\"""].
"""
