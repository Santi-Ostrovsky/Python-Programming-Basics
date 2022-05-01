"""
                                    MAIN DATA TYPES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> STRINGS: Alphanumeric values presented in single or double quotes [''], [""].
> NUMBERS: Numeric values presented without quotes.
> BOOLEAN: True / False values, that determine a quality on a statement.

                                       STRINGS
                                       ‾‾‾‾‾‾‾
Strings are taken as plane text. It is the default data type of user inputs in Python.
"""
# EXAMPLE STRINGS
print('')  # EMPTY STRING --> Will just print a blank line.
print('Hello World.')  # Displays 'Hello World.' in console.
print('Numbers can be strings too: 0123456789.')  # Numbers inside strings are just text.

"""
ESCAPE CHARACTERS --> In the middle of a string, we can use a Backslash [\] to tell the
Python interpreter to render the following symbol intro the console, literally, instead
of interpreting it as a new command in the line. (LOOK UP ALL ESCAPE CHARACTERS).
"""
# EXAMPLE STRINGS
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Hello, \'Santi\', welcome to Python.')  # Backslash was used before quotes to
print('')                                     # prevent the string from ending.

# Backslash + 'n' [\n] --> used to start a new line, just like "print('')".
print('Hello, this is a command used to...\n...start a new line')

"""
                                STRING CONCATENATION
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Strings and other Data types can be concatenated in a single line of code, either
using [,], [+], or a concatenation function/method. Here, we'll take a look at the
first two.

Comma [,] can be used to concatenate strings or other Data types, and will place a
whitespace in between, automatically.
"""
# EXAMPLES
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Concatenation examples (Comma):')
print('\nThe string \'I am\' and the number \'26\'.')
print('-->', 'I am', 26)
print('\nThe string \'I am 26\' and the string \'years old.\'')
print('\'I am 26\'', '\'years old.\'')

"""
Plus sign [+] can only be used to concatenate strings. So, if we wanted to concatenate a
string with another Data type, but couldn't use [,] for formatting reasons, we must first
convert other Data types into strings, by typing [str([data])], 'data' being the value of
a different Data type we want to concatenate. [+] will not place a space between the
concatenated strings, so those have to be added manually.
"""
# Example
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Concatenations examples (Plus sign):')
print('\nThe string \'I am\' and the number \'26\'.')
print('How this is done: \'I am \' + \'str(26)\'.')
print('I am ' + str(26))

"""
                                   STRING METHODS
                                   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
Functions or Methods are ways to create, modify, get information, format, or delete
pieces of data in the code. All basic functions are already pre-built in Python, but
some may be created by the programmer, which we'll see later.

Built-in String Methods (some take arguments in parentheses, others don't):
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.CAPITALIZE() - Returns a copy of the string with its first letter capitalized/
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾  titlecased, and the rest lowerscased.
"""
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('--STRING METHODS--')
print('\n> Capitalize the string \'hello\' by using [str.CAPITALIZE()]:')
print('hello'.capitalize())
"""                   
> str.CASEFOLD() - Returns a casefolded copy of the string for caseless matching. It
  ‾‾‾‾‾‾‾‾‾‾‾‾    is similar to lowercasing but more aggressive, since it removes
                  all case distinctions. For example, the German lowercase letter 'ß'
                  is equivalent to 'ss', but since its already lowercase, the method
                  [str.LOWER()] would do nothing to it, while [str.CASEFOLD()]
                  converts it to 'ss'.
"""
print('\n> Casefold the string \'HeLlO\' by using [str.CASEFOLD()]:')
print('HeLlO'.casefold())
"""                   
> str.CENTER(width,[fillchar]) - Center a string of length 'width'. Padding is done
  ‾‾‾‾‾‾‾‾‾‾      using the specified 'fillchar' (ASCII space by default). The
                  original string is returned if 'width' is less than or equal to
                  the length [len(str)] of the string.
"""
print('\n> Center the string \'Hello\' by using [str.CENTER(20)]:')
print('Hello'.center(20))
print('Now Center the string \'Hello\' by using [str.CENTER(20, \'-\')]:')
print('Hello'.center(20, '-'))
"""                                
> str.COUNT(sub,[start,[end]]) - Returns the number of non-overlapping occurrences of
  ‾‾‾‾‾‾‾‾‾       the substring 'sub' in the range [start, end]. Optional arguments
                  'start' and 'end' are interpreted as in slice notation.
"""
print('\n> Count the string \'Hello\' by using [str.COUNT(\'ll\')]:')
print('hello'.count('ll'))
"""
> str.ENCODE(encoding='utf-8', errors='strict') - LOOK UP FOR ENCODING PURPOSES.
  ‾‾‾‾‾‾‾‾‾‾                                      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.ENDSWITH(suffix,[start,[end]]) - Returns 'True' if the string ends with the
  ‾‾‾‾‾‾‾‾‾‾‾‾    specified suffix, otherwise returns 'False'. The suffix can also
                  be a tuple of suffixes to look for. Optional arguments 'start'
                  (test beginning at that position) and 'end' (stop comparing at
                  that position).
"""
print('\n> Check if the string \'Hello\' ends with \'o\' '
      'by using [str.endswith(\'o\')]:')
