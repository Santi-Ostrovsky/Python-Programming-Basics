"""
                                READING & WRITING DATA
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Storing data and the results of a program's functionality is important for working
over multiple sessions and sharing those results for other programs to interact with.
Since when Python closes, all variables in the memory are lost, data must be stored in
some other way, and it must also be readable and/or writable by other programs or the
same program that originated the data, in a different execution.

Python files can interact with external files, such as text documents [.txt] and other
databases, for programs to save and get data from them.


                                     TXT FILES
                                     ‾‾‾‾‾‾‾‾‾
Text files with extension .txt are files containing plain text, that can be used to
store data in a disk to share with other programs or to be used by the same program
in a different execution. These text files, however, must be in a certain format,
organized in a specific way in order to be used by the program.

To work with text files, the first thing to do is to OPEN them, by using the [open()]
statement, which will take 2 string arguments:

- An absolute or relative path to the file, or just the file name if said file is in
  the same directory as the Python file opening it;

- The mode we want to open the file in, which can be any of the following (lowercase):

    --> 'r' - Default mode, which opens the file for READING only.

    --> 'w' - Opens the file for WRITING, modifying it. If the file does not exist,
               this command creates it.

    --> 'a' - Opens the file in APPEND mode, adding data without overwriting the
              existing one. If the file foes not exist, this command creates it.

    --> 'b' - Opens the file in BINARY mode. 'rb' or 'wb' would mean "read binary" and
               "write binary", respectively, and its used when the opened file has
               non-ascii characters. Opening the file in binary mode will never alter
               or hard the data inside, however opening it in ascii mode by default may
               delete or change some characters inside, modifying the data you are
               trying to access. The data inside is read and written in the form of
               bytes objects (important: only use for files that do not contain text).

    --> 'r+' - Opens the file for READING AND WRITING. Does not create a new file. This
               command allows you to modify existing data in the file without discarding
               all of its contents.

    --> 'w+' - Opens the file for WRITING AND READING, discarding existing contents
               (overwriting). If the file does not exist, this command creates it.

    --> 'a+' - Opens the file for READING AND WRITING, APPENDING the new data at the
               end of the file, without discarding or overwriting data.

The [OPEN(x, y)] can also be stored as a variable, meaning that calling said variable
(or even a function) would open the file without having to type the entire command each
time.

IMPORTANT --> ALWAYS CLOSE EXTERNAL FILES AFTER USING THEM, BY USING THE [.CLOSE()]
‾‾‾‾‾‾‾‾‾     FUNCTION.

So, an example of how to open a file, inside a variable or function, in order to read
it, would be as follows (file called 'employee_list' containing employees' names):

>>> read_EmployeeList = open('employee_list', 'r')
>>> close_EmployeeList = read_EmployeeList.close


READING FILES
‾‾‾‾‾‾‾‾‾‾‾‾‾
Before reading a from a file, it is good practice conditioning the action of reading
to the result of checking if the file is readable, for which we must use the
'[file].readable()' function. It returns the boolean value [True] if the file is
readable, [False] otherwise.

There are other built-in methods to get information from a file, such as:
- [file].tell(x) --> Returns an integer giving the file object 'x's current position in
                        the file, represented as a number of bytes from the beginning of
                        the file when in binary mode, or an opaque number in text mode.

- [file].seek(x, y) --> Used to change the object's position (cursor), 'x' representing
                        the 'offset', the position in the file, and the optional
                        argument 'y', representing the 'whence', where a value of '0'
                        would count from the beginning of the file, a value or '1'
                        would count from the current file cursor position, and a value
                        of '2' would count from the end of the file. When omitted, 'y'
                        defaults to '0', counting from the beginning of the file.

Once we know the file is readable, we can use any of the following built-in functions
to get data from the file:

- [file].READ() --> Used to access ALL DATA in the file. If used following a 'print'
                         statement, the entire text file would be printed out. An
                         optional 'size' argument can be given in between parentheses,
                         indicating the amount of lines accessed in the file, so that
                         it is not completely imported to the local module if the file
                         is too large for the memory to handle properly.

                         >>> f = open('employee_list.txt', 'r')
                         >>> content = f.read()
                         >>> f.close()
                         >>> print(content)
                         --> [The entire file is printed out]

- [file].READLINE() --> Used to access ONE INDIVIDUAL LINE of data in the text file
                         at a time, moving the 'cursor' to the next line, meaning that
                         if another 'readline()' command is given, the following line
                         will be accessed (the same would happen if the 'read()' command
                         was used after the first 'readline()', the entire file would be
                         accessed separated from the first line).

                         >>> f = open('employee_list.txt', 'r')
                         >>> content = f.readline()
                         >>> f.close()
                         >>> print(content)
                         --> [Fist line in the file is printed out]

- [file].READLINES() --> Used to access ALL LINES in the file as elements inside a
                         list. Since each line represents an element in the list, they
                         have an index position associated to them, meaning that we
                         could use the 'readlines()' command to access all lines in the
                         file, but still get information or print out only one by
                         indexing it as follows: 'readlines()[index]'

                         >>> f = open('employee_list.txt', 'r')
                         >>> content = f.readlines()[3]
                         >>> f.close()
                         >>> print(content)
                         --> [third line in the file is printed out]

                         The 'readlines()' method can also be used with a FOR LOOP to
                         print out or access not only all lines in the file, but every
                         character in a given line. For example:

                         >>> f = open('employee_list.txt', 'r')
                         >>> for i in f.readlines()[2]:
                         >>>    print(i)
                         >>> f.close()
                         --> [All characters in the second line of the file printed out
                             in individual lines]

WRITING AND APPENDING FILES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
For writing in a text file, we only have one command: '[file].write()', which will
affect the file according to what mode we opened the file in ('w', 'r+', 'a+', etc.).

>>> f = open('employee_list.txt', 'a')
>>> f.write('John M. Newman - HR\n')
>>> f.close()

In the example above, the file was opened in 'append' mode, which adds data to the end
the file. Then the '[file].write()' method was used to add the new line
"John M. Newman - HR" to the file, plus '\n' to create a new line. Finally, the file
was closed to save progress and avoid loss of data.

'[file].write()' can also be paired with FOR LOOPS and other built-in structures and
functions, for example:

>>> nf = open('new_file.txt', 'w')
>>> for i in range(5):
>>>     nf.write(f"This is line {i+1}.\n")
>>> nf.close()

'new_file' gets created with the following lines:
- This is line 1.
- This is line 2.
- This is line 3.
- This is line 4.
- This is line 5.

WITH STATEMENT
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Knowing how important it is to close text files after using them, it is good practice to
make use of a feature called 'WITH' keyword, when dealing with file objects. When
accessing files with the 'WITH' statement, files are automatically and properly closed
after its suite finishes, even if exceptions are raised. Example:

>>> with open('new_file.txt') as f:
>>>     print(f.read())
>>> print('File operations end here')
>>> print(f.closed)

First, we have the 'WITH' statement, 'OPEN' keyword with the name of the file, and an
alias, equivalent to opening the file inside a variable. Indented inside the 'WITH'
block (much like a function) the command to print the entire file is given, but not the
order to close it.

Finally, a line will be printed stating that no more file operations are performed
after that point, and a final line printing the '[file].closed' method, which returns
a boolean value depending on whether the called filed was closed or not.

After executing this block, console returns the following:

--> This is line 1.
--> This is line 2.
--> This is line 3.
--> This is line 4.
--> This is line 5.

--> File operations end here.
--> True


                                     CSV FILES
                                     ‾‾‾‾‾‾‾‾‾
CSV (Comma-separated Values) files store lots of scientific data, as delimited text
files that use commas [,] to separate values. It is a very useful format that can store
large tables of data in plain text. Each line (row) in the data is one data record, and
each record consists of one or more fields, separated by commas. These files can also be
opened using Microsoft Excel, to visualize the file as a set of rows and columns.

Python has its own CSV Module that can handle the reading and writing of CSV files with
built-in methods (Pandas Module can also be used to handle CSV files).
LOOK UP THE CSV MODULE HERE: https://docs.python.org/3/library/csv.html
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

We can also the Numpy package to read the CSV files directly into a numpy array.  HERE:
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.02-CSV-Files.html ‾‾‾‾


                                    PICKLE FILES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾
Saving data in .txt or CSV files allows you to only save text data, but if we wanted to
save data that will be directly used in a Python file as Lists, Tuples or Dictionaries,
we must use the PICKLE Module to access Pickle files (.pkl) which are able to store said
kind of data (.pkl are Python dependent files).

IMPORTANT --> Pickle files are binary files, so data stored and retrieved must be
serialized and de-serialized respectively, and files must be handled in binary mode.

First, the Pickle Module must be imported, as any other module would be:
>>> import pickle

More about the Pickle module, Data stream format and proprietary methods here:
https://docs.python.org/3/library/pickle.html#module-pickle

WRITE A PICKLE FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
To use Pickle to serialize an object, we must use the 'pickle.dump' function, which
takes 2 arguments:
- The object we want to dump inside the file;
- The file object returned by the '[file].open' function (Note that the example file is
  handled in binary mode - 'wb').

>>> import pickle as pkl
>>> dictionary_a = {'A':0, 'B':1, 'C':2}
>>> pkl.dump(dictionary_1, open('test.pkl', 'wb'))

READ A PICKLE FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
To load the dictionary object we saved in the file 'test.pkl' in previous example, we
must use the 'pickle.load' function (Note that the example file was loaded in binary
mode - 'rb'):

>>> new_dictionary = pkl.load(open('test.pkl', 'rb'))
>>> print(new_dictionary)

--> {'A':0, 'B':1, 'C':2}

MORE ABOUT HANDLING DATA WITH PICKLE MODULE HERE: https://youtu.be/eWrTSBIQess
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾


                                     JSON FILES
                                     ‾‾‾‾‾‾‾‾‾‾
JSON (JavaScript Object Notation) files (.json) are not Python dependent files like .pkl
files are, they are language-independent data. They usually take less space on disk and
its manipulation is much faster than pickle files.

JSON FORMAT
‾‾‾‾‾‾‾‾‾‾‾
Text is JSON is written through quoted string values in key-value pairs withing curly
brackets [{}], very similar to a Python Dictionary:

>>> {
>>>     "school": "UC Berkeley",
>>>     "address": {
>>>         "city": "Berkeley",
>>>         "state": "California",
>>>         "postal": "94720"
>>>   },
>>>
>>>     "list":[
>>>         "student 1",
>>>         "student 2",
>>>         "student 3"
>>>       ]
>>> }

As can be seen by the brackets' indentation, everything in the block above is inside
'"school": "UC Berkeley"', as other data values like 'address' and 'student list'.

WRITING A JSON FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The easiest way to handle JSON files in Python is to use the json Module, but there are
more libraries like simplejson and jyson that can also handle them. The difference is,
the json Module natively supports JSON files by Python.

>>> import json
>>>
>>> school  = {
>>>     "school": "UC Berkeley",
>>>     "address": {
>>>         "city": "Berkeley",
>>>         "state": "California",
>>>         "postal": "94720"
>>>     },
>>>     "list":[
>>>         "student 1",
>>>         "student 2",
>>>         "student 3"
>>>     ],
>>>
>>>     "array": [1, 2, 3]
>>> }
>>>
>>> json.dump(school, open(school.json', 'w'))

To serialize an object, we use the json.dump function, like in the pickle module, which
takes 2 arguments:
- The object we want to handle;
- The file object returned by the open function and the opening mode (in this case, w).

READING A JSON FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Now lets load the JSON file we just created in the previous example, by using the
'json.load' function (with previously imported json module):

>>> my_school = json.load(open('school.json', 'r'))
>>> print(my_school)

--> Python interpreter will load all the data into a string, as follows:
{'school': 'UC Berkeley', 'address': {'city': 'Berkeley', 'state': 'California',
'postal': '94720'}, 'list': ['student 1', 'student 2', 'student 3'], 'array': [1, 2, 3]}

MORE ON THE JSON MODULE HERE: https://docs.python.org/3/library/json.html#module-json ,
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
AND: https://docs.python.org/3.10/tutorial/inputoutput.html#reading-and-writing-files
‾‾‾

                                     HDF5 FILES
                                     ‾‾‾‾‾‾‾‾‾‾
HDF5 (Hierarchical Data Format) files can store large amounts of data for scientific
computing, providing the solution when previous file types just don't cut it. HDF5 is
a powerful binary data format with no limit on the file size: it provides parallel 'IO'
(input/output), and carries out a lot of low level optimizations to make queries faster
and storage requirements smaller.

MORE ON HDF5 FILES HERE:
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.05-HDF5-Files.html


                        COMPRESSION USING THE 'LZMA' ALGORITHM
                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
https://docs.python.org/3.10/library/lzma.html#reading-and-writing-compressed-files


                            READING & WRITING UNICODE DATA
                            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
https://docs.python.org/3.10/howto/unicode.html#reading-and-writing-unicode-data


"""

