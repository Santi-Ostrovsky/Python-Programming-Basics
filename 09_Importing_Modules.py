"""
                                    IMPORTING MODULES
                                    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
From now on, a Module is any Python file (.py) that is not part of the current program.
An external file, either built-in, downloaded using PIP, or manually created by the
coder, any Module is one that adds external functionality to a program, without
physically being inside said program. Both modules and packages can be imported.

Python code in one module gains access to the code in another module by the process
of importing it. The [import] statement is the most common way of invoking the import
machinery, but it is not the only way to do so.

The [import] statement combines two operations: it first searches for the  named
module, and then binds it the results of that search to a name in the local scope.
This means that, when called, Python will look for the module, and bind either all or
some names (variables and functions) to the program they were called from. It will
bind all or just some names, depending on what the import command was (examples below).

Imports always have to be done at the top of the file, after any module comments and
docstrings (description of the file done between inverted commas [""], just like this
text, which is a docstring).

Something that also has to be taken into account when importing, is that whenever we
do import a file/module, we must specify the path of said file, if it is not in the
same directory as the local file they are being imported/called from. Let's say the
file we are in right now, is inside a folder/directory, with another file called
"Useful_Functions", containing functionality that we want to import to our local file.
In this case, we can just type the name of the file, because it is in the same
directory. Otherwise, we would have to specify the entire path of the imported file
before its name, so that Python knows where to look for it.

Just like the [MATH] module (seen in file #2), Python has several built-in modules
that bring a lot of functionality to a program. To use them, these modules have to
be called/imported, which can be done in a couple different ways.

                                SYNTAX OF IMPORT STATEMENTS
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1 > IMPORT [MODULE]
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [IMPORT] statement imports the entire Module into a local file, as a "package of
functions". This means that, as the entire file is imported and not just the
functionality inside the file, the Module has to be called each time a variable or
function from said Module is used, and their names will not be polluting the namespace
in the local file the Module was called from.

As an example with objects from ordinary life, we could use the following metaphor to
further understand what that means: If I wanted to stay in my room and not have to go
out, but I still wanted drinks and food from the fridge, I could either get those
before staying inside, or I could bring the entire fridge with me, so that the stuff
that I want to use/consume, will not be lying around in my room; but every time I
wanted something, I would have to open the fridge to get it. With the [IMPORT]
statement, we are doing the latter, "bringing the fridge to the room and opening it
everytime we want something from it".
"""
# USE THE 'MATH' MODULE AS EXAMPLE:
import math
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('By typing "import math", we bring the entire package of math functions from '
      'said module,\nand have to call it each we want to use them.')
print('Lets say we want to use the "Power" [pow()] function. Once the math module has '
      'been imported, by using\nthis specific syntax, we can only use it by calling '
      'the module before the function, as follows:')
print('> WRONG --> pow(2, 3) --> "No variable \'pow\' found in local file."')
print('> RIGHT --> math.pow(2, 3) -->', math.pow(2, 3))

"""
2 > FROM [MODULE] IMPORT [FUNCTION / VALUE]
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [FROM] statement serves the purpose of importing functionality from an external
Module, without having to import the Module itself, like the [IMPORT] statement does.

In this case, the external Module does not have to be called before the variables
and/or functions we want to use from it, and the names of those variables and/or
functions will be taking slots in the namespace (if we have a variable called
"Numbers" in our local file, and we wanted to import a variable from an external file
with the same name, we would have to change the name of the variable in the local file,
since there cannot be two variables with the same name.

Using the same example from ordinary life we used before, in stead of bringing the
fridge to my room and opening it every time I wanted something from it, I would
directly take everything I need from the fridge with me, but leaving the fridge in the
kitchen. Now, every item I took is occupying a different space in my room, but they
are already there, I do not need to open the fridge to access them.

When using the [FROM] statement, we can group the needed variables and/or functions we
need, as long as they are all from the same Module. If we wanted to import
functionality from two different modules, each Module will require a different line of
code with its respective [FROM] statement.

If we wanted to import the entirety of the Module's contents but not the Module itself,
or all sub-packages inside a main package. We can achieve this by typing:
[from [module] import *] --> an asterix will import all variables and functions.
Have in mind that, this may result in the main program being filled up with numerous
unaffiliated names polluting the namespace, and names overlapping or colliding with
other functions or variables from different files and/or modules, generating unintended
consequences.
"""
# USE THE 'RANDOM' MODULE AS EXAMPLE:
from random import randint, randrange
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('By typing "from random import randint, randrange", we only bring the '
      '[RANDINT()] and [RANDRANGE()]\nfunctions from the \'random\' module.')

print('\nThese two functions are just being used as an example, but their uses are:')
print('--> [RANDINT(x, y)]: Returns a random integer greater than or equal to \'x\', '
      'and lower than or\nequal to \'y\' (x <= number <= y).')
print('--> [RANDRANGE(x, y, z)]: Returns a randomly selected element from range \'x\' '
      'to \'y\' in steps of \'z\'\n(can take only one argument \'y\'). It is similar '
      'to [RANDINT()],but more specific\n(previous example is equal to '
      'randrange(x, y+1).')

print('\nFunctions would be used as follows:')
print('> WRONG --> random.randint(1, 100) --> "No object \'random\' found in '
      'local file."')
print('> RIGHT --> randint(1, 100) -->', randint(1, 100))
print('\n> WRONG --> random.randrange(100) --> "No object \'random\' found in '
      'local file."')
print('> RIGHT --> randrange(100) -->', randrange(100))