print('Hello'.endswith('o'))
"""                                      
> str.EXPANDTABS(tabsize=8) - LOOK UP FOR CONVERSION OF TAB-CHARACTERS TO SPACES.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.FIND(sub, [start, [end]]) - Returns the lowest index position in the string where
                  the  substring 'sub' is fount within the optional slice arguments
                  [start, end]. Returns '-1' if the substring 'sub' is not found in
                  the string.
"""
print('\n> Find \'e\'s index position in the string \'Hello\' '
      'by using [str.FIND(\'e\')]:')
print('Hello'.find('e'))
print('Now find \'o\'s index position in the string \'Hello\' '
      'by using [str.FIND(\'o\', 3)]:')
print('Hello'.find('o', 3))
"""
> str.FORMAT(*args, **kwargs) - Performs a string-formatting operation. The string on
  ‾‾‾‾‾‾‾‾‾‾      which this method is called can contain literal text or replacement
                  fields delimited by braces [{}]. Each replacement field contains
                  either the numeric index of a positional argument, or the name of a
                  keyword argument. Returns a copy of the string where each replacement
                  field is replaced with the string value of the corresponding argument.
                  STRING FORMATTING EXPLAINED LATER IN THE FILE.
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.FORMAT_MAP(mapping) - LOOK UP FOR FORMATTING MAPPING IN DICTIONARY SUBCLASSES.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.INDEX(sub, [start, [end]]) - Like str.FIND(), but raise ValueError when the
  ‾‾‾‾‾‾‾‾‾       substring is not found. (Opposite to [str.RINDEX()]).
"""
print('\n> Find \'e\'s index position in the string \'Hello\' '
      'by using [str.INDEX(\'e\')]:')
