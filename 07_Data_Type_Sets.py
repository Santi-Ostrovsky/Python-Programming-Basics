"""
                                    OTHER DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> LISTS
> TUPLES
> SETS
> DICTIONARIES
> CLASSES / OBJECTS

                                         SETS
                                         ‾‾‾‾
Sets and FrozenSets are another ITERABLE / sequence Data type, like Lists or Tuples,
that allow to store individual pieces of data of different Data types, but cannot
store: more than one other iteration inside, or duplicate items.

Sets store an unordered, unchangeable and un-indexed collection of data.
Note: 'unchangeable' doesn't mean that the set cannot be shortened or appended (add
or remove items inside), but that values that already exist inside cannot be modified.

Sets are mainly used to find unique elements in other variables like Strings, Lists,
Tuples, or Dictionaries.

- EXAMPLE: Let's say we have the String [text = 'Hello, how are you?']. A quick way to
find all unique elements in the string 'text', is to make a Set with it.

>>> text = 'Hello, how are you?'
>>> print(set(text))
----→ {'H', '?', 'e', 'r', 'h', 'a', 'y', 'l', 'o', 'u', 'w', ',', ' '}

In this example, the Python console returned all individual (unique) characters in the
string 'text', in no particular order. Notice that both 'H' and 'h' are present in the
returned Set, and that is because casing transform characters into others, with a
different "character ID".

FrozenSets are an immutable version of Sets. Since FrozenSets are immutable and
hashable, they may be used as dictionary keys or as a member value on another Set.

Sets may be constructed in several ways:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1 > Define a variable with its value between braces [{}], separating all individual
values with a comma [,]. This way of constructing a Set is not very useful, since it
doesn't serve the purpose of identifying unique elements on another variable, and will
only perform said task on the manually entered data (either string, list, tuple, etc.).
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create set \'example\' by defining it as a variable: '
      '\'example\' = {0, 1, 0, 2, 1, 3, 2, 1, 3}')
example = {0, 1, 0, 2, 1, 3, 2, 1, 3}
print('')
print('Now print it out:')
print('Set \'example\' :', example)

"""
2 > Using a Set comprehension method to automatically create a Set with instructed
values --- [SEEN IN LATER FILES].
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create Set \'Set_of_squares\' by entering: '
      'Set_of_squares = {x ** 2 for x in range(10)}')
Set_of_squares = {x ** 2 for x in range(10)}
print('')
print('Now print it out:')
print('Set_of_squares :', Set_of_squares)

"""
3 > Using the Type Constructor [set(x)] (built-in set-creating function)
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create set \'unique_values\' by using the built-in function [set()], to make '
      'a set out of a string:\n'
      'text = \'Banana\'\n'
      'unique_values = set(text)')
text = 'Banana'
unique_values = set(text)
print('')
print('Now print it out:')
print('unique_values :', unique_values)

"""
4 > When creating an empty Set, parentheses [()] have to be used when defining the
variable, instead of braces [{}]. The latter creates an empty Dictionary, which cannot
change type after being defined (Tuples can).

                  WRONG                   │           RIGHT
      ────────────────────────────────────┼────────────────────────────────────
            >>> NewSet = {}               │      >>> NewSet = ()           
            >>> print(type(NewSet))       │      >>> print(type(NewSet))   
            ----→ <class 'dictionary'>    │      ----→ <class 'tuple'>


                                    SET OPERATIONS
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Like other  data collections, Sets support functions and statements like ['x' in set], 
[len(set)], ['x' in set] and ['x' not in set]. Other types of functions and methods can
be used to, like the String method [str.JOIN()], to make a String out of all values in
a Set, for example.

Sets, support "mathematical" operations that allow the program to find unique elements
in 2 or more different sets, find unique elements in common in 2 or more sets, determine
if all values in a set 'x' are present in a different one 'y' ('x' subset of 'y'), etc.

For instance, if in doubt of what type a piece of data or variable is, the function
[type(x)] can be used to return the Data type of 'x'.

- EXAMPLE: We don't know if the variable 'test = {1, 2, 3}' corresponds to the Set Data
type, or some other, so we ask the Python interpreter to give us that information by
either printing it or returning it to the code as a boolean value:

>>> test1 = {1, 2, 3}
>>> print(type(test1))
----→ <class 'set'>
      -- OR --
