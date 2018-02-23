"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 19             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 19 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
#                       Problem 1 Answers
#=====================<FIVE POSSIBLE ANSWERS>=======================

def upper1(ch): # Bad. It should ignore non-lowercase letters.
    return chr(ord(ch) - 32)
#------------------------------------------------------------

def upper2(ch): # BAD: It aborts program.
    if 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
    exit('ERROR: Bad input = ' + str(ch))
#------------------------------------------------------------

def upper3(ch): # BAD: It returns TWO different data types.
    if 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
    return -1
#------------------------------------------------------------

def upper4(ch): # OK, however, the error traps are unnecessary.
    assert type(ch) == str and len(ch) == 1, ch
    if 'a' <= ch <= 'z':
        ch = chr(ord(ch) - 32)
    return ch
#------------------------------------------------------------

def upper5(ch): # Best: 1. It ignores non-lowercase letters.
                #       2. It returns only one data type.
                #       3. It has no needless error traps.
    if 'a' <= ch <= 'z':
        ch = chr(ord(ch) - 32)
    return ch
#-------------------------------------------------------------------Chapter 19--

#                          Problem 2 Answers
#
def equal1(num1, num2): # Terrible code
#---Check the data
    if not isinstance(num1, (int, float)) or \
       not isinstance(num2, (int, float)):
       return None
#---Return equality (True or false)
    if abs(num1 - num2) < 0.000000000001:
       return True
    return False

def equal2(x, y):  # Ex.: equals2(0.000 000 000 01,  0) is False,
                   # but  equals2(0.000 000 000 001, 0) is True.
    return abs(x-y) <= 1e-12 # 1e-12 = 0.000 000 000 001 (eleven decimal zeros)

def equal3(x, y): # Ex.: equals3(0.000 000 000 01,  0) is False,
                  # but  equals3(0.000 000 000 001, 0) is True.
    return round (x, 11) == round (y, 11) # 1e-12 = 0.000 000 000 001 = 1 billionth
#-------------------------------------------------------------------Chapter 19--

#                                Problem 3 My Answer
def solveBertrandsParadox():
#---Initialize.
    from random import randint
    trials    = 100000
    goldFirst = 0
    goldMatch = 0
    coin      = [['gold',  'gold'  ],
                 ['gold',  'silver'],
                 ['silver','silver'],]

#---Run many simulation trials.
    for n in range(trials):
        drawer   = randint(0,2)
        position = randint(0,1)
        if coin[drawer][position] == 'silver':
           continue
        goldFirst += 1
        if coin[drawer][position] == coin[drawer][1-position]:
           goldMatch += 1

#---Print labeled answer.
    print('Six coin answer for', trials, 'trials:',
            round(goldMatch/goldFirst * 100,  1), '%')

#-------------------------------------------------------------------Chapter 19--

#                                Problem 4 Answers
"""
   VERSION 4a. Two break points are randomly marked on the given stick, and
               the stick is broken into three parts.
"""
def puzzle4a():
    triangleCount = 0

    for n in range(TOTAL_RUNS):
        a, b  = random(), random()
        if a > b:
            a, b = b, a                          # a   = length of left   piece
        if (a < 0.5 and b-a < 0.5 and b > 0.5):  # b-a = length of middle piece.
           triangleCount += 1                    # 1-b = length of right  piece.

    print('Puzzle 6a: The probability of forming a triangle is',
                      round( triangleCount/TOTAL_RUNS, 3) )
#---Output: Probability of forming a triangle is +------+ in 4.39 seconds.
#                                                | 0.25 |
#                                                +------+
#-----------------------------------------------------------computer simulation--


"""
   VERSION 4b. One break point is randomly marked on the given stick. The stick
               is broken into two parts. A second break point is marked on the
               longer of the two sticks. That stick is broken.
"""
#----------------------------------------------------------computer simulation--

def puzzle4b():
    triangleCount = 0

    for n in range(TOTAL_RUNS):
        a = random()
        if a < 0.5:
           b = uniform(a, 1)
        else:
            b = a
            a = uniform(0, b)
        if (a < 0.5 and b-a < 0.5 and b > 0.5): # a < b
           triangleCount += 1

    print('Puzzle 4b: The probability of forming a triangle is',
                      round( triangleCount/TOTAL_RUNS, 3) )
#---Output: Probability of forming a triangle is  +-------+ in 8.3 seconds.
#                                                 | 0.386 |
#                                                 +-------+
#----------------------------------------------------------computer simulation--

"""
   VERSION 4c. One break point is randomly marked on the given stick.
               The stick is broken. One of the sticks is randomly chosen,
               and a second break point is marked on it. That stick is broken.
"""
def puzzle4c():
    triangleCount = 0

    for n in range(TOTAL_RUNS):
        r    = random()      # r = first break point
        if random() < 0.5:   # flip a coin
           a = uniform(0, r) # cut on the left side
           b = r
        else:
            a = r            # cut on the right side
            b = uniform(r, 1)
        if (a < 0.5 and b-a < 0.5 and b > 0.5): # a < b
           triangleCount += 1

    print('Puzzle 4c: The probability of forming a triangle is',
                      round( triangleCount/TOTAL_RUNS, 3) )