print('Hello'.index('e'))
"""
> str.ISALNUM() - Returns 'True' if all characters in the string are alphanumeric and
  ‾‾‾‾‾‾‾‾‾‾‾     there is at least one character, 'False' otherwise.
"""
print('\n> Check if the string \'Hello123\' is alphanumeric by using [str.ISALNUM()]:')
print('Hello123'.isalnum())
"""
> str.ISALPHA() - Returns 'True' if all characters in the string are alphabetic and
  ‾‾‾‾‾‾‾‾‾‾‾     there is at least one character, 'False' otherwise.
"""
print('\n> Check if the string \'Hello123\' is alphabetic by using [str.ISALPHA()]:')
print('Hello123'.isalpha())
print('Now check if the string \'Hello\' is alphabetic by using [str.ISALPHA()]:')
print('Hello'.isalpha())
"""
> str.ISASCII() - Returns 'True' if the string is empty or all characters in the string
  ‾‾‾‾‾‾‾‾‾‾‾     are ASCII, 'False' otherwise. LOOK UP ASCII CHARACTERS.
                                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.ISDECIMAL() - Returns 'True' if all characters in the string are decimal
  ‾‾‾‾‾‾‾‾‾‾‾‾‾   characters and there is at least one character, 'False' otherwise.
                  Decimal characters are those that can be used to form numbers in
                  base 10.
"""
print('\n> Check if the string \'Hello123\' is decimal by using [str.ISDECIMAL()]:')
print('Hello123'.isdecimal())
print('Now check if the string \'12345\' is decimal by using [str.ISDECIMAL()]:')
print('12345'.isdecimal())
"""
> str.ISDIGIT() - Returns 'True' if all characters in the string are digits and there
  ‾‾‾‾‾‾‾‾‾‾‾     is at least one character, 'False' otherwise. Digits include decimal
                  characters and digits that need special handling, such as the
                  compatibility superscript digits.
"""
print('\n> Check if the string \'Hello123\' is digit by using [str.ISDIGIT()]:')
print('Hello123'.isdigit())
print('Now check if the string \'12345\' is digit by using [str.ISDIGIT()]:')
print('12345'.isdigit())
"""
> str.ISIDENTIFIER() - Returns 'True' if the string is a valid identifier according to
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾the language definition. Some keywords may be 'None', 'and', 'if',
                  'lambda', 'import', 'while', 'def', 'return', etc.
                  LOOK UP LEXICAL ANALYSIS IDENTIFIERS, KEYWORDS AND SOFT KEYWORDS.
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.ISLOWER() - Returns 'True' if all cased characters in the string are lowercase
  ‾‾‾‾‾‾‾‾‾‾‾     and there is at least one cased character, 'False' otherwise.
"""
print('\n> Check if the string \'Hello\' is all lower case by using [str.ISLOWER()]:')
print('Hello123'.islower())
print('Now check if the string \'hello\' is all lower case by using [str.ISLOWER()]:')
print('hello'.islower())
"""
> str.ISNUMERIC() - Returns 'True' if all characters in the string are numeric
  ‾‾‾‾‾‾‾‾‾‾‾‾‾   characters and there is at least one character, 'False' otherwise.
                  Numeric characters include digit characters, and all characters that
                  had the Unicode numeric value property.
                  Numeric_Type=[Digit], [Decimal] or [Numeric].
"""
print('\n> Check if the string \'Hello123\' is all numeric '
      'by using [str.ISNUMERIC()]:')
print('Hello123'.isnumeric())
print('\n> Check if the string \'12345\' is all numeric '
      'by using [str.ISNUMERIC()]:')
print('12345'.isnumeric())
"""
> str.ISPRINTABLE() - Returns 'True' if all characters in the string are printable or
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ the string is empty, 'False' otherwise. Non-printable characters are
                  those defined in the Unicode character database as "Other" or
                  "Separator", excepting the ASCII space which is printable. Printable
                  characters are those which should not be escaped when the built-in
                  function [REPR(object)] is invoked on a string.
"""
print('\n> Check if the string \'Hello123\' is printable by using [str.ISPRINTABLE()]:')
print('Hello123'.isprintable())
"""
> str.ISSPACE() - Returns 'True' if there are only white spaces in the string and there
  ‾‾‾‾‾‾‾‾‾‾‾     is at least one character, 'False' otherwise.
"""
print('\n> Check if the string \'Hello, man\' is all space by using [str.ISSPACE()]:')
print('Hello, man'.isspace())
print('Now check if the string \' \' is all space by using [str.ISSPACE()]:')
print(' '.isspace())
"""
> str.ISTITLE() - Returns 'True' if the string is titlecased and there is at least one
  ‾‾‾‾‾‾‾‾‾‾‾     character, 'False' otherwise. For example, uppercase characters may
                  only follow uncased characters and lowercase characters may only
                  follow cased ones.
"""
print('\n> Check if the string \'Hello, man\' is a title by using [str.ISTITLE()]:')
print('Hello, man'.istitle())
print('Now check if the string \'Hello, Alfa\' is a title by using [str.ISTITLE()]:')
print('Hello, Alfa'.istitle())
"""
> str.ISUPPER() - Returns 'True' if all characters in the string are uppercase and
  ‾‾‾‾‾‾‾‾‾‾‾     there is at least one character, 'False' otherwise.
"""
print('\n> Check if the string \'Hello\' is all upper case by using [str.ISUPPER()]:')
print('Hello'.isupper())
print('Now check if the string \'HELLO\' is all upper case by using [str.ISUPPER()]:')
print('HELLO'.isupper())
"""
> str.JOIN(iterable) - Returns a string which is the concatenation of all digits in
  ‾‾‾‾‾‾‾‾       'iterable'. A TypeError will be raised if there are any non-string
                  values in 'iterable'.
"""
print('\n> Join the str. \'12345\' to the str. \'Hello\' by using [str.JOIN()]:')
print('12345'.join('Hello'))
"""
> LEN(str) - Function that returns the length of the given string, in index positions.
  ‾‾‾
"""
print('\n> Get the index length of the string \'Hello\' by using [LEN(str)]:')
print(len('Hello'))
"""
> str[X] - Function that returns a digit inside the string, at the given numeric index
  ‾‾‾             position 'x'. Index count starts at zero [0]. If the given numeric
                  index position 'X' is out of range (meaning it exceeds the string's
                  length, an IndexError will be raised.
"""
print('\n> Get the letter at index position \'4\' in the'
      'str. \'Hello\' by using [str[4]]]:')
