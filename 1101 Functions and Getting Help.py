help(round)

round(1.56666,ndigits=4)

help(print)

a = 10
b = 20
print(a,b,sep=' xYx ', end='\t', flush=True)
print(10)

import sys 
import time 
  
for i in range(10): 
    print(i, end =' ') 
    sys.stdout.flush() 
    time.sleep(1) 
	
for i in range(10):
    print(i, end=' ', flush=True)
	
def least_difference(a, b, c):
    diff1 = abs(a-b)
    print('diff 1',diff1)
    diff2 = abs(b-c)
    print('diff 2',diff2)
    diff3 = abs(a-c)
    print('diff 3',diff3)
    return min(diff1, diff2, diff3)
	
print('Total least difference',least_difference(1,2,3))

print(
    "Total 1:",
    least_difference(1, 5, 10),
    "\nTotal 2:",
    least_difference(10, 20, 40),
    "\nTotal 3:",
    least_difference(30, 60, 90)
)

help(least_difference)

def least_difference(a, b, c):
    """
    Return Value of A,B,C
    
    >>> least_difference(1, 2, 3)
    1
    """
    
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
	
help(least_difference)

def least_difference(a, b, c):
    """
    Return the smallest difference between any two numbers
    among a, b, c
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)

mystery = print()
print(mystery)

print(1, 2, 3, sep = ' < ')

print(1, 2, 3)

def greet(who="Colin"):
    print("Hello", who)
    
greet()
greet(who="Kaggle")
greet("world")

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 2),
    sep = '\n'
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep = '\n'
)