>>> test2 = {1, 2, 3}
>>> if type(test2) is set:     [SEEN IN FUTURE FILES]
>>> ...

BUILT-IN SET OPERATIONS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> set.ADD(x) - Allows to add the value 'x' to the set (at no particular position, since
  ‾‾‾‾‾‾‾      Sets are unordered collections of data).
"""
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Add the value \'5\' to the Set \'NumSet = {0, 1, 1, 2, 1, 3}\' by '
      'using [NumSet.add(5)]:')
NumSet = {0, 1, 1, 2, 1, 3}
print('Print \'NumSet\' before being modified -->', NumSet)
NumSet.add(5)
print('Now print the modified set \'NumSet\' -->', NumSet)

"""
> set.CLEAR() - Used to remove all objects inside the Set. Takes no arguments.
  ‾‾‾‾‾‾‾‾‾
"""
print('\nClear the Set \'NumSet = {0, 1, 1, 2, 1, 3}\' by '
      'using [NumSet.clear()]:')
NumSet = {0, 1, 1, 2, 1, 3}
print('Print \'NumSet\' before being cleared -->', NumSet)
NumSet.clear()
print('Now print the cleared set \'NumSet\' -->', NumSet)

"""
> set.COPY() - Returns a copy of the Set to either by used as value for another variable
  ‾‾‾‾‾‾‾‾     or in a function. Takes no arguments.
"""
print('\nCopy the Set \'NumSet = {0, 1, 1, 2, 1, 3}\' into the variable \'New\' by '
      'using [New = NumSet.copy()]:')
NumSet = {0, 1, 1, 2, 1, 3}
print('Print \'NumSet\' -->', NumSet)
New = NumSet.copy()
print('Now print the new Set \'New\' -->', NumSet)

"""
> set.DIFFERENCE(...) - Returns a Set containing the difference between to or more Sets.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾             
               If 2 Sets were looked at in a Venn diagram, 'SetA' being circle 'A',
               'SetB' being circle 'B', and the intersection between both circles being
               all values both sets have in common, we could use the [set.DIFFERENCE()]
               operation to get all values from SetA without those in common with SetB
               and vice-versa.
               
               > For SetA - SetB --> [SetA.difference(SetB)]
               > For SetB - SetA --> [SetB.difference(SetA)]
               
               If we wanted to get all values in a Set, without including values present
               in more that one other set, we must add those sets in between parentheses
               separated by a comma [,] (example: [setA.difference(setB, setC, setD)]).
"""
print('\nGet the difference in \'set1\', from sets \'set2\' and \'set3\'.')
set1 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
set2 = {10, 15, 25, 55, 92, 30, 50}
set3 = {70, 75, 95, 68, 46, 90, 99}
print('Print \'set1\' -->', set1)
print('Print \'set2\' -->', set2)
print('Print \'set3\' -->', set3)
print('>>> [set1.difference(set2, set3)] -->', set1.difference(set2, set3))

"""
> set.DIFFERENCE_UPDATE(...) - Like [set.DIFFERENCE()], this one is used to find the
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾difference between 2 or more Sets, and permanently remove all
               items in common with the other Sets included in the function.
"""
print('\nGet the difference_update in \'set1\', from sets \'set2\' and \'set3\'.')
set1 = {10, 15, 20, 25, 30, 35, 40, 45, 50}
set2 = {15, 25, 35}
set3 = {30, 45, 55}
print('Print \'set1\' -->', set1)
print('Print \'set2\' -->', set2)
print('Print \'set3\' -->', set3)
set1.difference_update(set2, set3)
print('>>> [set1.difference_update(set2, set3)] \nNew \'set1\' -->', set1)

"""
> set.DISCARD(x) - Removes the specified item 'x' from the Set.
 ‾‾‾‾‾‾‾‾‾‾‾‾
"""
print('\nDiscard the value \'3\' from the Set \'Nums = {0, 1, 2, 3, 4, 5}\' by '
      'using [Nums.discard(3)]:')
Nums = {0, 1, 2, 3, 4, 5}
print('Print Set \'Nums\' -->', Nums)
Nums.discard(3)
print('>>> [Nums.discard(3)] \nNew Set \'Nums\' -->', Nums)

"""
> set.INTERSECTION(...) - Opposite to the function [set.DIFFERENCE()], is used to create
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ a Set with the 'intersection' values of 2 or more Sets.
               
               In the Venn diagram example used then, if we were to use
               [SetA.intersection(SetB)], instead printing the SetA without the values
               in the SetB, we would be printing only those values SetA has in common
               with SetB.
