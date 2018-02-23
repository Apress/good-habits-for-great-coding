"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 14             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 14 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
def quad(a, b, c):
    from math import sqrt
    disc = b*b-4*a*c
    if disc < 0:
        return 'There are no real roots.'
    x1 = (-b+sqrt(disc))/(2*a)
    x2 = (-b-sqrt(disc))/(2*a)
    if disc == 0:
        return x1
    return x1, x2

#-------------------------------------------------------------------Chapter 14--
def quad(a, b, c):
#---Rescale all three coefficients to prevent overflow of b*b and 4*a*c. (Python
#   has 16-17 digits of accuracy.) Underflow is still possible. Mathematically
#   the roots are not changed by this process.
    m = max(abs(a),abs(b),abs(c))
    if m != 0:
        a1 = a/m
        b1 = b/m
        c1 = c/m # Now the largest parameter (a, b, c) is 1.

#---Special case 1: a = 0, b = 0, and c = 0.
    if a == 0 and b == 0 and c == 0:
        return 'All real numbers are roots.'

#---Special case 2: a = 0, b = 0, and c != 0.
    if a == 0 and b == 0 and c != 0:
        return 'There are no roots (real or otherwise).'

#---Special case 3: a = 0 and b != 0.
    if a == 0 and b != 0:
       x1 = -c/b # = the only root.
       #-Cast as int type if possible (optional).
       if x1 == int(x1): x1 = int(x1) # This turns -0.0 into 0.
       return  x1

#---Bookkeeping.
    from math import sqrt
    disc = b*b-4*a*c

#---Special case 4: sqrt of negative number.
    if disc < 0:
        return 'There are no real roots.'

#---Special case 5: a != 0, b = 0, c = 0 (Needed for case 6.)
    if a != 0 and b == 0 and c == 0:
        return 0

#---Special case 6: Rationalize the numerator in one of the roots. Why? If b*b
#   is much much larger than 4*a*c, then sqrt(disc) = |b|. Consequently,
#   -b + sqrt(b*b) will be zero for b > 0, and -b - sqrt(b*b) will be zero
#   for b < 0. We need the "+" and "-" signs reversed in these two situations.
    if b > 0:
        x1 = (-b-sqrt(disc))/(2*a)
        x2 = (-2*c)/(b+sqrt(disc)) # = (-b+sqrt(disc))/(2*a)
    else:
        x1 = (-b+sqrt(disc))/(2*a)
        x2 = (-2*c)/(b-sqrt(disc)) # = (-b-sqrt(disc))/(2*a)

#---Cast as int types if possible (optional). This turns -0.0 int 0.
    if x1 == int(x1): x1 = int(x1)
    if x2 == int(x2): x2 = int(x2)

#---Special case 7. Only one root.
    if disc == 0: return x1

    return x1, x2
#-------------------------------------------------------------------Chapter 14--

def dataInput():
    s = 'Enter an integer:'
    posLimit =  float('inf') # = an optional check for bounds.
    negLimit = -float('inf') # = an optional check for bounds.
    while True:
       try:
          data = input(s)
          num  = int(data) # a non-int will raise exception.
          if not (negLimit < num < posLimit): raise Error # out-of-bounds.
       except:
          s = '"' + str(data) + '" is NOT an integer. \
              Try again. \nEnter an integer:'
       else:
          print('input = ', num)
          return num
#====================================<MAIN>=====================================

def main():
    print(quad(1,2,3))
    print(quad(1,3,2))
    print(quad(1,2,1))
    dataInput()
#-------------------------------------------------------------------Chapter 14--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