print('Hello'[4])
"""
> str.INDEX(x) - Function that returns the first index position of the given substring
  ‾‾‾‾‾‾‾‾‾       'x' inside the string. If the given substring 'x' is not found in the
                  string, an ValueError will be raised.
"""
print('\n> Get the first index position of the letter \'l\' in the'
      'str. \'Hello\' by using [str.INDEX(\'l\')]:')
print('Hello'.index('l'))
"""
> str.LJUST(width, [fillchar]) - Returns the string left-justified in a string of
  ‾‾‾‾‾‾‾‾‾       length 'width'. The original string will be returned if 'width' is
                  less than or equal to the length [len(str)] of the string. Padding
                  is done using the specified 'fillchar' argument.
                  (Opposite to [str.RJUST()]).
"""
print('\n> Justify the string \'Hello\' to the left by using [str.LJUST(20)]:')
print('Hello'.ljust(20))
print('Now justify the string \'Hello\' to the left by using [str.LJUST(20, \'-\')]:')
print('Hello'.ljust(20, '-'))
"""
> str.LOWER() - Returns a copy of the string with all cased letters converted to
  ‾‾‾‾‾‾‾‾‾       lowercase.
"""
print('\n> Convert the string \'Hello\' to all lower case by using [str.LOWER()]:')
print('Hello'.lower())
"""
> str.LSTRIP([chars]) - Returns a copy of the string with a set of characters removed.
  ‾‾‾‾‾‾‾‾‾‾      the 'chars' argument is a string specifying the set of characters to
                  be removed. If omitted or None, the 'chars' argument defaults to
                  removing whitespaces. Different from [str.REMOVEPREFIX] and
                  [str.REMOVESUFFIX] described below.
"""
print('\n> Strip the characters \'Hell\' from the left in the'
      'str. \'Hello, man\' by using [str.LSTRIP(\'Hell\')]:')
print('Hello, man'.lstrip('Hell'))
"""
> str.MAKETRANS(x, [y, [z]]) - Static method that returns a translation table usable
  ‾‾‾‾‾‾‾‾‾‾‾‾‾   for the [str.TRANSLATE()] method described below. If there are two
                  arguments, they must be strings of equal length, and in the resulting
                  dictionary, each character in 'x' will be mapped to the character at
                  the same position in 'y'. If there is a third argument, if must be a
                  string, whose characters will be mapped to 'None' in the result.
                  LOOK UP TRANSLATION WITH MAKETRANS() AND TRANSLATE()
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.PARTITION(sep) - Splits the string a the fist occurrence of 'sep', and returns a
  ‾‾‾‾‾‾‾‾‾‾‾‾‾   3-tuple containing the part before the separator, the separator
                  itself, and the part after the separator. Of the separator is not
                  found, returns a 3-tuple containing the string itself, followed by
                  two empty strings. (Opposite to [str.RPARTITION()]).
"""
print('\n> Split the string \'Hello\' into a 3-value tuple at the first occurrence of'
      '\n\'l\' by using [str.PARTITION(\'l\')]:')
