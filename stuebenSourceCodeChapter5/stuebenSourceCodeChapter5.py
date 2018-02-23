"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 5              |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 5 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
#========================<GLOBAL IMPORTS AND CONSTANTS>=========================

WIDTH = 512; HEIGHT = 512
class ImageFrame:
    def __init__(self, colors, wd = WIDTH, ht = HEIGHT, colorFlag = False):
        self.img = PhotoImage(width = wd, height = ht)
        for row in range(ht):
            for col in range(wd):
                num = colors[row*wd + col]
                if colorFlag == True:
                   kolor ='#%02x%02x%02x' % (num[0], num[1], num[2]) # = color
                else:
                   kolor ='#%02x%02x%02x' % (num, num, num)     # = gray-scale
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = wd, height = ht); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElapsedTime ('displayed image')
#--------------------------------------------------------------------Chapter 5--

def solutionIsCorrect(matrix):
#---Build lists of rows and columns.
    rows = [[]] * MAX
    cols = [[]] * MAX
    for r in range(MAX):
        for c in range(MAX):
            rows[r].append(matrix[r][c].value)
            cols[c].append(matrix[r][c].value)

#---Build list of blocks.
    block  = []
    for n in range(MAX):
        block.append([])
    for n in range(MAX):
        for r in range(blockHeight):
            for c in range(blockWidth):
                  row = (n//blockWidth)*blockHeight+r
                  col = (n%blockHeight*blockWidth) +c
                  block[n].append(matrix[row][col].value)

#---Check all rows for all n digits.
    for r in rows:
        for n in range(1, MAX+1):
            if {n,} not in r:  #  <--The type must be set({n}), not int (n).
                return False

#---Check all columns for all n digits.
    for c in cols:
        for n in range(1, MAX+1):
            if {n,} not in c:
                return False

#---Check all blocks for all n digits.
    for b in block:
        for n in range(1, MAX+1):
            if {n,} not in b:
                return False
    return True # True means NO errors in the matrix.
#--------------------------------------------------------------------Chapter 5--

def createAlphametic():
    from itertools import permutations
    from re        import findall  # re stands for regular expressions.
    puzzle = 'SEND + MORE == MONEY' # Notice we use '==', not '='.
    puzzle = 'OOOH + FOOD == FIGHT' # 8886 + 1883 == 10769
    print(' NOW ATTEMPTING TO FIND ALL\n SOLUTIONS FOR THIS ALPHAMETIC\n PUZZLE:', puzzle)
    solutionFound = False
    count = 0

    words = findall('[A-Z]+', puzzle.upper())        # words = ['SEND', 'MORE', 'MONEY']
    keys  = set(''.join(words))                      # keys  = {'Y', 'S', 'R', 'M', 'O', 'N', 'E', 'D'}
    if len(keys) > 10:
       print('--- ERROR: The puzzle has MORE than ten letters.')
       exit()
    initialLetters   = {word[0] for word in words}   # Example: initialLetters = {'M', 'S'}
    numberOfInitials = len(initialLetters)
    keys             = ''.join(initialLetters) + ''.join(keys - initialLetters) # Example: keys = 'MSEDONRY'

    for values in permutations('1234567890', len(keys)):
        values = ''.join(values)        # Example: ('1', '2', '3', '4', '5', '6', '7', '8') becomes '12345678'
        if '0' in values[0:numberOfInitials]:        # No zeros are allowed in initial letters.
            continue               # If eval() finds a number beginning with zero, it will throw an exception.
                                                     #         'M':  3,  'S':  8,  'E':  5, ...}
        table    = str.maketrans(keys, values)       # table = {77: 51,   83: 56,   69: 53, ...}
        equation = puzzle.translate(table)           # Example: equation = 8514 + 3275 == 32156
        if eval(equation):
           solutionFound = True
           if count == 0:
              print('------------------------------------')
              print('All solutions are listed below:')
           count += 1
           print(count,'. ', equation, sep = '')

    if not solutionFound:
       print('No solutions exist.')
#====================================<MAIN>=====================================
from tkinter import *
def main():
    global x # This line is necessary.
    image = [0]*(512*512)
    x = ImageFrame(image)

#--------------------------------------------------------------------Chapter 5--
if __name__ == '__main__':
    from time import clock; START_TIME = clock();main(); print('\n   '+'- '*12);
    print('   PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################