"""
3 > IMPORT [MODULE] AS [...]
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The [IMPORT] statement accepts this variation, the [AS] statement, which allows to
import an entire Module with an alias. The effect of the import is the exact same as
the one in the first case, using the [IMPORT] statement.

This is useful when several Modules are imported into a file, and the coder needs an
easier way to identify or categorize each one.

For example, let's say we want to import the following modules into our local file:
- configparser
- contextvars
- dataclasses
- faulthandler
- lib2to3
- multiprocessing
- pickletools
- turtledemo

All above are Python built-in modules with particularly long or hard-to-spell names
when in a rush. So, an easy way to import and categorize these modules would be to
apply an alias to each one, when importing them, as follows:
- [ import configparser as co1 ]
- [ import contextvars as co2 ]
- [ import dataclasses as dat ]
- [ import faulthandler as fau ]
- [ import lib2to3 as lib ]
- [ import multiprocessing as mul ]
- [ import pickletools as pic ]
- [ import turtledemo as tur ]

All modules were imported, and all their functionalities can be used in the local file,
but their original Module names do not have to be called when using said
functionalities, their aliases have to be called instead.

For example, to use a function from the 'dataclasses' module, we would have to type the
following: [dat.astuple()] in stead of [dataclasses.astuple()]. Easier to remember,
quicker to enter in the code.


                            ABSOLUTE AND RELATIVE IMPORTS
                            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
ABSOLUTE IMPORTS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Absolute import involves typing the full path, from the project’s root folder to the
desired module. An absolute import states the resource to be imported using its full
path from the project’s root folder.

│
└────────── project_a
               │
               ├────────── p_1
               │            │
               │            ├────────── module_a
               │            │
               │            └────────── module_b
               │
               └────────── p_2
                            │
                            ├────────── module_c
                            │
                            └────────── sp_3
                                          │
                                          └────────── sm_d

Here we have a Directory named 'project_a', under which there are two sub-directories
'p_1' and 'p_2'.

- Package 'p_1' has Modules 'a' and 'b'. 'module_a' contains the function [fun1()].
- Package 'p_2' has Module 'c', which contains the function [fun2()]; and
  Sub-Package 'sp_3', which contains Sub-Module 'sm_d'.

--> To import [fun1()] from 'module_a' and [fun2()] from 'module_c':

    >>> from p_1 import module_a import fun1
    >>> from p_2 import module_c import fun2
    
--> To import [fun3()] from 'sm_d':

    >>> from p_2.sp_3.sm_d import fun3
    
    * The entire path is written from the root folder, separating directories and
      sub-directories (folders and sub-folders or packages and sub-packages) with a
      dot/decimal point, before importing the function.

Pros and Cons of Absolute imports:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Pros:
- Absolute import is clear and its easy to tell exactly from where the imported
  resource is, just by looking at the statement.
- Absolute imports remain valid even if the current location of the import statement
  changes.

Con:
- If the directory structure is very long, the usage of absolute imports is not
  meaningful. In such case, using relative imports works well. An example of a
  big directory structure can be: [from p_1.sp_2.sp_3.sp_4.module_f import fun6].
 
  
RELATIVE IMPORTS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Relative imports specify the Object or Module imported from its current location.

The syntax of relative import depends on current location as well as a location of
Module or Object to be imported. Relative imports use dot(.) notation to specify a
location:
- Single dot [.] specifies that the Module is in the current Directory.
- Two dots [..] indicate that the Module is in the parent Directory of the current
  location.
- Three dots [...] indicate that the Module is in the grandparent Directory.
- AND SO ON...

│
└────────── project_a
               │
               ├────────── p_1
               │            │
               │            ├────────── module_a
               │            │
               │            └────────── module_b
               │
               └────────── p_2
                            │
                            ├────────── module_c
                            │
                            └────────── sp_3
                                          │
                                          └────────── sm_d
                
Lets use the same Directory named 'project_a', under which there are two
sub-directories 'p_1' and 'p_2'.

- Package 'p_1' has Modules 'a' and 'b'. 'module_a' contains the function [fun1()].
- Package 'p_2' has Module 'c', which contains the function [fun2()]; and
  Sub-Package 'sp_3', which contains Sub-Module 'sm_d'.

--> If we were working in 'module_b', to import [fun1()] from 'module_a', use:

    >>> from .module_a import fun1
    
    * We use a dot [.] to go to the current Directory (p_1), then enter the Module we
      want to import, and finally use the 'import' statement to access the individual
      function.
      
--> If we were working in 'sm_d', to import [fun2()] from 'module_c', use:

    >>> from ..module_c import fun2
    
    * One dot [.] to go to current Directory 'sp_3', and one more [.] to go to the
      father  Directory 'p_2', then specify which file we are looking for (module_c),
      and finally import the function [fun3()].
    
--> But, if we were working in 'module_b', and wanted to import [fun2()]
    from 'module_c', we would not be able to do so, since we would have to go over
    'p_1', reaching the root folder 'package_a', which cannot be done with relative
    import.
    
    In that case, an Absolute Import would be needed. Otherwise, the program will
    crash and Python will raise the ValueError 'Attempted relative import beyond
    top-level package':

    >>> from ..p_2.module_c import fun1 --> [ValueError: Attempted relative import
                                            beyond top-level package].

Pros and Cons of Relative imports :
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Pros:
- Working with relative imports is concise.
- Based on current location it reduces the complexity of an import statement.

Cons:
- Relative imports are not so readable as Absolute imports.
- Using Relative imports is not easy since it is very hard to tell the exact
  location of a Module.


                                  PYTHON BUILT-IN MODULES
                                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Python has a long list of built-in modules that can be called in any of the ways
explained at the beginning. Among the most commonly used are:
- math
- random
- re
- collections
- time
- http
- copy

For a full list, LOOK UP PYTHON MODULE INDEX: https://docs.python.org/3/py-modindex.html
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