print('Hello'.partition('l'))
"""
> str.REMOVEPREFIX(prefix) - If the string starts with the 'prefix' string, returns
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾the string with the prefix stripped [str[len(prefix):]. Otherwise,
                  returns a copy of the original string.
"""
print('\n> Remove the prefix \'Text\' from the str. \'TextBook\' '
      'by using [str.REMOVEPREFIX(\'Text\')]:')
print('TextBook'.removeprefix('Text'))
print('Now remove the prefix \'Text\' from the str. \'BaseTextBook\' '
      'by using [str.REMOVEPREFIX(\'Text\')]')
print('BaseTextBook'.removeprefix('Text'))
"""                                
> str.REMOVESUFFIX(suffix) - If the string ends with the 'suffix' string, returns the
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾string with the suffix stripped [str[:-len(suffix)]. Otherwise,
                  returns a copy of the original string.
"""
print('\n> Remove the suffix \'Book\' from the str. \'TextBook\' '
      'by using [str.REMOVESUFFIX(\'Book\')]:')
print('TextBook'.removesuffix('Book'))
print('Now remove the suffix \'Text\' from the str. \'TextBook\' '
      'by using [str.REMOVESUFFIX(\'Text\')]')
print('TextBook'.removesuffix('Text'))
"""                       
> str.REPLACE(old, new, [count]) - Returns a copy of the string with all occurrences
  ‾‾‾‾‾‾‾‾‾‾‾     of the substring 'old' replaced by the substring 'new'. If the
                  optional argument 'count' is given, only the first 'count'
                  occurrences are replaced.
"""
print('\n> Replace the word \'boy\' by the word \'man\' in the '
      'str. \'Hello, boy\' by using [str.REPLACE(\'boy\', \'man\')]:')
print('Hello, boy'.replace('boy', 'man'))
"""                                   
> str.RFIND(sub, [start, [end]]) - Returns the highest index or latest occurrence in
  ‾‾‾‾‾‾‾‾‾       the string where 'sub' is found, such as 'sub' is contained within
                  [s[start:end]]. Optional arguments 'start' and 'end' are interpreted
                  as in slice notation. Returns '-1' on failure.
"""
print('\n> Find the highest index (latest occurrence) where the '
      'substring \'m\' is located \nin the string \'Hello, my name is Alfa\' by '
      'using [str.RFIND(\'m\')]:')
print('Hello, my name is Alfa'.rfind('m'))
"""                                   
> str.RINDEX(sub, [start, [end]]) - Like [str.RFIND()] but raises a ValueError when
  ‾‾‾‾‾‾‾‾‾‾      the substring 'sub' is not found.
"""
print('\n> Find the highest index (latest occurrence) where the '
      'substring \'a\' is located \nin the string \'Hello, my name is Alfa\' by '
      'using [str.RINDEX(\'m\')]:')
print('Hello, my name is Alfa'.rindex('a'))
"""                                    
> str.RJUST(width, [fillchar]) - Returns the string right-justified in a string of
  ‾‾‾‾‾‾‾‾‾       length 'width'. The original string is returned if 'width' is less
                  than or equal to the length of the string [len(str)]. Padding is done
                  using the specified 'fillchar' argument. (Opposite to [str.LJUST()]).
"""
print('\n> Justify the string \'Hello\' to the right by using [str.RJUST(20)]:')
print('Hello'.rjust(20))
print('Now justify the string \'Hello\' to the right by using [str.RJUST(20, \'-\')]:')
print('Hello'.rjust(20, '-'))
"""                                 
> str.RPARTITION(sep) - Splits the string at the last occurrence of 'sep', and returns
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾  a 3-tuple containing the part before the separator, the separator
                  itself, and the part after the separator. If the separator is not
                  found, returns a 3-tuple containing 2 empty strings, followed by the
                  string itself. (Opposite to [str.PARTITION()]).
"""
print('\n> Split the string \'Hello\' into a 3-value tuple at the latest occurrence of'
      '\n\'l\' by using [str.PARTITION(\'l\')]:')
