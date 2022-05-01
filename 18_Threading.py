"""
UPDATE TO PYTHON 3.10

                                THREADS AND THREADING
                                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
When you need Python to execute more than one line of code at a time, the Threading
module must be called.

Let's imagine we have a box, and we want to open and close it automatically, every 5
seconds. The box also has an LED light which we want to turn On and Off every second.
In the following example, we will see how we can create a code to perform both tasks.

https://www.geeksforgeeks.org/multithreading-python-set-1/
"""
# EXAMPLE:
import time
from threading import Thread
print('')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

# Define a function for the box.
def box():
    while True:
        print('---- The Box is Open ----')
        time.sleep(5) # 'sleep()' is used to time Python executions.
        print('--- The Box is Closed ---')
        time.sleep(5)

# Define a function for the LED light.
def led():
    while True:
        print('LED On')
        time.sleep(1)
        print('LED Off')
        time.sleep(1)

"""
Both functions box() and led() perform the needed tasks, but when run, Python will only
be able to perform either the box task or the LED task, because both functions perform
infinite loops and Python is able to run one thing at a time. For this, we create
Threads (as objects in a class), which can run in parallel with the main program.
"""
# Define a Thread for each previously defined function.
boxThread = Thread(target = box())
ledThread = Thread(target = led())

"""
Similar to how .txt files must be closed after used, threads must be terminated after
execution, otherwise they would keep working after the main program shuts down. We can
successfully kill threads by using the '[thread].daemon = True' method:
"""
# Terminate both thread executions.
boxThread.daemon = True
ledThread.daemon = True

# Now execute the threads.
boxThread.start()
ledThread.start()

"""
Now, if we ended the program right here, after the last line of code the program would,
shutting down both threads, so to avoid this we can create an infinite loop to avoid the
program from shutting down.
"""
# Define an infinite loop that will both prevent the program from ending its execution
# and also count every tenth of a second.
x = 0
while True:
    pass
    print(x)
    x += .1
    time.sleep(.1)