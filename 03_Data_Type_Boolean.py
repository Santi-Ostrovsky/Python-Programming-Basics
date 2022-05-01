"""
                                    MAIN DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> STRINGS: Alphanumeric values presented in single or double quotes [''], [""].
> NUMBERS: Numeric values presented without quotes.
> BOOLEAN: True / False values, that determine a quality on a statement.

                                       BOOLEANS
                                       ‾‾‾‾‾‾‾‾
Boolean values are two constant objects [True] and [False], that determine the quality of
certain statements, and condition certain program functionalities to work in a specific
way.

Boolean values [True] and [False] occupy a namespace for those words, so no variables in
the code can be named like that. They are both pre-built names in the Python interpreter
with a given functionality (like 'print'), and will always be highlighted when used.
Values [True] and [False] must always be capitalized to work as Booleans.

Most times, Booleans are implicit in the code, meaning that we can condition a function
to work in a certain way if a condition is met. Boolean values will determine if said
conditions are met, by returning a [True] or [False] value to the interpreter.

For example: We want the console to print out the result of the operation '2 + 5', but
only if the result of said operation is lower than zero. After performing the arithmetic
operation '2 + 5', the Python interpreter will check if the condition 'lower than zero'
[<0] is met. If it is, the condition will be [True] and the result will be printed out;
otherwise, the condition won't be met, returning the Boolean value [False] and the result
will not be printed out.

Those types of conditions can be set by using Branching Statements [if], which we'll see
further in the files.

                            BOOLEAN OPERATIONS & CONDITIONALS
                            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The Python interpreter will react to met and unmet conditions, and for that, we must
first set said conditions by performing Boolean operations and/or using conditional or
comparison operators.

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
