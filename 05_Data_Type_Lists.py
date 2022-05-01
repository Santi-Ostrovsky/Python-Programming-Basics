"""
                                    OTHER DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> LISTS
> TUPLES
> SETS
> DICTIONARIES
> CLASSES / OBJECTS

                                        LISTS
                                        ‾‾‾‾‾
Lists are the most versatile Data type in Python. They can contain several pieces of
data, of a single or different Data types, organized inside a variable. Can be referred
as ITERABLE, for containing several pieces of data.

Lists may be constructed in several ways:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1 > Define a variable and, as value, use a pair of square brackets '[]' to denote an
empty list, or enter values inside brackets separated by a comma [,]
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create list \'list_of_numbers\' by defining it as a variable:\n'
      '\'list_of_numbers_1\' = [0, 1, 2, 3, 4, 5]\n               OR\n'
      '\'list_of_numbers_2\' = [0], [1], [2], [3], [4], [5]')
list_of_numbers_1 = [0, 1, 2, 3, 4, 5]
list_of_numbers_2 = [0], [1], [2], [3], [4], [5]
print('')
print('Now print them out:')
print('list_of_numbers_1 :', list_of_numbers_1)
print('list_of_numbers_2 :', list_of_numbers_2)

"""
2 > Using a list comprehension method to automatically create a List with instructed
values --- [SEEN IN LATER FILES].
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create list \'list_of_squares\' by entering, for example:\n'
      'list_of_squares = [x ** 2 for x in range(10)]')
list_of_squares = [x ** 2 for x in range(10)]
print('')
print('Now print it out:')
print('list_of_squares :', list_of_squares)

"""
3 > Using the Type Constructor [list(x)] (built-in list-creating function)
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create list \'letters\' by using the built-in function [list()], to make '
      'a list out of a string:\n'
      'text = \'Python\'\n'
      'letters = list(text)')
text = 'Python'
letters = list(text)
print('')
print('Now print it out:')
print('letters :', letters)

"""
                                    LIST METHODS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾
Like Strings, Lists and all other built-in sequence types can be indexed, sliced, and
any other built-in method can be used on them to either get information about them or
about individual values inside the List, to modify values, add new values, delete values
or even clear the entire List.

