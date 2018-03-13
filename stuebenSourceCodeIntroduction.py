"""    +-------------------------------=-------------------------------+
       |               STUEBEN'S SOURCE CODE: INTRODUCTION             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from the Introduction of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################

#========================<GLOBAL IMPORTS AND CONSTANTS>=========================
from sys import setrecursionlimit; setrecursionlimit(100) # default = 1000
from random import random, randint, uniform, shuffle, choice
#====================================<MAIN>=====================================
def power(base, exponent):
    product = 1
    for n in range(exponent):
        product *= base
    return product
#-----------------------------------------------------------------Introduction--

def powr(b, exp):
    x = 1
    for n in range(exp):
        x *= b
    return x
#-----------------------------------------------------------------Introduction--

def powr(b, exp):
    binStng = bin(exp)[2:] # Change integer exp to a binary string.
    revStng = reversed(binStng) # Reverse the digits (alt. = binStng[::-1]).
    product  = 1
    for ch in revStng:
        if ch == '1':
           product *= b
        b *= b
    return product
#-----------------------------------------------------------------Introduction--

def powr1(b, exp):
    myPowr = 1
    while exp > 0:
        myPowr *= ((~exp)&1) or b
        b *= b
        exp >>= 1  # Shift one bit right.
    return myPowr
#-----------------------------------------------------------------Introduction--

def powr2(b, exp):
    myPowr = 1
    while exp > 0:
        if exp%2 == 1:   # An odd exp means right-most bit is 1.
            myPowr *= b
        b *= b
        exp //= 2
    return myPowr
#-----------------------------------------------------------------Introduction--

def powr3(b, exp):
    return (not exp) or ((powr3(b, exp >> 1)**2) * (((~exp)&1) or b))

"""+===================+========-========*========-========+===================+
   ||                          A SHUFFLING PROBLEM                            ||
   ||                    by M. Stueben (October 8, 2017)                      ||
   ||            Interview Question, Mr. Jones, XYZ Corporation               ||
   ||                                                                         ||
   || Description: By computer stimulation this program determines the prob-  ||
   ||              ability of a deck of 52 cards having at least one unmoved  ||
   ||              card element after shuffling. (Answer: 0.63, rounded.)     ||
   ||                                                                         ||
   || Language:  Python Ver. 3.4                                              ||
   || Graphics:  None                                                         ||
   || Downloads: None                                                         ||
   || Run time:  Approx. 43 seconds for 1,000,000 runs of a 52-element array. ||
   +===========================================================================+
"""
###############################<START OF PROGRAM>###############################
def printHeading():
    print('                     A SHUFFLING PROBLEM')
    print('                   (currently calculating)')
#-------------------------------------------------------------------------------

def shuffleArrays():
    totalArrays = 0 # Arrays with at least one unmoved element after shuffling.
    for trial in range(TRIAL_RUNS):
        array = list(range(LIST_SIZE))
        shuffle(array)
        for num in range(LIST_SIZE):
            if array[num] == num:
                totalArrays += 1
                break
    probability = round(totalArrays/TRIAL_RUNS, 2)
    return probability
#-------------------------------------------------------------------------------

def printResult(probability):
    print('   Result:', probability ,'is the probability of an array having at')
    print('   least one unmoved element after shuffling. This is based')
    print('   on a computer simulation with an array size =', LIST_SIZE, 'and')
    print('  ', TRIAL_RUNS, 'trial runs.')
#=====================<GLOBAL CONSTANTS and GLOBAL IMPORTS>=====================

from random import shuffle
TRIAL_RUNS = 1000000
LIST_SIZE  =      52
assert LIST_SIZE > 1, 'LIST_SIZE must be greater than 1.'
#=====================================<MAIN>====================================

def main():
    printHeading()
    probability = shuffleArrays()
    printResult(probability)
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    from time import clock; START_TIME = clock();main(); print('\n   '+'- '*12);
    print('   PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
