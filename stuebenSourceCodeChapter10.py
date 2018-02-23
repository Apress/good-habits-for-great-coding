"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 10             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 10 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################

def frange(start, stop, step = 1):
    i = start
    while i < stop:
        yield i # <-- not return i
        i += step
#-------------------------------------------------------------------Chapter 10--

def drawCircle(cx, cy, radius, image):
    from math import cos, sin
    for t in frange(0, 6.28, 0.01): # range will not allow float steps.
        x = cx + radius*cos(t)
        y = cy + radius*sin(t)
        image[int(y)*WIDTH  + int(x)] = 255 # <--A
        image[int(y *WIDTH) + int(x)] = 255 # <--B
        image[int(y *WIDTH  +     x)] = 255 # <--C
    return image
#-------------------------------------------------------------------Chapter 10--

def solveEquation(a,b,c,d,x):
#   +---------------------------------------------------------+
#   | Given: (x-a) = (by-c)/(d-y)                             |
#   | Return the unique value for y, if it exists.            |
#   |           [y = (x*d - a*d + c)/(x-a+b).]                |
#   |        If no value for y exists, then print an          |
#   |           error message and exit the program.           |
#   |        If multiple values for y exist, then print       |
#   |           a warning and return a valid value for y.     |
#   +---------------------------------------------------------+

    if (x == (a-b) and (c != b*d)):
       exit('ERROR: No solution. The expression reduces to c = b*d.')

    if (x == (a-b) and (c == b*d)):
       print('WARNING: y is NOT unique: y may take ANY value, except d.')
       return int(not d) # y = 0 or 1

    if (x != (a-b) and (c == b*d)):
       exit('ERROR: No solution. The expression reduces to y = d.')

#---Note: x != (a-b) and c != b*d).
    y = (x*d - a*d + c)/(x-a+b)   # <-- No division by zero and no y = d.
    return y
#-------------------------------------------------------------------Chapter 10--

def antifreeze (quartCap, pct1, pct2):
    # pct1 = current percentage, and pct2 = desired percentage.
    assert 0<= pct1 <=1 and 0<= pct2 <=1 and pct1 <= pct2 and quartCap > 0, \
            ["ERROR (bad input):", quartCap, pct1, pct2] # Note the FOUR cases.
    return round(quartCap*(pct2-pct1)/(1-pct1), 2)

#====================================<MAIN>=====================================

def main():
    quartCap = 100; pct1 = 0.60; pct2 = 0.70
    print(antifreeze (quartCap, pct1, pct2))

    exit()
    a = 1; b = 2; c = 3; d = 4; x = -1
    y = solveEquation(a,b,c,d,x)
    print('Case 1.',  round(x-a, 12) == round((b*y-c) / (d-y), 12))

    a = 1; b = 2; c = 8; d = 4; x = -1
    y = solveEquation(a,b,c,d,x)
    print('Case 2.',  round(x-a, 12) == round((b*y-c) / (d-y), 12))

    a = 1; b = 2; c = 8; d = 4; x = 5
    y = solveEquation(a,b,c,d,x)
    print('Case 3.',  round(x-a, 12) == round((b*y-c) / (d-y), 12))

    a = 1; b = 2; c = 3; d = 4; x = 5
    y = solveEquation(a,b,c,d,x) # y = 3.1666666666666665
    print('Case 4.',  round(x-a, 12) == round((b*y-c) / (d-y), 12))

#-------------------------------------------------------------------Chapter 10--
if __name__ == '__main__':
    from time import clock; START_TIME = clock();main(); print('\n   '+'- '*12);
    print('   PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
