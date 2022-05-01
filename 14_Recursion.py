"""
                                     RECURSION
                                     ‾‾‾‾‾‾‾‾‾
Recursion is the way a big process can be arranged in smaller processes in order to
complete a series of tasks in a more efficient manner, by delegating functionality to
the smaller processes.

Let's say the CEO of a large company wants to know how many people work for said company.
One way of doing so, is to spend a big amount of time and effort counting up the number
of people on the company's payroll. However, a CEO has more important things to do, so he
implements a different, more clever strategy: recursion (delegate)...

...He calls a meeting with all department directors and asks everyone to report how many
people work on their respective departments. Each director then calls all their managers,
who subsequently call all their supervisors to perform the task. Each supervisor already
knows how many people work under them, and immediately report this information back to
their managers, who subsequently report to their department directors, finally reporting
back to the CEO.

By going over the second strategy, the CEO accomplished what was a difficult and tedious
task if done on his own, but made fast and easy by delegating similar tasks to his
subordinates.

This method of solving difficult problems by breaking them into simpler tasks is called
RECURSION, and represents the basis of engineering and science problem-solving
techniques. In programming, recursive functions are used to accomplish large tasks.


                                 RECURSIVE FUNCTIONS
                                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Recursive functions are functions that make calls to themselves. They work like a mix of
loops and nested functions, and used when a function is more suited than a loop.

Every recursive function has 2 components:
- The base function or base case, where the main function is defined. It is usually the
  smallest input and has an easily verifiable solution. It is also the mechanism that
  stops the function from calling itself forever.
- The recursive step, the set of all cases where recursive calls are made (where the
  function calls itself).

 ╔════════════════════════════════════════════════╗
 ║ def [BASE FUNCTION]():                         ║
 ║                                                ║
 ║                     │                          ║
 ║                     │  -->  [RECURSIVE CALLS]  ║
 ║                     │                          ║
 ║                                                ║
 ║     [BASE FUNCTION]()  -->  (Function call)    ║
 ╚════════════════════════════════════════════════╝
"""
# EXAMPLE:
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Lets create a recursive function to print \'x\' number of steps in the Fibonacci '
      'sequence,\nwhich starts with a \'0\' and a \'1\', and continues each step '
      'with a sum of the previous 2\nsteps, like so: 0, 1, 1, 2, 3, 5, 8, 13, 21, '
      '34, 55, 89, 144, 233, 377, 610, 987, 1597...\n')

print('>>> def rec_fibonacci(x):')
print('>>>     if x <= 1: # ---->  (base case)')
print('>>>         return x')
print('>>>     else: # ---->  (recursive call)')
print('>>>         return rec_fibonacci(x-1) + rec_fibonacci(x-2)')

print('\nNow that the recursive function is complete, lets define a variable to be '
      'used as an argument\nin said function, which could be a user input or a '
      'predefined number. In this case, \'12\'.\n')

print('>>> num_steps = 12')

print('\nNow use both the recursive function and the \'n_steps\' variable in a loop '
      'to get\nthe desired number of steps in the Fibonacci sequence:\n')

print('>>> if num_steps <=0:')
print('>>>     print(\'Invalid input. Number of steps bust be a positive integer.\'')
print('>>> else:')
print('>>>     print(\'Fibonacci sequence up to\', num_step, \'steps:\')')
print('>>>     for i in range(num_steps):')
print('>>>         print(rec_fibonacci(i))')

print('\nFinally, execute:\n')

def rec_fibonacci(x):
    if x <= 1:
        return x
    else:
        return rec_fibonacci(x-1) + rec_fibonacci(x-2)

num_steps = 12

if num_steps <= 0:
    print('Invalid input. Number of steps must be a positive integer.')
else:
    print('Fibonacci sequence up to', num_steps, 'steps:')
    for i in range(num_steps):
        print(rec_fibonacci(i))
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
