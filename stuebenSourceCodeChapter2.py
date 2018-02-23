"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 2              |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 2 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################

#========================<GLOBAL IMPORTS AND CONSTANTS>=========================
from sys import setrecursionlimit; setrecursionlimit(100) # default = 1000
from random import random, randint, uniform, shuffle, choice
#====================================<MAIN>=====================================
def fibA(num): # This function took 7.45 seconds to find the 1000th
               # Fibonacci number 100,000 times in Python Ver. 3.4.
    if num < 3:
       return 1
    a = b = 1
    for i in range(2, num):
        a, b = b, a+b
    return b
#--------------------------------------------------------------------Chapter 2--

def fibB(num): # Too slow.
    if num < 3: return 1
    return fibB(num-1) + fibB(num-2)
#--------------------------------------------------------------------Chapter 2--

def fibBB(num): # Still too slow to compare.
    if num < 18:
       return [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,][num]
    return fibBB(num-1) + fibBB(num-2)
#--------------------------------------------------------------------Chapter 2--

def fibC(num, dict): # 57.11 seconds to find the 1000th Fibonacci number
                     # 100,000 times.
    if num in dict:
        return dict[num]
    dict[num] = fibC(num-1, dict) + fibC(num-2, dict)
    return dict[num]
# The call to fibC looks like this:  print(' C.', fibC(n, {1:1, 2:1}))
#--------------------------------------------------------------------Chapter 2--

def fibD(num): # 73.96 seconds.
    if num in fibD.dict:
        return fibD.dict[num]
    fibD.dict[num] = fibD(num-1) + fibD(num-2)
    return fibD.dict[num]
fibD.dict = {1:1, 2:1}
# A Python function's class variable must be declared BELOW the function.
#--------------------------------------------------------------------Chapter 2--

def fibE(num): # 76.35 seconds.
    def fib(num):
        if num in fib.dict:
            return fib.dict[num]
        fib.dict[num] = fib(num-1) + fib(num-2)
        return fib.dict[num]
    fib.dict = {1:1, 2:1}
    return (fib(num))
#--------------------------------------------------------------------Chapter 2--

def fibF(num, dict = {1:1, 2:1}): # 59.99 seconds.
    if num in dict:
        return dict[num]
    dict[num] = fibF(num-1, dict) + fibF(num-2, dict)
    return dict[num]
#--------------------------------------------------------------------Chapter 2--

def memoize(function):            # function = fibB.
   from sys  import setrecursionlimit; setrecursionlimit(1000) # default = 1000
   dict = {}                      # This line is executed only once.
   def wrapper(num):              # num came from fibB(num).
      if num not in dict:
         dict[num] = function(num)# the return of fibB is always to dict[num].
      return dict[num]            # The return is to function, except for final.
   return wrapper                 # This line  is executed only once.
#--------------------------------------------------------------------Chapter 2--

def timer(function):
    from time import clock
    from sys  import setrecursionlimit; setrecursionlimit(1000) # default = 1000
    startTime = clock()
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    elapsedTime = round(clock()-startTime, 2)
    print('-->', function.__name__ +"'s time =", elapsedTime, 'seconds.')
    return wrapper
#--------------------------------------------------------------------Chapter 2--

def fibG(num):
    from math import sqrt
    phi1 = (1 + sqrt(5))/2
    phi2 = (1 - sqrt(5))/2
    return round((phi1**num - phi2**num) / sqrt(5))
#--------------------------------------------------------------------Chapter 2--

def fibGG(num): # 1153 seconds = 19 minutes and 13 seconds.
    from decimal import Decimal, getcontext
    from math import sqrt
    if num > 70:
        getcontext().prec = 2*num
    phi1 = (Decimal(1) + Decimal(5).sqrt())/Decimal(2)
    phi2 = (Decimal(1) - Decimal(5).sqrt())/Decimal(2)
    return round((phi1**Decimal(num) - phi2**Decimal(num)) /
           Decimal(5).sqrt())
#--------------------------------------------------------------------Chapter 2--

def fibG(num): # Faster version
    from math import sqrt
    sqrt5 = sqrt(5) # Do not compute this number more than once.
    phi   = (1 + sqrt5)/2
    return round((phi**num)/sqrt5)
#====================================<MAIN>=====================================

def main():
#---Create file containing the first max Fibonacci numbers.
    from time import clock
    max = 79 # = One more number than can be read out.
    print('max =', max)
    print('start')
    start = clock()
    file1 = open('g:\\junk.txt', 'w')
    file1.write('1\n')
    a = b = 1
    for i in range(1, max):
        file1.write(str(a)+'\n')
        a, b = b, a+b
    file1.close()
    stop = clock()
    print('stop')
    print('time =', round(stop-start, 2), 'seconds.')

#---Extract a number from of a file of numbers.
    file1 = open('g:\\junk.txt', 'r')
    print('start')
    start = clock()
    for n in range(78):
        file1.readline()
    num = (file1.readline())
    print('num =', num)
    file1.close()
    stop = clock()
    print('stop')
    print('time =', round(stop-start, 2), 'seconds.') # 8.94 seconds.

    print(fibA(12))
    print(fibB(12))
    print(fibBB(12))
    n = 12
    print(' C.', fibC(n, {1:1, 2:1}))
    print(fibD(12))
    print(fibE(12))
    print(fibF(12))
    print(fibG(70))
    print(fibGG(12))
#--------------------------------------------------------------------Chapter 2--
if __name__ == '__main__':
    from time import clock; START_TIME = clock();main(); print('\n   '+'- '*12);
    print('   PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
