"""
                                  OTHER DATA TYPES
                                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
> LISTS
> TUPLES
> SETS
> DICTIONARIES
> CLASSES / OBJECTS

                          OBJECT ORIENTED PROGRAMMING (OOP)
                          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Until now, all files treated what is called Procedure-oriented programming (POP), which
simply consists on a list of instructions to tell the computer what to do, and these
instructions are then organized into functions.

The relatively modern programming paradigm of Object-oriented Programming (OOP from now
on), is commonly used when writing large programs or packages. It simplifies the code
for better readability, better describes the end goal of the project, is reusable, and
reduces the number of potential bugs in the code, among other pluses.

Given these features, OOP can be found in most standard packages in the field. Python
is a highly object-oriented programming language, so understanding OOP is crucial for
an efficient programming.

OOP breaks programming tasks into Objects, which combine data (attributes) and
behaviours or functions (methods). Objects, can only exist under Classes. Therefore,
OOP has 2 main components: Classes and Objects.

                                CLASSES AND OBJECTS
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
CLASSES are blueprints used to define a logical grouping of data and functions.
Basically, they define a new Data type, and each piece of complete data will be
called an OBJECT. Objects are instances of the defined class with actual values.

Similar to a function, classes are defined as a block of code, starting with the
[CLASS] statement. The syntax of a Class definition is explained below.

As an example, the "Rectangle" class is created, defining a new Data Type for
rectangles (all class names must be in CamelCase / first capital letter). Inside
every class, there has to be an __init__ method, to establish all values/parameters
each object inside the class will have.

__init__(self...) --> self, is used to name each object. When the term 'self' is used
inside a class method, means that it will work with all objects in the class. If we
were to put a name instead of 'self', for example "rectangle1", all objects in the
class will be called "rectangle1", even if we create them under some other name, so
the class would stop being useful.

After __init__(self...), inside the parentheses, we must add all main parameters of
our objects. In this case, rectangles will have a Color, Length, and Width. We can
define the name of these parameters, inside the parenthesis, to whatever we like. For
example, 'Color' can be 'c', or it could be 'ghjk123', but that wouldn't be practical.

So, if we were to define all parameters as a single letter, the method would be
completed as follows: __init__(self, c, l, w).

After the __init__ define line, we must list below, how to define and determine each
parameter when individual objects in the Class are created, as follows:

>>> class Rectangle:
>>>     def __init__(self, c, l, w):
>>>         self.color = c
>>>         self.length = l
>>>         self.width = w

In this case, the Class 'Rectangle' will have objects with 3 main parameters besides
'self'(name): c, l and w ('c', 'l' and 'w' being the names of the parameters in the
method; and 'color', 'length'  and  'width' being the description of said parameters
when individual objects are created or their values are called/returned/printed).
When creating an object, each parameter will have to be defined.

To create an object in the 'Rectangle' Class, we must define them like we were defining
a variable, and calling the Class name in the variable's value, as follows:

>>> rectangle_1 = Rectangle(red, 2, 4)

In this case, we are creating a variable called 'rectangle_1', that becomes an object
when the class 'Rectangle' is called in the variable's description. In parentheses, the
object's attributes are entered, separated by a comma [,]. Parameters 'red', '2' and '4'
correspond to values 'c' (color), 'l' (length) and 'w' (width) in the example above.

To call objects' attributes, we must type [object's name].[attribute]. For example, if
we  were to  print the attribute 'l' from the object 'rectangle_1', we should enter:
'print(rectangle_1.l)' and the console will return '2' in the execution, as 'l' (length)
was defined as '2' when the object 'rectangle_1' was created.

We can also create secondary methods inside a Class, to either modify, re-organize,
select, categorize or provide information about individual objects inside said Class,
and their attributes. As follows:

>>> class Rectangle:
>>>     def __init__(self, c, l, w):
>>>         self.color = c                          │
>>>         self.length = l                         │
>>>         self.width = w                          │  --> (Everything inside the Class
>>>                                                 │       must be indented as it would
>>>     def area(self):                             │       be inside a function).
>>>         self.area = self.length * self.width    │
>>>         return self.area                        │
>>>
>>> rectangle_1 = Rectangle(red, 2, 4)
>>> print(rectangle_1.area)
        ↓
        ↓
        ↓
[Console returns:] 8 --> (length * width = 2*4 = 8)
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Create class \'Rectangle\', with 3 parameters: color, length and width; '
      'and 2 methods to calculate\nboth area and perimeter of the individual '
      'rectangle objects.\n')

print('>>> class Rectangle:')
print('>>>     def __init__(self, c, l, w):')
print('>>>         self.color = c')
print('>>>         self.length = l')
print('>>>         self.width = w')
print('')
print('>>>     def area(self):')
print('>>>         self.area = self.length * self.width')
print('>>>         return self.area')
print('')
print('>>>     def perimeter(self):')
print('>>>         self.perimeter  = (self.length * 2) + (self.width * 2)')
print('>>>         return self.perimeter')

class Rectangle:
    def __init__(self, c, l, w):
        self.color = c
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length * self.width
        return self.area

    def perimeter(self):
        self.perimeter  = (self.length * 2) + (self.width * 2)
        return self.perimeter

print('\nNow, create 5 different Rectangle class objects and define their '
      'attributes.\n')

print('>>> rec1 = Rectangle(\'red\', 2, 4)')
print('>>> rec2 = Rectangle(\'blue\', 6, 4)')
print('>>> rec3 = Rectangle(\'green\', 5, 3)')
print('>>> rec4 = Rectangle(\'yellow\', 3, 8)')
print('>>> rec5 = Rectangle(\'purple\', 4, 9)')

rec1 = Rectangle('red', 2, 4)
rec2 = Rectangle('blue', 6, 4)
rec3 = Rectangle('green', 5, 3)
rec4 = Rectangle('yellow', 3, 8)
rec5 = Rectangle('purple', 4, 9)

print('\nFinally, print out info about objects and test inner methods \'area\' & '
      '\'perimeter\':\n')

print('>>> print(\'Rectangle 2\'s color is:\', rec2.color)')
print('>>> print(\'Rectangle 3\'s length is:\', rec3.length)')
print('>>> print(\'Rectangle 4\'s width is:\', rec4.width)')
print('>>> print(\'Rectangle 1\'s area (2*4) is:\', rec1.area())')
print('>>> print(\'Rectangle 5\'s perimeter (4*2 + 9*2) is:\', rec5.perimeter())')

print('\nRectangle 2\'s color is:', rec2.color)
print('\nRectangle 3\'s length is:', rec3.length)
print('\nRectangle 4\'s width is:', rec4.width)
print('\nRectangle 1\'s area (2*4) is:', rec1.area())
print('\nRectangle 5\'s perimeter (4*2 + 9*2) is:', rec5.perimeter())

"""
                     INHERITANCE, ENCAPSULATION & POLYMORPHISM
                     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