print('Hello'.rpartition('l'))
"""                        
> str.RSPLIT(sep, maxsplit=- 1) - Returns a list of the words in the string, using
  ‾‾‾‾‾‾‾‾‾‾      'sep' as the delimiter string. If 'maxsplit' is given, at most
                  'maxsplits' splits are done, to the right (the rightmost ones). If
                  'sep' is not specified or 'None', any  whitespace will be a
                  separator. (Opposite to [str.SPLIT()]).
"""
print('\n> Split the sting \'Hello, my name is Alfa\' at the latest occurrence'
      '\nof \'m\' and only one time, by using [str.RSPLIT(\'m\', 1)]:')
print('Hello, my name is Alfa'.rsplit('m', 1))
"""                                    
> str.RSTRIP([chars]) - Returns a copy of the string with trailing characters removed.
  ‾‾‾‾‾‾‾‾‾‾      The 'chars' argument is a string specifying the set of characters to
                  be removed. If omitted or 'None', the 'chars' argument defaults to
                  removing whitespace. The 'chars' argument is not a suffix, so all
                  combinations of its values are stripped. (Opposite to [str.STRIP()]).
"""
print('\n> Strip the sting \'+  spacious  \' at the latest occurrence '
      'of \' \' (whitespace) by using [str.RSPLIT()]:')
print('+  spacious  '.rstrip() + '> Note that there is no extra space at the end now.')
print('\nNow strip the sting \'mississippi\' at the latest occurrence'
      'of \'ipz\' by using [str.RSPLIT(\'ipz\')]:')
print('mississippi'.rstrip('ipz'), '>\'z\' is not in the string, but there is \'ip\', '
                                   'and from that occurrence the string is stripped.')
print('\nNow strip the sting \'Monty Python\' at the latest occurrence '
      'of \' Python\' by using [str.RSPLIT(\' Python\')]:')
print('Monty Python'.rstrip(' Python'), '> Removes all combinations of the substring '
                                        '\' Python\'. In this case, starting with '
                                        '\'on\' at \'Monty\'')
print('\nBut if we remove the suffix \' Python\' from the string \'Monty Python\' by '
      'using\n[str.REMOVESUFFIX(\' Python\')], the result is different, as it won\'t '
      'remove all\ncombinations, just the last one:')
print('Monty Python'.removesuffix(' Python'), '> Only \' Python\' gets removed from '
                                              'the string')
"""
> str.SPLIT(sep, maxsplit=- 1) - Returns a list of the words in a string, using
  ‾‾‾‾‾‾‾‾‾       'sep' as the delimiter string.  If 'maxsplit' is given, at most
                  'maxsplits' splits are done (thus, the list wil have at most
                  [maxsplit+1] elements). If 'maxsplit' is not specified or '-1', then
                  there is no limit on the  number of splits (all possible splits are
                  made). (Opposite to [str.RSPLIT()]).
"""
print('\n> Split the sting \'Hello, my name is Alfa\' at the first occurrence'
      '\nof \'m\' and only one time, by using [str.SPLIT(\'m\', 1)]:')
print('Hello, my name is Alfa'.split('m', 1))
"""                  
> str.SPLITLINES(keepends=False) - LOOK UP FOR INDIVIDUAL SPLIT METHOD BOUNDARIES IN
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾                         UNIVERSAL NEWLINES (PYTHON GLOSSARY)
                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.STARTSWITH(prefix, [start, [end]]) - Returns 'True' if the string starts with
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾  the 'prefix', 'False' otherwise. 'prefix' can also be a tuple of
                  prefixes to look for. With optional 'start' and 'end' arguments to
                  start comparison at a specific index.
"""
print('\n> Check if the string \'Hello\' starts with \'h\' '
      'by using [str.STARTSWITH(\'h\')]:')
print('Hello'.startswith('h'))
print('Now check if the string \'Hello\' starts with \'H\' '
      'by using [str.STARTSWITH(\'H\')]:')
print('Hello'.startswith('H'))
"""                  
> str.STRIP([chars]) - Returns a copy of  the  string with the leading a trailing
  ‾‾‾‾‾‾‾‾‾       characters removed. The 'chars; argument is a string specifying the
                  set of characters to be removed. If omitted or 'None', the 'chars'
                  argument defaults to removing whitespaces. The 'chars' argument is
                  not a prefix or suffix, but all combinations of its values.
                  (Opposite to [str.RSTRIP()]). 
"""
print('\n> Strip the sting \'  spacious  \' at the first and last occurrence '
      'of \' \' (whitespace) by using [str.RSPLIT()]:')
