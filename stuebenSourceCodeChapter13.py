"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 13             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 13 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
def binarySearchTest():
    array = [0,1,2,3,4,6,7,8,9] # <--5 is missing
    print('array   =', array)
    print('Test -9 =', binarySearch(array,-9) == -1)
    print('Test  0 =', binarySearch(array, 0) ==  0)
    print('Test  4 =', binarySearch(array, 4) ==  4)
    print('Test  5 =', binarySearch(array, 5) == -1)
    print('Test  9 =', binarySearch(array, 9) ==  9)
    print('Test 10 =', binarySearch(array,10) == -1)
#-------------------------------------------------------------------Chapter 13--

def binarySearchTest():
    runs = 1000 # The number of random arrays to be tested.

#---A function to verify the binarySearch for a single element.
    def check(array, value):
        valueIndex = binarySearch(array, value)
        if ((valueIndex == -1) and (value in array)) or \
           ((valueIndex != -1) and (array[valueIndex] != value)):
           print('\nFALSE: array =', array)
           print('The position of', value, 'is returned as', valueIndex)
           exit()

#---Check all numbers in all random arrays created below.
    for i in range(runs):
#-------Create a random sized array each with different random values.
        arrayLength = randint( 0, 30)
        sm          = randint(-5, 20)   # sm = smallest possible value in array.
        lg          = randint(20, 40)   # lg = largest  possible value in array.
        array       = sorted([randint(sm,lg) for j in range(0,arrayLength)])
#-------Test every value possible in the array and many not in the array.
        for value in range(sm-2, lg+2):
            check(array, value)
    print('True: The binarySearch function passed', runs, 'tests.')
#-------------------------------------------------------------------Chapter 13--

def binarySearch(array, target):
    # UNCHECKED preconditions: array is a list of sorted integers.
    left  = 0
    right = len(array)-1

    while left < right:
        mid = (left + right)//2   # rounds down.
        if array[mid] == target:
            return mid
        if array[mid] < target:
            if left == mid:
                left = left+1
            else:
                left = mid
        else:
            right = mid

#---Check for empty array or possible solution where left = right.
    if (array != []) and (array[left] == target):
       return left # left = right = index of target.
    return -1      # Either array = [], or target not in array.
#-------------------------------------------------------------------Chapter 13--

def binarySearch(array, target): # A better design. 29.51 seconds
    left  = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2    # rounds down.
        if array[mid] < target:
           left = mid+1
        elif array[mid] > target:
           right = mid-1
        else:
           return mid
    return -1
#-------------------------------------------------------------------Chapter 13--

def binarySearchUT(array, target): # Untangled code. 39.33 seconds
    left  = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2   # rounds down.
        if array[mid]  < target: left  = mid+1
        if array[mid]  > target: right = mid-1
        if array[mid] == target: return mid
    return -1
#====================================<MAIN>=====================================

def main():
    array = [0,1,2,3,4,5,7,8,9,10]
    print(binarySearch(array, 6))
#-------------------------------------------------------------------Chapter 13--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