OOP, as shown before, is very powerful, as it allows to create an indeterminate amount
of Data types inside a program, combining classes, objects, and data methods. However,
there are 3 more important concepts that make OOP even more efficient: Inheritance,
Encapsulation and Polymorphism (LOOK UP THE LAST TWO).
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                    INHERITANCE
                                    ‾‾‾‾‾‾‾‾‾‾‾
Inheritance is the concept that allows us to define a Class that inherits all methods
and attributes from another Class. Conventionally, the new Class will be called
"Child Class" and the one it inherits from is called "Parent Class" or "Superclass".
The syntax structure for basic inheritance is:

>>> class [Child Class]([Parent Class]):
>>>                  │ 
>>>                  │  --> [class methods]
>>>                  │

Following this structure, Inheritance builds a relation between the Child Class and the
Parent Class, in a way that the latter is a general type while the former is a specific
type, where the Child Class can access all attributes and methods from the Parent Class.

There are 3 different types of Inheritance:
1 --> Inheritance + new method extension
2 --> Inheritance + method overriding
3 --> Inheritance + attributes update

Below, an example applying all types of Inheritance can be found:
- The Class 'Students' is created, and its attributes and method defined;
- The Class 'ArabStudents' is created, with 'Students' as its Parent Class, defining
  a new method to categorize objects defined withing the inherited parameters
  (Case 1: Inheritance + new method extension);
- The Class 'HonorStudents' is created, with 'Students' as its Parent Class, redefining
  the 'failed_class()' method originally defined in the latter
  (Case 2: Inheritance + method overriding);
- The Class 'NewStudents' is created, with 'Students' as its Parent Class, updating the
  objects' attributes by adding a new one to the original pool. It is possible to
  redefine the entire __init__ method, but in this case just one extra attribute is
  being added. (Case 3: Inheritance + attributes update);

"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print(' ---- INHERITANCE ----\n')
print('1: Create Class \'Students\', with 2 parameters: Name and Grade;\n'
      '2: Create Child Class \'ArabStudents\', which extends a new method;\n'
      '3: Create Child Class \'HonorStudents\', which overrides a parent method;\n'
      '4: Create Child Class \'NewStudents\', which updates the parent attributes,\n'
      '   and displays it in a separate method.\n')

