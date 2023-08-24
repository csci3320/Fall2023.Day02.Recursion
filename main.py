#
# Simple program to show how recursion can act the same 
# as a for loop.
#

# A function that calls a for loop

def forLoop(start, stop, increment):
    for currentValue in range(start,stop,increment):
        print(currentValue)

# The function that will be called recursively
def recurse(currentValue, stop, increment):
    if currentValue >= stop:
        return
    print(currentValue)
    currentValue += increment
    recurse(currentValue, stop, increment)

# A function that loops using recursion
def recursion(start, stop, increment):
    recurse(start, stop, increment)

# Call both loops
# The output should be the numbers 0 to 5 twice.
forLoop(0,6,1)
recursion(0,6,1)


