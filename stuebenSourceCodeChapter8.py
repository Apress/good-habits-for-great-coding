"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 8              |
       |                               by                              |
       |                  M. Stueben (December 29, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 8 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
graph =  {'A':[('Z',  75), ('T', 118), ('S', 140)],
          'Z':[('A',  75), ('O',  71)],
          'T':[('A', 118), ('L', 111)],
          'L':[('T', 111), ('M',  70)],
          'M':[('L',  70), ('D',  75)],
          'D':[('M',  75), ('C',  120)],
          'C':[('D', 120), ('R',  146), ('P',  138)],
          'R':[('C', 146), ('P',   97), ('S',   80)],
          'S':[('R',  80), ('F',   99), ('O',  151), ('A', 140)],
          'O':[('S', 151), ('Z',   71)],
          'P':[('C', 138), ('R',   97), ('B',  101)],
          'F':[('S',  99), ('B',  211)],
          'B':[('P', 101), ('F',  211), ('G',   90), ('U',  85)],
          'G':[('B',  90)],
          'U':[('B',  85), ('H',   98), ('V',  142)],
          'H':[('U',  98), ('E',  86)],
          'E':[('H',  86)],
          'V':[('U', 142), ('I',   92)],
          'I':[('V',  92), ('N',   87)],
          'N':[('I',  87)],}
#--------------------------------------------------------------------Chapter 8--

def isAllVowels(stng):
    for ch in stng.lower():
        if ch not in ['a', 'e', 'i', 'o', 'u']:
           return False
    return True
#--------------------------------------------------------------------Chapter 8--

def printBoard(board):                 # Example: board = [3,5,7,2,0,6,4,1]
    print("###################")
    for col in board:
        s = ['- '] * len(board)        # build a list of strings with no 'Q '
        s[col] = 'Q '                  # insert 'Q 's in the correct places
        print('# ' + ''.join(s) + "#") # make the list into one string.
    print("###################")
#--------------------------------------------------------------------Chapter 8--


def DFS_FewestNodesPath(node, goalNode, path=[]):
# Notes: 1. We avoid loops by reference to the path itself.
#        2. The recursion will be unwound just below the recursive call at (*).

#---Append current node.
    path = path + [node]

#---base case
    if node == goalNode:
       return path

#---recursive case
    bestPathSoFar = []
    for (child, dist) in graph[node]: # dist is a dummy variable that is never used.
        if child not in path:
           newPath = DFS_FewestNodesPath(child, goalNode, path)               # <-- (*)
           if newPath and (len(newPath) < len(bestPathSoFar) or bestPathSoFar == []):
              bestPathSoFar = newPath

#---Return best path, which could be [].
    return bestPathSoFar
#--------------------------------------------------------------------Chapter 8--

# VERSION 2.
def permute(Lst, r):
    from math import factorial
    Lst = Lst[:]
    L = len(Lst)
    assert L>=1 and r>=0 and r<factorial(L) and \
           type(Lst) == list and type(r)==int
    if L == 1: return Lst
    d     = factorial(L-1)
    digit = Lst[r//d]
    Lst.remove(digit)
    return [digit] + permute(Lst, r%d)
#--------------------------------------------------------------------Chapter 8--

def repeatingDecimalToFraction(number, repLength):
#---Preconditions: number is float type, repLength is integer and 0 < repLength <= length of decimal portion.
    numberCastToString     = str(number)
    decimalPointPosition   = numberCastToString.find('.')
    lengthOfDecimalPortion = len(numberCastToString) - decimalPointPosition - 1

                                               # == AN EXAMPLE IS GIVEN TO MAKE THIS ALGORITHM CLEAR. ==
                                               # number              = 12.34567 <-- Here, the 67 repeats.
                                               # repLength           = 2, the length of 67
    numberlength = len(numberCastToString)     # numberlength        = 8, the total length
    lengthOfIntegerPart = len(str(int(number)))# lengthOfIntegerPart = 2, the length of 12
    shiftLength = numberlength - (lengthOfIntegerPart + 1 + repLength) # 1 is for the decimal point.
                                               # shiftLength         = 8 - (2 + 1 + 2) = 3, the distance
                                               # from the decimal point in 12.34567 to the repeating part (67)
    factor1 = int (10**(shiftLength+repLength))# factor1             =  100000
    factor2 = int (10**shiftLength)            # factor2             =    1000
    numberTimesFactor1 = int(number * factor1) #                     = 1234567.676767
    numberTimesFactor2 = int(number * factor2) #                     =   12345.676767
    numerator = numberTimesFactor1 - numberTimesFactor2 #            = 1234567.676767 - 12345.676767 = 1222222
    denominator = factor1 - factor2            # = 99000 (= 100000x - 1000x = (100000 - 1000)x
    return numerator, denominator              # postcondition: integer types are returned.

#====================================<MAIN>=====================================

def main():
    print(isAllVowels('aeiouy'))
    board = [3,5,7,2,0,6,4,1]
    printBoard(board)
    print(DFS_FewestNodesPath(node = 'A', goalNode = 'B'))
    print(permute(['a','b','c','d',],2))
    print(repeatingDecimalToFraction(12.345, 2)) # = 12.3454545...

#--------------------------------------------------------------------Chapter 8--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