"""
print('\nGet the intersection values of Sets \'SetA\' and \'SetB\'by '
      'using [SetA.intersection(SetB)]:')
SetA = {0, 1, 2, 3, 4, 5, 6}
SetB = {3, 4, 5, 6, 7, 8, 9}
print('\'SetA\' -->', SetA)
print('\'SetB\' -->', SetB)
print('>>> [SetA.intersection(SetB)] -->', SetA.intersection(SetB))

"""
> set.INTERSECTION_UPDATE(...) - Opposite to the function [set.DIFFERENCE_UPDATE()],
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ is used to find the intersection between 2 or more Sets
               (items in common), and permanently modify the operated Set to have as
               values, said intersection.
"""
print('\nGet the intersection_update in \'SetA\', from \'SetB\'.')
SetA = {0, 1, 2, 3, 4, 5, 6}
SetB = {3, 4, 5, 6, 7, 8, 9}
SetC = {4, 5, 6, 7, 8, 9, 10}
print('Print \'SetA\' -->', SetA)
print('Print \'SetB\' -->', SetB)
print('Print \'SetC\' -->', SetC)
SetA.intersection_update(SetB, SetC)
print('>>> [SetA.intersection_update(SetB, SetC)] \nNew \'SetA\' -->', SetA)

"""
> set.ISDISJOINT(x) - Returns whether 2 Sets have an intersection or not. The returned
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾ value will be a Boolean ( [True] / [False] ). Returns [True] if the
               Set has no elements in common with 'x', [False] otherwise.
"""
print('\nFind out if \'Set1\' and \'Set2\' are disjoint:')
Set1 = {0, 1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7, 8, 9}
print('Print \'Set1\' -->', Set1)
print('Print \'Set2\' -->', Set2)
print('>>> [Set1.isdisjoint(Set2)] -->', Set1.isdisjoint(Set2))

print('\nNow find out if \'set_a\' and \'set_b\' are disjoint:')
set_a = {'Tom', 'Ally', 'Jack'}
set_b = {'John', 'Mark', 'Jim'}
print('Print \'set_a\' -->', set_a)
print('Print \'set_b\' -->', set_b)
print('>>> [set_a.isdisjoint(set_b)] -->', set_a.isdisjoint(set_b))

"""
> set.ISSUBSET(x) - Returns whether another Set contains the called Set in the function,
  ‾‾‾‾‾‾‾‾‾‾‾‾ or not. The returned value will be a Boolean ( [True] / [False] ).
               Returns [True] if the values of the called Set are present in 'x',
               [False] otherwise.
"""
print('\nFind out if \'Set1\' is a subset of \'Set2\':')
Set1 = {2, 3, 4, 5}
Set2 = {0, 1, 2, 3, 4, 5, 6, 7}
print('Print \'Set1\' -->', Set1)
print('Print \'Set2\' -->', Set2)
print('>>> [Set1.issubset(Set2)] -->', Set1.issubset(Set2))

print('\nNow find out if \'Set2\' is a subset of \'Set1\':')
Set1 = {2, 3, 4, 5}
Set2 = {0, 1, 2, 3, 4, 5, 6, 7}
print('Print \'Set1\' -->', Set1)
print('Print \'Set2\' -->', Set2)
print('>>> [Set2.issubset(Set1)] -->', Set2.issubset(Set1))

print('\nFind out if \'Set1\' is a superset of \'Set2\':')
"""
> set.ISSUPERSET(x) - Opposite so [set.SUBSET()], returns whether or not the called Set
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾ contains the values in 'x'. The returned value will be a Boolean
               ( [True] / [False] ). Returns [True] if the values in 'x' are present in
               the called Set, [False] otherwise.
"""
Set1 = {2, 3, 4, 5}
Set2 = {0, 1, 2, 3, 4, 5, 6, 7}
print('Print \'Set1\' -->', Set1)
print('Print \'Set2\' -->', Set2)
print('>>> [Set1.issuperset(Set2)] -->', Set1.issuperset(Set2))

print('\nNow find out if \'Set2\' is a superset of \'Set1\':')
Set1 = {2, 3, 4, 5}
Set2 = {0, 1, 2, 3, 4, 5, 6, 7}
print('Print \'Set1\' -->', Set1)
print('Print \'Set2\' -->', Set2)
print('>>> [Set2.issuperset(Set1)] -->', Set2.issuperset(Set1))

"""
> set.POP() - Removes a random item from the called Set. Takes no arguments.
  ‾‾‾‾‾‾‾
