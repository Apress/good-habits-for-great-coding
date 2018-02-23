"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 18             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 18 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
Lst =  [14175, 15055, 16616, 17495, 18072, 19390, 19731, 22161, 23320,
        23717, 26343, 28725, 29127, 32257, 40020, 41867, 43155, 46298,
        56734, 57176, 58306, 61848, 65825, 66042, 68634, 69189, 72936,
        74287, 74537, 81942, 82027, 82623, 82802, 82988, 90467, 97042,
        97507, 99564]
def findEqualSumPartition():
    from random import randint
    count = 0
    failed = True
    while failed:
    #----Initializing.
         count += 1
         s = set() # = empty set

    #----Randomly assemble 19 different indices.
         while len(s) < 19:
             s.add(randint(0,37)) # Duplicates are never appended to a set type.

    #----Check the total.
         if sum(Lst[n] for n in s) == 1000000:
         #--Print the solution, if it exists.
            s = sorted(s)
            print('Answer =', end = ' ')
            for n in s:
                print(Lst[n], end =', ')
            print('\ntotal =', sum(Lst[n] for n in s))
            print('This took', count, 'tries.')
            failed = False
#-------------------------------------------------------------------Chapter 18--

def bubble(x):
    leng = len(x)
    for i in range(leng-1):
        for j in range(leng-i-1):
            if x[j] > x[j+1]:
               x[j], x[j+1] = x[j+1], x[j]
    return x
#-------------------------------------------------------------------Chapter 18--

def bub1(x):
    if x[0] > x[1]:
       x[0], x[1] = x[1], x[0]
    if x[1] > x[2]:
       x[1], x[2] = x[2], x[1]
    if x[2] > x[3]:
       x[2], x[3] = x[3], x[2]
    if x[0] > x[1]:
       x[0], x[1] = x[1], x[0]
    if x[1] > x[2]:
       x[1], x[2] = x[2], x[1]
    if x[0] > x[1]:
       x[0], x[1] = x[1], x[0]
    return x
#-------------------------------------------------------------------Chapter 18--

def bub2(x):
    [a,b,c,d] = x
    if a > b:
       a, b = b, a
    if b > c:
       b, c = c, b
    if c > d:
       c, d = d, c
    if a > b:
       a, b = b, a
    if b > c:
       b, c = c, b
    if a > b:
       a, b = b, a
    return [a, b, c, d]
#-------------------------------------------------------------------Chapter 18--

def quickSort(array):
    if len(array) < 2:
        return array
    less, equal, greater = [], [], []
    pivot = array[0]

    for x in array:
        if x <  pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quickSort(less) + equal + quickSort(greater)
#-------------------------------------------------------------------Chapter 18--

def combSort(array):
    aLength    = len(array)
    recentSwap = False
    gap        = aLength
    while recentSwap or gap > 1:
        gap        = max(1, int(gap/1.3))
        recentSwap = False
        for i in range(aLength-gap):
            j = i+gap
            if array[i] > array[j]:
               array[i],  array[j] = array[j], array[i]
               recentSwap = True
    return array
#-------------------------------------------------------------------Chapter 18--

def sortTest(trialRuns, sortFunct):
#---This sub function checks if an array is sorted or not.
    def arraySorted(x):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                print('NOT SORTED! at positions', i, 'and', i+1)
                return False
        return True

#---Create random-sized array of random integers, then sort and check if sorted.
    for n in range(trialRuns):
        listSize = randint(0,50)
        array = []
        r = randint(0,20)
        for i in range(listSize):
            array.append(randint(-r,r))

        sortFunct(array)

        if not arraySorted(array):
            exit()

    print('\nTested', sortFunct)
    print('Passed test of', trialRuns, 'random trialRuns.')
    print('-'*46)
#-------------------------------------------------------------------Chapter 18--

def countSort(array, max):
#---This array is assumed to take values in the range of 0 to max (inclusive).
    counters = [0] * max

    for number in array:
        counters[number] += 1

    array = []
    for (number, count) in enumerate(counters):
        array.extend([number]*count)

    return array
#====================<GLOBAL CONSTANTS and GLOBAL IMPORTS>===================

from random import shuffle, randint
#=====================================<MAIN>====================================

def main():
    findEqualSumPartition()
    sortTest(trialRuns = 10000, sortFunct = combSort)
#-------------------------------------------------------------------Chapter 18--
if __name__ == '__main__':
     from time import clock; START_TIME = clock(); main(); print('- '*12);
     print('RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
