"""
                                    OTHER DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> LISTS
> TUPLES
> SETS
> DICTIONARIES
> CLASSES / OBJECTS

                                        TUPLES
                                        ‾‾‾‾‾‾
Similar to Lists, Tuples are Data types that allow to store individual pieces of data,
both of a single or different Data types, organized inside a variable. The main
difference with the List Data type, is that objects in the Tuple are IMMUTABLE, values
inside cannot be deleted, replaced or altered in any way. Usually used to store data that
is likely never going to change, such as geographic coordinates. Tuples can also be
referred as ITERABLE, for containing several pieces of data.

Even if Tuples are immutable, they may contain mutable objects inside, such as Lists. So,
if a tuple contains a list, the values inside can be modified, but the list itself cannot
be replaced as it is a single value inside the tuple. If it was the other way around, and
there was a tuple contained inside a list as one of its values, the tuple can be removed
or replaced entirely, but not the values contained inside it.

Tuples may be constructed in several ways:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1 > Define a variable and separate all values with a comma [,]. To make sure there will
be no syntax errors in the code, all values may be also enclosed with parentheses [()].
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create tuple \'tuple\' by defining it as a variable:\n'
      '\'tuple1\' = 0, 1, 2, 3, 4, 5 --//-- \'tuple2\' = (\'Tom\', \'Anna\', \'Wayne\')')
tuple1 = 0, 1, 2, 3, 4, 5
tuple2 = ('Tom', 'Anna', 'Wayne')
print('')
print('Now print them out:')
print('tuple1 :', tuple1)
print('tuple2 :', tuple2)
"""
In these examples, both variables are tuples, one originally defined with parentheses,
and one without, but both have the tuple format, so are both printed out the same by
the Python interpreter.
_______________________

2 > Using a Type Constructor (built-in tuple-creating function)
- EXAMPLE: random_values = tuple(x, y, z...) --> Creates tuple called 'random_values'.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create tuple \'letters\' by using the built-in function [tuple()], to make '
      'a tuple out of a string:\n'
      'text = \'Python\'\n'
      'letters = tuple(text)')
text = 'Python'
letters = tuple(text)
print('')
print('Now print it out:')
print('letters :', letters)

"""
3 > To construct a 0 or 1 items tuple out of a single variable, the first method needs to
be carefully looked out.

To create an empty tuple, name a variable and pair it with an empty value in parentheses.
To create a 1-item tuple, name a variable and leave a comma [,] after the first and only
item in the tuple.
"""
# EXAMPLES:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create an empty tuple \'tuple3\' by defining it as a variable with no values in '
      'parentheses: \'tuple3\' = ()')
tuple3 = ()
print('Print \'tuple3\':', tuple3)
print('\nNow create an 1-item tuple \'tuple4\' by defining it as a variable with one '
      'value and a comma [,]: \'tuple4\' = \'ALFA\',')
tuple4 = 'ALFA',
print('Print \'tuple4\':', tuple4)

"""
Such as Lists, TUPLES CAN ALSO BE NESTED, and have multiple tuples inside a single main
tuple, and those inner tuples may also be maid out of other data sequences, like lists.

                                    TUPLE METHODS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾
In terms of built-in methods, tuples have the same methods all ITERABLE Data types have
(so same as lists), but can only use those that don't alter individual values inside the
tuple.
"""