#---Output: Probability of forming a triangle is  +-------+ in 8.70 seconds.
#                                                 | 0.193 |
#                                                 +-------+
#----------------------------------------------------------computer simulation--


"""
   VERSION 4d. One break point is randomly marked on the given stick. The stick
               is broken. One of the sticks is randomly WITHN A PROBABILITY
               PROPORTIONAL TO ITS LENGTH, and a second break point is marked
               on it. That stick is broken.
"""
def puzzle4d():
    triangleCount = 0

    for n in range(TOTAL_RUNS):
        r    = random()      # r = first break point
        if random() < r:     # break left stick
           a = uniform(0, r)
           b = r
        else:                # break right stick
            a = r
            b = uniform(r, 1)
        if (a < 0.5 and b-a < 0.5 and b > 0.5): # a < b
           triangleCount += 1

    print('Puzzle 4d: The probability of forming a triangle is',
                      round( triangleCount/TOTAL_RUNS, 3) )
#---Output: Probability of forming a triangle is  +-------+ in 8.68 seconds
#                                                 | 0.25  |
#                                                 +-------+
#-------------------------------------------------------------------Chapter 19--

#                               Problem 5 My Answer
def permute(Lst, r):
    from math import factorial

    L = len(Lst)
    assert L>=1 and r>=0 and r<factorial(L), ['L=', L, 'r=', r]
    Lst = Lst[:]
    if L == 1: return Lst

    d     = factorial(L-1)
    digit = Lst[r//d]
    Lst.remove(digit)
    return [digit] + permute(Lst, r%d)
#-------------------------------------------------------------------Chapter 19--

#                               Problem 6 Answers
#
#--Solution 1 Best, because it is so easy to debug.
    for x in range(1,101):
        if x % 15 == 0: print('Fizz and Buzz'); continue
        if x %  3 == 0: print('Fizz');          continue
        if x %  5 == 0: print('Buzz');          continue
        print(x)
#-------------------------------------------------------------

#--Solution 2  Mr. Stueben's solution.
    for x in range(1, 101):
        if x % 15 == 0:                print('Fizz and Buzz')
        if x % 3  == 0 and x % 5 != 0: print('Fizz')
        if x % 5  == 0 and x % 3 != 0: print('Buzz')
        if x % 5  != 0 and x % 3 != 0: print(x)
#-------------------------------------------------------------


#--Solution 3 Not bad.
    for x in range(1, 101):
        if x % 15 == 0:
            print('Fizz and Buzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)
#-------------------------------------------------------------

#--Solution 4 Clever.
    for x in range(1, 101):
        stng = ''
        if x % 3  == 0: stng += 'Fizz'
        if x % 15 == 0: stng += ' and '
        if x % 5  == 0: stng += 'Buzz'
        print(stng if stng else x)
#-------------------------------------------------------------

#--Solution 5 Maybe too clever.
    for x in range(1, 101):
        stng =      'Fizz and Buzz' if x%15 == 0 \
              else  'Fizz'          if x% 3 == 0 \
              else  'Buzz'          if x% 5 == 0 \
              else  ''
        print(stng if stng else x)
#-------------------------------------------------------------

#--Solution 6 # The Ã¢â‚¬Å“notÃ¢â‚¬Â makes the code more difficult to understand.
    for n in range (101):
        stng = str(n)
        if not(n%3): stng = 'Fizz'
        if not(n%5): stng = 'Buzz'
        if not(n%3 + n%5):
                     stng ='Fizz and Buzz'
        print(n, stng)
#-------------------------------------------------------------

#--Solution 7 This code says much about the programmerÃ¢â‚¬â„¢s lack
#             of experience in refactoring.
    for n in range(1,101):
       flag = True
       if n%3 == 0:
          print('Fizz', end = '')
          if n%15 == 0:
             print(' and Buzz', end = '')
          print()
          flag = False
       if flag and n%5 == 0:
          print('Buzz')
          flag = False
       if flag:
          print(n)
#-------------------------------------------------------------

#--Solution 8 Why would anyone work with x+1 instead of x? Why would
#             anyone write Ã¢â‚¬Å“if (x+1) % 3 == 0: if (x+1) % 5 == 0Ã¢â‚¬Â,
#             instead of a single Ã¢â‚¬Å“if (x+1) % 15 == 0Ã¢â‚¬Â?
    for x in range(100):
        if (x+1) % 3 ==0:
           if (x+1) % 5 == 0:
              print('Fizz and Buzz')
           else:
              print('Fizz')
        elif (x+1) % 5 == 0:
              print('Buzz')
        else:
              print((x+1))
#=====================================<MAIN>====================================

def main():
    pass
#-------------------------------------------------------------------Chapter 19--
if __name__ == '__main__':
     from time import clock; START_TIME = clock(); main(); print('- '*12);
     print('RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
