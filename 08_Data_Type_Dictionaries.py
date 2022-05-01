"""
                                  OTHER DATA TYPES
                                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> LISTS
> TUPLES
> SETS
> DICTIONARIES
> CLASSES / OBJECTS

                                    DICTIONARIES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾
Another ITERABLE Data type, a structure that allows to store information in 'Key-Value'
pairs. Like a real dictionary, this one has a "Word -→ Meaning" structure, but those
terms are called 'Keys' and 'Values'. Keys always have to be UNIQUE.

Sometimes found in other languages as "Associative Memories" or "Associative Arrays",
Dictionaries, unlike sequences which are indexed by a range of numbers, are indexed by
immutable Keys.

Keys can be made of Strings, Numbers, or Tuples. Tuples can be used as Keys if they
contain only Strings, Numbers or Tuples, if it contains any mutable object, it cannot
be used as a Dictionary Key. Lists cannot be used as Keys either, since they can be
modified in place using index and slice assignments, or methods like [append()] and
[extend()].

Dictionaries may be constructed in several ways:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1 > Define a variable with its value between braces [{}], separating all individual
[Key : Value] pairs with a comma [,].
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create Dictionary \'Months\' by defining it as a variable:\n'
      '\'Months1\' = {\'Jan\': \'January\', \'Feb\': \'February\'}'
      '\n         OR\n\''
      'Months2\' = {\n'
      '     \'Jan\': \'January\',\n'
      '     \'Feb\': \'February\',\n'
      '     \'Mar\': \'March\',\n'
      '     \'Apr\': \'April\'\n}')
Months1 = {'Jan': 'January', 'Feb': 'February'}
Months2 = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April'
}
print('')
print('Now print them out:')
print('Months1 -->', Months1)
print('Months2 -->', Months2)

"""
2 > Using the Type Constructor [dict(x)] (built-in dictionary-creating function),
and entering a list of Key-Value tuples as arguments.
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create Dictionary \'Numbers\' by using the built-in function [dict()]:')
print('\'Numbers\' = dict([(1, \'One\'), (2, \'Two\'), (3, \'Three\')])')
Numbers = dict([(1, 'One'), (2, 'Two'), (3, 'Three')])
print('')
print('Now print it out:')
print('Numbers -->', Numbers)

"""
                                DICTIONARY METHODS
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Dictionaries have a set of built-in methods, functions and operators that can be used
to either get information from a Dictionary, modify or add new values or key-value
pairs, or to merge 2 or more different Dictionaries, for example.

Built-in Dictionary methods & operations:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> dict.CLEAR() - Removes all elements from the called Dictionary. Takes no arguments.
  ‾‾‾‾‾‾‾‾‾‾‾‾
"""
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Clear Dictionary \'Days\' by using [Days.clear()]:')
print('\'Days\' = {\'Mon\': \'Monday\', \'Tue\': \'Tuesday\', \'Wed\': \'Wednesday\'}')
Days = {
    'Mon': 'Monday',
    'Tue': 'Tuesday',
    'Wed': 'Wednesday'
}
print('Print Dictionary \'Days\' -->,', Days)
Days.clear()
print('[Days.clear()]. Cleared Dictionary \'Days\' -->', Days)

"""
> dict.COPY() - Returns a copy of the called Dictionary. Takes no arguments.
  ‾‾‾‾‾‾‾‾‾‾‾
"""
print('\nCopy Dictionary \'Days\' into variable \'New\' by using [New = Days.copy()]:')
print('\'Days\' = {\'Mon\': \'Monday\', \'Tue\': \'Tuesday\', \'Wed\': \'Wednesday\'}')
Days = {
    'Mon': 'Monday',
    'Tue': 'Tuesday',
    'Wed': 'Wednesday'
}
print('[New = Days.copy()]')
New = Days.copy()
print('Print Dictionary \'New\' -->', New)

