"""
                                    MAIN DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> STRINGS: Alphanumeric values presented in single or double quotes [''], [""].
> NUMBERS: Numeric values presented without quotes.
> BOOLEAN: True / False values, that determine a quality on a statement.

                                       NUMBERS
                                       ‾‾‾‾‾‾‾
Numbers are taken as numeric values. They can Integers [int(x)] or Decimal [float(x.y)].

If wanted to get a user input as a number, it has to be converted to such Data type, as
it will be a string by default.
"""
# EXAMPLE NUMBERS
print('') # Blank line.
print('The following is a number:', 26) # Displays in console, a combination of a string
print('\nAll these are numbers:')       # and a number, in number data type.
print(26, 30, 21, 10, 15, 84, 96, 73, 105)

"""
Now, there's a difference between numbers inside a string and those with the [number]
Data type. For example, if we wanted to use the symbol [+] to add a number to another,
we could only get an arithmetic operation out of numbers in the [number] Data type,
otherwise the symbol [+] would just be concatenating to strings containing numbers.
"""
# EXAMPLES:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('\nThe string \'5\' plus [+] the string \'2\', equals:')
print('5' + '2', '--> This is not correct arithmetic, but it is what '
                 'the Python interpreter was told to do.')
print('\nIf we use the plus [+] sign to add two numeric values, we\'ll get a valid '
                 'arithmetic operation:')
print('5', '+', '2', '=', 5 + 2, '--> Here, both \'5\' and \'2\' values were entered '
                 'without commas, so that Python would interpret\nboth as values in '
                 'the [number] Data type, including [+], so that it would be a valid '
                 'operator.')

"""                     _________________________________
                        Some things to take into account:
                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
--> Integers and Floats are not the same. Most processes in Python can only be done
    taking integers as arguments or parameters, like counting index positions or ranges.

--> When Integers and Floats are mixed in a single arithmetic operation, the result will
    always be a Float (decimal number), even if the result has to show X.0.
    For EXAMPLE: 2 + 4 equals 6. But, if we were to convert any of those values into a
    floating point number, either by entering it as float(x) or by adding a decimal
    point [2.0 + 4.0] to any of them, re result would no longer be '6', but '6.0'.
    
--> Some arithmetic operations always return a Float, even if all values in it are
    Integers. For EXAMPLE: Division [/] always returns a float. 2 / 2 = 1.0.
"""
# EXAMPLES
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('\nPerforming 2 + 4 as integers vs 2.0 + 4 as float and integer:')
print('2 + 4 =', 2 + 4)
print('2.0 + 4 =', 2.0 + 4)
print('2 + float(4) =', 2 + float(4))
print('')
print('Performing a regular [Division] vs a [Floor Division] (Float vs Integer).')
print('10 / 5 =', 10 / 5)
print('10 // 5 =', 10 // 5)

"""
                                    OPERATORS
                                    ‾‾‾‾‾‾‾‾‾
In Python, there are a number of basic operators to perform arithmetic operations, but
not only can the programmer design their own operators, if needed, the [MATH] module
can be imported into the Python file, with a lot of mathematical functionality such as
new operators and functions for trigonometry, for example.

Addition = [+] --> 2 + 6 = 8
‾‾‾‾‾‾‾‾
Subtraction = [-] --> 8 - 6 = 2
‾‾‾‾‾‾‾‾‾‾‾
Multiplication = [*] --> 2 * 4 = 8
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Division = [/] --> Returns a Float: 8 / 2 = 4.0
‾‾‾‾‾‾‾‾
Floor Division = [//] --> Returns the largest possible Integer: 8 // 6 = 1
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Modulus = [%] --> Returns the remainder of a division: 8 % 6 = 2
‾‾‾‾‾‾‾           In the Floor Division, 8//6 returned 1 as the largest possible
                  Integer, meaning that 6 goes in 8 a maximum of 1 time. The Modulus
                  operation returns the remainder of that operation, which is 2.
                  Modulus can both operate and return Float values.

Exponentiation = [**] --> Returns the result of raising a value by the power of the
‾‾‾‾‾‾‾‾‾‾‾‾‾‾    second: 2 ** 4 = 16 (2 * 2 = 4; 4 * 2 = 8; 8 * 2 = 16)
"""
# EXAMPLES
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('\nAddition --> 2 + 6 =', 2 + 6)
print('\nSubtraction --> 8 - 6 =', 8 - 6)
print('\nMultiplication --> 2 * 4 =', 2 * 4)
print('\nDivision --> 8 / 2 =', 8 / 2)
print('\nFloor Division --> 8 // 6 =', 8 // 6)
print('\nModulus --> 8 % 6 =', 8 % 6)
print('\nExponentiation --> 2 ** 4 =', 2 ** 4)

"""
                                MATHEMATICAL FUNCTIONS
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Python includes Built-in functions to get information from numeric values or to perform
certain mathematical calculations:

> ABS(x) - Returns the absolute value of 'x' (positive distance between 'x' and zero).
  ‾‾‾
> CEIL(x) - [MATH MODULE] Returns the ceiling of 'x' (smallest integer greater than 'x')
  ‾‾‾‾
> EXP(x) - [MATH MODULE] Returns the exponential of 'x'.
  ‾‾‾
> FLOOR(x) - [MATH MODULE] Returns the floor of 'x' (largest integer lower than 'x').
  ‾‾‾‾‾
> MAX(x, y, z...) - Returns the largest value of its arguments.
  ‾‾‾
> MIN(x, y, z...) - Returns the smallest value of its arguments.
  ‾‾‾
> MODF(x) - [MATH MODULE] Returns the factorial and integer parts of 'x' in a 2-item
  ‾‾‾‾      tuple, and the integer part is always returned as a float.

> POW(x, y, z) - Returns the value of 'x' raised by the power of 'y'. Can take a third
  ‾‾‾       argument if 'x' and 'y' are integers, and the third argument 'z' will
            perform a modulus operation of the first result. 

> ROUND(x, [y]) - Returns 'x' rounded to the closest integer. If second argument 'y' is
  ‾‾‾‾‾     given, it will round 'x's decimal value to 'y' decimal places.

> SQRT(x) - Returns the square root of 'x' (Always returns a float).
  ‾‾‾‾
> PI - [MATH MODULE] Returns the mathematical constant 'pi'.
  ‾‾
> E - [MATH MODULE] Returns the mathematical constant 'e'.
  ‾
> LOOK UP RANDOM NUMBER [RANDOM MODULE] AND TRIGONOMETRIC FUNCTIONS [MATH MODULE]
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
# EXAMPLES
import math
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('\nAbsolute --> abs(-6.6) =', abs(-6.6))
print('\nCeiling --> math.ceil(-6.6) =', math.ceil(-6.6))
print('\nExponential --> math.exp(6.6) =', math.exp(6.6))
print('\nFloor --> math.floor(-6.6) =', math.floor(-6.6))
print('\nMax --> max(20, 40, -60) =', max(20, 40, -60))
print('\nMin --> min(20, 40, -60) =', min(20, 40, -60))
print('\nMODF --> math.modf(6.6) =', math.modf(6.6))
print('\nPower --> pow(2, 4) =', pow(2, 4))
print('\nPower --> 2**4=16; 16%12=4, so... pow(2, 4, 12) =', pow(2, 4, 12))
print('\nRound --> round(6.6623, 2) =', round(6.6623, 2))
print('\nSquare Root --> math.sqrt(9) =', math.sqrt(9))
print('\nPI --> math.pi =', math.pi)
print('\nE --> math.e =', math.e)
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
