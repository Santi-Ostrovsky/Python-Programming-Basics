"""
                                        VARIABLES
                                        ‾‾‾‾‾‾‾‾‾
Variables are values contained in names that we determine, and carried either along the
entire code, or just inside particular functions.

Variables can be made out of ANY Data type, not just the main 3 types (Strings, Numbers
and Booleans) already seen. They can also be made out of a combination of more than one
Data type, if defined correctly, or even arithmetic operations such as '10 + 6' (variable
would be equal to '16').

To define a variable, it has to be named and equaled to a value, a piece of information.
When defining variables in a Python file, names cannot have whitespaces in them, so words
can be separated either by an underscore [_] or just by capitalizing letters. There's no
required casing for letters in a variable name, they can all be lowercase, uppercase,
titlecase or capitalized.
"""
# EXAMPLES
print('')
print('Lets define a variable by entering the following:')
print('StringVariable = \'This variable is a string\'')
StringVariable = 'This variable is a string'
print('\nNow that a string variable was defined, lets define one for each Data type.')
print('NumberVariable = \'26\'')
NumberVariable =  26
print('Boolean_variable = \'True\'')
Boolean_variable = True
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('We can now print the created variables:\n')
print('StringVariable -->', StringVariable)
print('NumberVariable -->', NumberVariable)
print('Boolean_variable -->', Boolean_variable)
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('As seen in previous files, non-string variables need to be converted to be '
      'concatenated,\nunless they are separated with a comma [,].')
print('\n\'StringVariable + \' \' + str(NumberVariable) + \' \' + '
      'str(Boolean_variable):\'')
print(StringVariable + ' ' + str(NumberVariable) + ' ' + str(Boolean_variable))
print('\nNow, separate them with a comma [,]...\n\n'
      '\'StringVariable, NumberVariable, Boolean_variable\':')
print(StringVariable, NumberVariable, Boolean_variable)

"""
Sometimes, empty variables are created (variables without value) so that certain
functions or program functionalities can fill them up for the program to use later. 
"""
# EXAMPLE
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('An empty variable \'empty\' is created: [empty = \'\']\n'
      '\nEven if the \'empty\' variable doesn\'t have any data assigned yet, it must '
      'have a Data type. So,\nwhen defining the variable, commas [\'\'] will be used '
      'to assign the String Data type to it, or it\ncan be defined as [0] (zero) '
      'to have no value but belong to the Number Data Type, for example.')
print('\'empty\' = \'\'')
print('\nNow, another variable can be created as the solution to an arithmetic '
      'operation, for example,\nand then given \'empty\', the value of said variable:')
print('\n\'result = 10 + 6\'')
print('\'empty = result\'')
print('\'print(empty)\' ↓')
result = 10 + 6
empty = result
print(empty)

"""
Note that the variable 'empty's data type was [String], but given as a new value, the
result of an arithmetic operation, its data type changed to [Number], specifically an
[int] value, which can be converted to [float] without trouble.

As this last example shows, variable values can be changed at any time, before or during
the execution of the program, just by re-defining them (assigning a new value).
"""
# EXAMPLE
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
name = 'Beta'
print('My name is', name)
name = 'Alfa'
print('But I like the name', name, 'better.')
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