"""
> DEL dict[x] - General [DEL] function used to remove the Key 'x' from the called
  ‾‾‾‾‾‾‾‾‾‾‾         Dictionary. Raises a KeyError if the Key 'x' is not found.
"""
print('\nDelete Key \'2\' from Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('[del Numbers[2]]')
del Numbers[2]
print('Now print modified Dictionary \'Numbers\' -->', Numbers)
"""
> DICT.FROMKEYS(x, y) - Create a new Dictionary with keys from 'x' values set to 'y'.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ Values default to [None] if argument 'y' is not given.
                      
                      Value 'x' has to be an iterable Data type, like a List or a
                      Sequence/Set, where each individual item will be taken as a key.
                      'y', however, can be of any Data type. It could be a manually
                      written String in the method argument, or it could be a variable
                      containing String, a Number, or an iterable Data Type.
"""
print('\nCreate Dictionary \'Numbers\' with items from List \'Nums\' as keys:')
print('\'Nums\' = [0, 1, 2, 3, 4, 5]')
Nums = [0, 1, 2, 3, 4, 5]
print('[Numbers = dict.fromkeys(Nums)] -- (No \'value\' argument was given so all '
      'values will default to [None])')
Numbers = dict.fromkeys(Nums)
print('Print Dictionary \'Numbers\' -->', Numbers)

print('\nNow create Dictionary \'Days\' with items from List \'days\' as keys:')
print('\'days\' = [\'Monday\', \'Tuesday\', \'Wednesday\']')
days = ['Monday', 'Tuesday', 'Wednesday']
print('[Days = dict.fromkeys(days, \'Weekday\')]')
Days = dict.fromkeys(days, 'Weekday')
print('Print Dictionary \'Days\' -->', Days)

"""
> dict.GET(x, y) - Returns the value for the key 'x' in the called Dictionary. If there
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾      is no key 'x' or it doesnt have an assigned value, returns the
                      default value 'y'. If default value 'y' is not given, returns
                      [None], so that this method never raises a KeyError. 
"""
print('\nGet value for key \'2\' in Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers.get(2)] -->', Numbers.get(2))

print('\nNow try to get value for key \'5\' in the same Dictionary \'Numbers\':')
print('Print [Numbers.get(6)] -->', Numbers.get(6))

"""
> dict.ITEMS() - Returns a List of individual key-value Tuples in the called Dictionary.
  ‾‾‾‾‾‾‾‾‾‾‾‾        Takes no arguments.
"""
print('\nGet List of key-values Tuples from the same Dictionary \'Numbers\':')
print('Print [Numbers.items()] -->', Numbers.items())

"""
> [key] in [x] - Returns the Boolean value [True] if the Key 'key' is present in the
  ‾‾‾‾‾‾‾‾‾‾‾‾        Dictionary 'x', [False] otherwise.
"""
print('\nCheck whether the Key \'2\' exists in Dictionary \'Numbers\' o not:')
print('Print [2 in Numbers] -->', 2 in Numbers)

print('\nNow check whether the Key \'6\' exists in Dictionary \'Numbers\' o not:')
print('Print [6 in Numbers] -->', 6 in Numbers)

"""
> [key] not in [x] - Opposite to the previous case, returns [True] if the Key 'key' is
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    NOT present in the Dictionary 'x', [False] otherwise.
"""
print('\nCheck whether the Key \'2\' exists in Dictionary \'Numbers\' o not:')
print('Print [2 not in Numbers] -->', 2 not in Numbers)

print('\nNow check whether the Key \'6\' exists in Dictionary \'Numbers\' o not:')
print('Print [6 not in Numbers] -->', 6 not in Numbers)

"""
> dict.KEYS() - Returns a List of the called Dictionary's Keys. Takes no arguments.
  ‾‾‾‾‾‾‾‾‾           
"""
print('\nGet a List of the Keys in Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers.keys()] -->', Numbers.keys())

"""
> LIST(x) - Similar to [dict.KEYS()], but in stead of just returning a List of Keys, it
  ‾‾‾‾                CREATES one in a different variable.
"""
print('\nCreate a List with the Keys in Dictionary \'Numbers\':')
print('[Number_Keys = list(Numbers)]')
Number_Keys = list(Numbers)
print('Print Number_Keys -->', Number_Keys)

"""
> LEN(x) - General function used to to get the number of items in the Dictionary 'x'.
  ‾‾‾                 In this case, items are all Dictionary's Key-Value pairs.
"""
print('\nGet the length of previously used Dictionary \'Numbers\':')
print('Print [len(Numbers)] -->', len(Numbers))

"""
> dict.POP(x, y) - Removes the Key 'x' from the called Dictionary, and returns its
  ‾‾‾‾‾‾‾‾            value. If the Key 'x' is not in the Dictionary, Python interpreter
                      returns 'y' as the default value. If 'y' is not given and the key
                      'x' is not in the Dictionary, a KeyError is raised.
"""
print('\nPop Key \'2\' from previously used Dictionary \'Numbers\':')
print('Print [Numbers.pop(2)] -->', Numbers.pop(2))
print('Now print modified Dictionary \'Numbers\' -->', Numbers)

print('\nNow try to pop Key \'6\' from previously used Dictionary \'Numbers\':')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers.pop(6, \'Six\')] -->', Numbers.pop(6, 'Six'))
print('Print \'modified\' Dictionary \'Numbers\' -->', Numbers)

"""
> dict.POPITEM() - Removes and returns the last entered Key-Value pair in the called
  ‾‾‾‾‾‾‾‾‾‾‾‾        Dictionary. If the Dictionary is empty and [dict.POPITEM()] is
                      used, a KeyError will be raised. Takes no arguments.
"""
print('\nPop and return last Key from Dictionary \'Numbers\':')
print('Print [Numbers.popitem()] -->', Numbers.popitem())
print('Now print modified Dictionary \'Numbers\' -->', Numbers)

"""
> dict.SETDEFAULT(x, y) - If the Key 'x' is ub the called Dictionary, return its value.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾     Otherwise, insert Key 'x' paired with the value 'y', and return
                      'y'. If 'y' is not given, it defaults to [None].
"""
print('\nReturn value for Key \'2\' from Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers.setdefault(2, \'ASDF\')] -->', Numbers.setdefault(2, 'ASDF'))
print('Python returns \'Two\' as the Key \'2\' is present in the Dictionary and '
      'already has a corresponding value.')

print('\nNow try to return value for Key \'5\' from Dictionary \'Numbers\':')
print('Print [Numbers.setdefault(5, \'Five\')] -->', Numbers.setdefault(5, 'Five'))
print('Now print the Dictionary \'Numbers\' -->', Numbers)
print('Note that the Key \'5\' and its value \'Five\' were added, since the pair '
      'was not found with the [dict.SETDEFAULT()] method.')

"""
> dict.UPDATE(...) - Updates the give Key-Value pairs from the called Dictionary.
  ‾‾‾‾‾‾‾‾‾‾‾         Given argument/s can be manually inserted Key-Value pairs as
                      [dict.UPDATE(1= 'One', 2= 'Two')], an iterable of Key-Value pairs
                      (as Tuples or iterables of lengths two), or another Dictionary.
                      If the called Dictionary already has Keys named the same as the
                      argument Dictionary or inserted Keys, the values for those
                      Keys in the called one will be replaced with the values assigned
                      in the argument.
                      
                      Can be done by using 'dict. | [...]' (similar to 'Merge').
"""
print('\nUpdate Dictionary \'Days\' with values from Dictionary \'Days2\':')
print('\'Days\' = {\'Mon\':\'Monday\', \'Tue\':\'Tuesday\', \'Wed\':\'Wednesday\'}')
print('\'Days2\' = {\'Mon\':1, \'Tue\':2, \'Wed\':3}')
Days = {'Mon':'Monday', 'Tue':'Tuesday', 'Wed':'Wednesday'}
Days2 = {'Mon':1, 'Tue':2, 'Wed':3}
print('Print \'Days\' -->', Days)
print('Print \'Days2\' -->', Days2)
print('[Days.update(Days2)]')
# noinspection PyTypeChecker
Days.update(Days2)
print('Now print updated Dictionary \'Days\' -->', Days)

"""
> dict.VALUES() - Returns a List of all the called Dictionary's Values. Takes no
  ‾‾‾‾‾‾‾‾‾‾‾         arguments.
"""
print('\nGet a List of the Values in Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers.values()] -->', Numbers.values())

"""
> SORTED(x) - Similar to [LIST(dict)], returns and/or creates a SORTED List of Keys, in
  ‾‾‾‾‾‾              alphabetical / ascending order.
"""
print('\nGet a sorted list of Keys from the Dictionary \'Letters\':')
print('\'Letters\' = {\'A\':\'a\', \'D\':\'d\', \'B\':\'b\', \'C\':\'c\'}')
Letters = {'A':'a', 'D':'d', 'B':'b', 'C':'c'}
print('[sorted_letters = sorted(Letters)]')
sorted_letters = sorted(Letters)
print('Print List of sorted Keys -->', sorted_letters)

"""
> x[key] - Returns the value of the Key 'key' in the called Dictionary 'x'. Raises a
  ‾‾‾‾‾‾              KeyError if 'key' is not in the Dictionary 'x'.
"""
print('\nPrint the value for Key \'2\' from Dictionary \'Numbers\':')
print('\'Numbers\' = {1: \'One\', 2: \'Two\', 3: \'Three\', 4: \'Four\'}')
Numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four'}
print('Print [Numbers[2] -->', Numbers[2])

"""
> x[key] = y - Allows to set a new value 'y' to the Key 'key' in the called Dictionary
  ‾‾‾‾‾‾‾‾‾‾          'x'. If 'key' is not in Dictionary 'x', it is added and given the
                      value 'y'.
"""
print('\nChange value of the Key \'5\' in the Dictionary \'Numbers\', but if there '
      'is no Key \'5\' in \'Numbers\',\ncreate it and assign the value \'Five\' to it:')
print('[Numbers[5] = \'Five\']')
Numbers[5] = 'Five'
print('Print Dictionary \'Numbers\' -->', Numbers)

"""
> dic. | x - Merge operation, used to create a new Dictionary with the merged Keys and
  ‾‾‾‾‾‾‾‾            Values from both the called Dictionary and the Dictionary 'x'.
                      Values from 'x' take priority when both dictionaries share Keys.
"""
print('\nMerge Dictionary \'Days1\' with the Dictionary \'Days2\':')
print('\'Days1\' = {\'Mon\':1, \'Tue\':2, \'Wed\':3, \'Thu\':4}')
print('\'Days2\' = {\'Thu\':1, \'Fri\':2, \'Sat\':3, \'Sun\':4}')
Days1 = {'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4}
Days2 = {'Thu':1, 'Fri':2, 'Sat':3, 'Sun':4}
print('Print \'Days1\' -->', Days1)
print('Print \'Days2\' -->', Days2)
print('Days3 = [Days1 | Days2]')
Days3 = [Days1 | Days2]
print('Now print merge Dictionary \'Days3\':')
print(Days3)
print('--> Note that the Key \'Thu\' got assigned the Value \'1\' from the Dictionary '
      '\'Days2\', as it has\npriority in the merge.')
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