print('  spacious  '.strip() + '> Note that there are no spaces now.')
print('\nNow strip the sting \'www.example.com\' at the first and last occurrence'
      'of \'cmowz.\' by using\n[str.RSPLIT(\'cmowz.\')]:')
print('www.example.com'.strip('cmowz.'), '> \'www.\' gets stripped as it is the first '
      'occurrence of \'w\' and \'.\', then \'.com\' gets stripped\nas its the first '
      'occurrence of \'c\', \'m\' and \'o\', and also the latest occurrence of \'.\'.')
"""                                    
> str.SWAPCASE() - Returns a copy of the string with uppercase letters converted to
  ‾‾‾‾‾‾‾‾‾‾‾‾    lowercase and vice versa.
"""
print('\n> Convert the string \'Hello\' to \'hELLO by using [str.SWAPCASE()]:')
print('Hello'.swapcase())
"""                  
> str.TITLE() - Returns a titlecased version of the string where every word starts with
  ‾‾‾‾‾‾‾‾‾       an uppercase character and the remaining characters are lowercase.
"""
print('\n> Convert the string \'Hello, my name is alfa\' to titlecase by using'
      '[str.TITLE()]:')
print('Hello, my name is alfa'.title())
"""                  
> str.TRANSLATE(table) - (See [str.MAKETRANS(X, Y, Z)]) Returns a copy of the string in
  ‾‾‾‾‾‾‾‾‾‾‾‾‾   which each character has been mapped through the given translation
                  table. The table must be an object that implements indexing via
                  [__getitem__()], typically a mapping or a sequence. When indexed by
                  an integer, the table object can do any of the following: return a
                  Unicode ordinal or a string to map the character to one or more other
                  characters, return 'None' to delete the character from the return
                  string, or raise a LookupError exception to map the character to
                  itself. See [codex] module for a more flexible approach to custom
                  mapping. LOOK UP TRANSLATION WITH MAKETRANS() AND TRANSLATE()
                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> str.UPPER() - Returns a copy of the  string with all cased characters converted to
  ‾‾‾‾‾‾‾‾‾       uppercase. Note that manipulating a string with [str.UPPER()] and
                  then applying the method [str.ISUPPER()] might return 'False' if the
                  original string contains uncased characters.
"""
print('\n> Convert the string \'Hello\' to all upper case by using [str.UPPER()]:')
print('Hello'.upper())
"""                 
> str.ZFILL(width) - Returns a copy of the string left-filled with ASCII '0' digits to
  ‾‾‾‾‾‾‾‾‾       make a string of length 'width'. A leading sign prefix '+'/'-' is
                  handled by inserting the padding AFTER the character rather than
                  before. The original string is returned if 'width' is less than or
                  equal to the length [len(str)] of the string.
"""
print('\n> Fill the string \'Hello\' from the left with \'0\'s '
      'by using [str.ZFILL(10)]:')
print('Hello'.zfill(10), '> The sting \'Hello\' has 5 index positions, so if the method '
                         'was\ngiven the task to fill up to 10 positions, it will add 5 '
                         'more zeros.')
print('\nNow fill the string \'-Hello\' from the left with \'0\'s '
      'by using [str.ZFILL(10)]:')
print('-Hello'.zfill(10), '> The sting \'-Hello\' has 6 index positions, so if the '
                         'method was\ngiven the task to fill up to 10 positions, it '
                         'will add 4 more zeros, but after\nany \'+\' or \'-\' signs.')
"""
                        REGULAR EXPRESSION OPERATIONS (LOOK UP)
                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                 
> str.MATCH() - 
> str.SEARCH() - 
> str.FINDALL() - 
> str.FINDITER() - 
> str.GROUP() - 
> str.START() - 
> str.END() - 
> str.SPAN() - 
> str.SPLIT() - 
> str.SUB() - 
> str.SUBN() - 
"""