print('>>> class Students:')
print('>>>     def __init__(self, n, g):')
print('>>>         self.name = n')
print('>>>         self.grade = g')
print('')
print('>>>     def failed_class(self):')
print('>>>         if self.grade < 6:')
print('>>>             return True')
print('>>>         else:')
print('>>>             return False')
print('')
print('>>> # Case 1: Inheritance + new method extension.')
print('>>> class ArabStudents(Students):')
print('>>>     def is_arab(self):')
print('>>>         if self.name endswith(\'mad\'):')
print('>>>             return True')
print('>>>         else:')
print('>>>             return False')
print('')
print('>>> # Case 2: Inheritance + method overriding.')
print('>>> class HonorStudents(Students):')
print('>>>     def failed_class(self):')
print('>>>         if self.grade < 7:')
print('>>>             return True')
print('>>>         else:')
print('>>>             return False')
print('')
print('>>> # Case 3: Inheritance + attributes update.')
print('>>> class NewStudents(Students):')
print('>>>     def __init__(self, n, g, td):')
print('>>>         super().__init__(n, g) # Call to the Superclass __init__ func.')
print('>>>         self.name = n')
print('>>>         self.grade = g')
print('>>>         self.transfer_date = td')
print('')
print('>>>     def print_date(self):')
print('>>>         print(self.transfer_date)')

class Students:
    def __init__(self, n, g):
        self.name = n
        self.grade = g

    def failed_class(self):
        if self.grade < 6:
            return True
        else:
            return False

class ArabStudents(Students):
    def is_arab(self):
        if self.name.endswith('mad'):
            return True
        else:
            return False

class HonorStudents(Students):
    def failed_class(self):
        if self.grade < 7:
            return True
        else:
            return False

class NewStudents(Students):
    def __init__(self, n, g, td):
        super().__init__(n, g)
        self.name = n
        self.grade = g
        self.transfer_date = td

    def print_date(self):
        print(self.transfer_date)

print('\n-------------------------------------------')
# Parent Class. Define Objects and test 'failed_class()' method.
print('\n- Parent Class. Define 2 Objects and test \'failed_class()\' method '
      '(6 to pass).\n')

print('>>> stud1 = Students(\'Troy\', 5.5)')
print('>>> stud2 = Students(\'Adam\', 8)')

stud1 = Students('Troy', 5.5)
stud2 = Students('Adam', 8)

print('\nstud1.failed_class() -->', stud1.failed_class())
print('stud2.failed_class() -->', stud2.failed_class())

print('\n-------------------------------------------')
# Case 1 --> Inheritance + new method extension.
print('\n- Case 1: create 2 different ArabStudent objects, that will take attributes '
      'from the \'Students\' Class,\nand test the \'is_arab()\' method.\n')

print('>>> astud1 = ArabStudents(\'Jim\', 8.5)')
print('>>> astud2 = ArabStudents(\'Mohamad\', 9)')

astud1 = ArabStudents('Jim', 8.5)
astud2 = ArabStudents('Mohamad', 9)

print('\nastud1.is_arab() -->', astud1.is_arab())
print('astud2.is_arab() -->', astud2.is_arab())

print('\n-------------------------------------------')
# Case 2 --> Inheritance + method overriding.
print('\n- Case 2: create 2 different HonorStudent objects, that will take attributes '
      'from the \'Students\' Class,\nbut override the \'failed_class()\' method by '
      'modifying the required grade to pass (from 6 to 7).\n')

print('>>> hstud1 = HonorStudents(\'Mark\', 6.5)')
print('>>> hstud2 = HonorStudents(\'Layla\', 8)')

hstud1 = HonorStudents('Mark', 6.5)
hstud2 = HonorStudents('Layla', 8)

print('\nhstud1.failed_class() -->', hstud1.failed_class())
print('hstud2.failed_class() -->', hstud2.failed_class())

print('\n-------------------------------------------')
# Case 3 --> Inheritance + attributes update.
print('\n- Case 3: create 2 different NewStudent objects, that will update the parent '
      'attributes from \'Students\'\nby adding an extra one, and run its method to '
      'display said attribute in both created objects.\n')

print('>>> nstud1 = NewStudents(\'Zack\', 7.5, \'05/06/2016\')')
print('>>> nstud2 = NewStudents(\'John\', 8, \'18/04/2018\')')

nstud1 = NewStudents('Zack', 7.5, '05/06/2016')
nstud2 = NewStudents('John', 8, '18/04/2018')

print('\nnstud1.print_date():'), nstud1.print_date()
print('nstud2.print_date():'), nstud2.print_date()

print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