"""
print('\nPop an item out the Set \'ExampleSet\' = {30, 25, 30, 40, 45, 25}:')
ExampleSet = {30, 25, 30, 40, 45, 25}
print('Print \'ExampleSet\' -->', ExampleSet)
ExampleSet.pop()
print('>>> [ExampleSet.pop()]')
print('Now print the modified \'ExampleSet\' -->', ExampleSet)

"""
> set.REMOVE(x) - removes the specified item 'x' from the called Set.
  ‾‾‾‾‾‾‾‾‾‾
"""
print('\nRemove the item \'30\' from \'ExampleSet\' = {30, 25, 30, 40, 45, 25}:')
ExampleSet = {30, 25, 30, 40, 45, 25}
print('Print \'ExampleSet\' -->', ExampleSet)
ExampleSet.remove(30)
print('>>> [ExampleSet.remove(30)]')
print('Now print the modified \'ExampleSet\' -->', ExampleSet)

"""
> set.SYMMETRIC_DIFFERENCE(x) - Returns a Set with symmetric differences of only 2
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ Sets. It is similar to [set.DIFFERENCE()], but in stead of
               returning a Set with all values in A, without values in B, the returned
               Set will have all values present in A and B, but not in both.
               
               If 2 Sets were looked at in a Venn diagram, 'SetA' being circle 'A',
               'SetB' being circle 'B', and the intersection between both circles being
               all values both sets have in common, we could use the
               [set.SYMMETRIC_DIFFERENCE()] operation to get all values from SetA and
               SetB, that are NOT part of the intersection. 
"""
print('\nGet the symmetric difference from Sets \'SetA\' and \'SetB\'.')
SetA = {0, 1, 2, 3, 4, 5}
SetB = {3, 4, 5, 6, 7, 8}
print('Print \'SetA\' -->', SetA)
print('Print \'SetB\' -->', SetB)
print('>>> [SetA.symmetric_difference(SetB)] -->', SetA.symmetric_difference(SetB))

"""
> set.SYMMETRIC_DIFFERENCE_UPDATE(x) - Like [set.SYMMETRIC_DIFFERENCE()], this one is
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ used to find the symmetric difference between 2 Sets,
               but it permanently remove all items in common with the Set 'x'.
"""
print('\nGet the symmetric_difference_update from Sets \'SetA\' and \'SetB\'.')
SetA = {0, 1, 2, 3, 4, 5}
SetB = {3, 4, 5, 6, 7, 8}
print('Print \'SetA\' -->', SetA)
print('Print \'SetB\' -->', SetB)
SetA.symmetric_difference_update(SetB)
print('>>> [SetA.symmetric_difference_update(SetB)] \nNew \'SetA\' -->', SetA)

"""
> set.UNION(...) - Return a new Set with all elements inside argument Sets.
  ‾‾‾‾‾‾‾‾‾
"""
print('\nJoin Sets \'SetA\' and \'SetB\' in a new Set \'JoinedSets\'.')
SetA = {0, 1, 2, 3, 4, 5}
SetB = {3, 4, 5, 6, 7, 8}
print('Print \'SetA\' -->', SetA)
print('Print \'SetB\' -->', SetB)
JoinedSets = SetA.union(SetB)
print('>>> JoinedSets = SetA.union(SetB) \nNew Set \'JoinedSets\' -->', JoinedSets)
"""
> set.UPDATE(...) - Updates the contents of an existing Set, adding the values from
  ‾‾‾‾‾‾‾‾‾‾   all argument Sets.
"""
print('\nUpdate the contents of the Set \'Old\' with the sets \'New1\' and \'New2\':')
Old = {'a', 'b', 'c', 'a', 'd'}
New1 = {'a', 'e', 'i', 'o', 'u'}
New2 = {'b', 'c', 'd', 'g', 'h'}
print('Print \'Old\' -->', Old)
print('Print \'New1\' -->', New1)
print('Print \'New2\' -->', New2)
Old.update(New1, New2)
print('>>> [Old.update(New1, New2)] \nUpdated Set \'Old\' -->', Old)
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
