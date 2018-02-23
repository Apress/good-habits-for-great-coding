"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 9              |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 9 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
def printMatrix(Lst, decimalAccuracy = 2):
    print('---MATRIX:')
    if type (Lst) != list or type (Lst[0]) != list:
        print('*' * 45)
        print(' WARNING: The received parameter is NOT a \n',
               'matrix type. No printing was done.        ')
        print('*' * 45)
        return
    maxLength = 0
    for row in Lst:
        for x in row:
            if type(x) == float: x = round(x, decimalAccuracy)
            maxLength = max(len(str(x)), maxLength)
            if type(x) == float:
                 print('%11.2f'%x,      end='')
            elif type(x) == int:
                 print('%8d   '%x,      end='')
            elif type(x) == str:
                 print('%8s   '%x,      end='')
            elif type(x) == bool:
                 print('%8s   '%str(x), end='')
            elif x == None:
                 print('%8s   '%str(x), end='')
            else:
                 print(x, ' ')
        print()
    print('   ==============================')
    print('   cell maxlength =', maxLength, '(8 is limit)')
#====================================<MAIN>=====================================

def main():
    Lst = [[1234, 12, 'happy'], [0.12, 0.1234567, 'a'], [True, None, 1234567890],]
    printMatrix(Lst)
#--------------------------------------------------------------------Chapter 9--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