As a Data Structure, Lists have several built-in methods (shared with all ITERABLE
Data types,that allow the program to perform all previous mentioned actions with
Lists' objects.

BUILT-IN ITERABLE METHODS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> list.APPEND(x) - Allows to add the value 'x' at the end of a list.
  ‾‾‾‾‾‾‾‾‾‾‾
"""
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('--LIST METHODS--')
print('\n> Append the value \'5\' to the list \'numbers\' = [0, 1, 2, 3, 4] by using '
      '[numbers.append(5)]:')
numbers = [0, 1, 2, 3, 4]
print('Original list \'numbers\':', numbers)
numbers.append(5)
print('Appended list \'numbers\':', numbers)

"""
> list.EXTEND(x) - Allows to append the list 'x' to a base list.
  ‾‾‾‾‾‾‾‾‾‾‾
"""
print('\n> Extend the list\'numb1\' = [0, 1, 2] with the list \'num2\' = [3, 4, 5] '
      'by using [num1.extend(num2)]:')
num1 = [0, 1, 2]
num2 = [3, 4, 5]
print('\'num1\':', num1)
print('\'num2\':', num2)
num1.extend(num2)
print('Extended list \'num1\':', num1)

"""
> list.INSERT(x, y) - Allows to add the value 'y' at the given index position 'x'.
  ‾‾‾‾‾‾‾‾‾‾‾         Index positions always start at count zero [0]. If the given index
                      position 'x' is greater than the length of the list, it would be
                      equivalent to the method [list.append(y)].
"""
print('\n> Insert the value \'2\' to the list \'numbers\' = [0, 1, 3, 4] by using '
      '[numbers.insert(2, 2)]:')
numbers = [0, 1, 3, 4]
print('Original list \'numbers\':', numbers)
numbers.insert(2, 2)
print('New list \'numbers\':', numbers)

"""
> list.REMOVE(x) - Allows to remove the value 'x' from the list. If the value 'x' is 
  ‾‾‾‾‾‾‾‾‾‾‾      repeated, the Python interpreter will only remove the first one.
                      Raises a ValueError if there is no such item in the list.
"""
print('\n> Remove the first value \'3\' in the list \'numbers\' = [0, 3, 1, 2, 3] by '
      'using [numbers.remove(3)]:')
numbers = [0, 3, 1, 2, 3]
print('Original list \'numbers\':', numbers)
numbers.remove(3)
print('New list \'numbers\':', numbers)

"""
> list.POP(x) - Allows to remove one value from the given list, at index position 'x'.
  ‾‾‾‾‾‾‾‾         Different from [list.remove(X)], [POP] removes an item or value
                      on the list by index position, in stead removing the first value
                      of 'x' on the list.
"""
print('\n> Pop the value \'5\' from the list \'numbers = [1, 2, 3, 4, 5] by using '
      '[numbers.pop(4)]:')
numbers = [1, 2, 3, 4, 5]
print('Original list \'numbers\':', numbers)
numbers.pop(4)
print('Popped list \'numbers\':', numbers)

"""
> list.CLEAR() - Allows to delete ALL elements in the given list. Takes no arguments.
  ‾‾‾‾‾‾‾‾‾‾
"""
print('\n> Clear all values in list \'numbers\' = [0, 1, 2, 3, 4] by using '
      '[numbers.clear()]:')
numbers = [0, 1, 2, 3, 4]
print('Original list \'numbers\':', numbers)
numbers.clear()
print('Cleared list \'numbers\':', numbers)

"""
> list.INDEX(x, [start, [end]]) - Returns the index position of the value 'x' in the
  ‾‾‾‾‾‾‾‾‾‾          given list. Optional arguments [start] and [end] are interpreted
                      as in SLICE notation, used to limit the search to a particular
                      subsequence of the list. If used, the returned index value is
                      computed relative to the beginning of the full sequence rather
                      than the [start] argument. Raises a ValueError if there is no
                      such item in the list or given range.
"""
print('\n> Find the index position of the value \'3\' to the list \'numbers\' = '
      '[1, 2, 3, 4, 5] by\n  using [numbers.index(3)]:')
numbers = [1, 2, 3, 4, 5]
print('Index position of value \'3\' in \'numbers\':', numbers.index(3))

"""
> list.COUNT(X) - Returns the number of times the value 'x' appears in the  given list.
  ‾‾‾‾‾‾‾‾‾‾
"""
print('\n> Count the times the value \'0\' appears on the list \'numbers\' '
      '= [0, 1, 0, 2, 3] by\n  using [numbers.count(0)]:')
numbers = [0, 1, 0, 2, 3]
print('Times the value \'0\' appears in \'numbers\':', numbers.count(0))

"""
> list.SORT() - Allows to either sort a String-only List in alphabetical order [A -> Z],
  ‾‾‾‾‾‾‾‾‾           or sort a Numbers-only List in ascending order [1 -> 10].
                      The [list.SORT()] method can take arguments; LOOK UP 'SORTED'
                      BUILT-IN FUNCTION FOR EXPLANATION.           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
print('\n> Sort the list \'names\' = [\'Tom\', \'Alan\', \'Gary\'] by using '
      '[names.sort()]:')
names = ['Tom', 'Alan', 'Gary']
names.sort()
print('Sorted list \'names\':', names)
print('\nNow sort the list \'numbers\' = [3, 1, 0, 2] by using [numbers.sort()]:')
numbers = [3, 1, 0, 2]
numbers.sort()
print('Sorted list \'numbers\':', numbers)

"""
> list.REVERSE() - Allows to reverse the order of the values in the given list, without
  ‾‾‾‾‾‾‾‾‾‾‾‾        any sorting involved. If wanted to, for example, get a numbers
                      list sorted in descending order, the list fist has to sorted and
                      then reversed. The [list.REVERSE()] method doesn't take any
                      arguments.
"""
print('\n> Reverse the order of all values in the list \'numbers\' = [6, 2, 4, 0, 8] '
      'by using [numbers.reverse()]:')
numbers = [6, 2, 4, 0, 8]
print('Original list \'numbers\':', numbers)
numbers.reverse()
print('Reversed list \'numbers\':', numbers)
print('\nNow sort all values in the list \'numbers\' = [6, 2, 4, 0, 8] in descending '
      'order by using\n[numbers.sort()], and then reversing the order by using '
      '[numbers.reverse()]:')
numbers = [6, 2, 4, 0, 8]
print('Original list \'numbers\':', numbers)
numbers.sort()
numbers.reverse()
print('Sorted and reversed list \'numbers\':', numbers)
"""
> list.COPY() - Creates a SHALLOW COPY of the given list, which can be stored in a
  ‾‾‾‾‾‾‾‾‾           different variable. Creating a Shallow-Copy, means that the new
                      list will have a different "ID" from the original, and if any
                      values were to be changed in any way, in any of them, the other
                      will remain untouched.
"""
print('\n> Copy the list \'numbers\' = [0, 1, 2, 3, 4] into the variable \'new\' by '
      'using [new = numbers.copy()],\nthen reverse ONLY the copy list, showing '
      'the original stayed untouched.')
numbers = [0, 1, 2, 3, 4]
print('Original list \'numbers\':', numbers)
new = numbers.copy()
print('Copy list \'new\':', new)
print('Now \'new\' is reversed and both lists are printed again:')
new.reverse()
print('Original list \'numbers\':', numbers)
print('Reversed copy list \'new\':', new)

"""
> LEN(list) - Generic Built-in function used to count index positions in Strings or
  ‾‾‾                 certain iterations, such as lists. In this case, the [LEN(x)]
                      function would be used to get the amount of index positions
                      (number of individual values or items) in the list 'x' as the
                      returned numerical value.
"""
print('\n> Find out the length of the list \'numbers\' = [0, 1, 2, 3, 4] by using '
      '[len(numbers)]:')
numbers = [0, 1, 2, 3, 4]
print('Length of list \'numbers\':', len(numbers))

"""
> SLICE --> list[x:y] - Slice operations come from the generic Built-in function
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾      [slice()], which has hundreds of uses. One of them, is to delimit
                      portions of a list to either be printed, modified, deleted,
                      calculated, indexed, etc.
                      
                      The first argument 'x', expresses the intention to count FROM
                      index position 'x', COUNTING 'x'. This argument can be either
                      positive (count starts at the beginning of the list) or negative
                      (count starts at the back of the list).
                      
                      The second argument 'y', expresses the intention to count UP TO
                      index position 'y', NOT COUNTING 'y'. This argument can also be
                      either positive or negative (counting from the beginning of the
                      list or the back, respectively).
                      
                      If a colon [:] was used without any numeric values as arguments
                      or parameters, no range would be determined, and the Python
                      interpreter would perform the requested action with a shallow
                      copy of the quoted list.
"""
print('\n> Lets use the base list \'letters\' = [\'a\', \'b\', \'c\', \'d\', \'e\'].')
letters = ['a', 'b', 'c', 'd', 'e']
print('List \'letters\' =', letters)
print('Now, print letters \'b\', \'c\' and \'d\' by using [letters[1:4]]')
print(letters[1:4])
print('\nNow, only print the last 2 values by using [letters[-2:]')
print(letters[-2:])
print('\nNow, lets change \'a\' and \'b\' for \'A\' and \'B\', respectively, by\nusing '
      '[letters[:2] = [\'A\', \'B\']]')
letters[:2] = ['A', 'B']
print(letters)

"""
                        LIST NESTING & NESTED LISTS / 2D LISTS
                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Lists are a very versatile Data type, so much that we can make a list out of other
lists, which is called 'LIST NESTING' and the resulting list would be a 'NESTED LIST'.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('--NESTED LISTS--')
print('\nLets create 2 lists, one for all vowels and one for the first five '
      'consonants.')
print('\'vowels\' = [\'a\', \'e\', \'i\', \'o\', \'u\']')
print('\'consonants\' = [\'b\', \'c\', \'d\', \'f\', \'g\']')
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g']
print('\nNow, lets create a \'letters\' list by nesting both \'vowels\' and '
      '\'consonants,\nby defining \'letters\' as a sum of both lists: '
      '\'letters = [vowels] + [consonants]\'')
print('--> Note that if no brackets were put around each list, the \'letters\' list '
      'would just be\na list of all values from \'vowels\' and all values from '
      '\'consonants\', all in a single list.')
letters = [vowels] + [consonants]
print('\nletters =', letters)

"""
To index a value in a Nested List, we must inter 2 values in the brackets. The first one
to identify the Inner List, and the second one to identify the index of the value in
said Inned List (in this case, just 2 values as there are just 2 lists within a list,
but if it was a Nested List of Nested Lists, it would take as many values as levels in
the List).
"""
# EXAMPLE:
print('')
print('If we were to Index the letter \'d\', we should first index the list where '
      'the value \'d\' is located,\nand then the index position of the value \'d\' '
      'within that list, as follows:')
print('\n--> print(letters[2][3])')
print('Value \'d\' in \'letters\' -->', letters[1][2])

"""
                                        2D LISTS
                                        ‾‾‾‾‾‾‾‾
Another way of understanding Nested Lists, is by seeing them as 2D Lists. We can achieve
this by building the main Nested List as an in-file grid, like an Excel file. To do so,
the nested must be written by separating each Inner List, placing them in a different
row.

- EXAMPLE:
letters = [
    ['a', 'e', 'i', 'o', 'u'],
    ['b', 'c', 'd', 'f', 'g']
]

This "grid" represents the exact same Nested List used in the previous example, but
seen as a 2D List. In this case, we name the variable and define it as a list by
opening the first bracket. Then, we start a new line where the first list is entered
(between brackets as well), and we separate it with a comma [,] from the next row.
We follow the procedure by creating the next list just like the first one, and if no
further "rows" (Inner Lists) are created, no comma [,] is needed at its end. Finally,
we close the last bracket of the main Nested List in a new row.

Now, individual values can be looked as items in a grid, and their index positions as
coordinates. Before, we used letters[x][y] as in 'index-list' + 'index-value', and now
it would be the same, but with the exception that we can look at as 'row' + 'column'
(remember ALL index counts start at ZERO [0]).

So, we already got the value 'd' by entering the indexes [1][2]. Now, if we were to get
the value 'o', for example, we could look at it as 'row [0]' + 'column [3]'.
"""
# EXAMPLE:
print('')
print('--> print(letters[0][3])')
print('Value \'o\' in \'letters\' -->', letters[0][3])
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
