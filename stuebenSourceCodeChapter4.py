"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 4              |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 4 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################

#========================<GLOBAL IMPORTS AND CONSTANTS>=========================
from sys import setrecursionlimit; setrecursionlimit(100) # default = 1000
from random import random, randint, uniform, shuffle, choice
#====================================<MAIN>=====================================
def fibH(num, a = 0, b = 1): # 31.91 seconds.
    if num == 1:
        return b
    return fibH(num - 1, b, a+b)
#--------------------------------------------------------------------Chapter 4--

def fibHH(n, a = 0, b = 1): # 31.91 seconds.
    return fibHH(n-1, b, a+b) if n > 1 else b
#--------------------------------------------------------------------Chapter 4--

f = lambda n, a=1, b=1: int(n<3) or a+f(n-1,b,a+b) # 56.08 seconds.
#--------------------------------------------------------------------Chapter 4--

def factorial1(n):        # Tail recursion 1 = 12.25 seconds
    if n == 1: return 1
    return n*factorial1(n-1)
#--------------------------------------------------------------------Chapter 4--

def factorial2(n, x = 1): # Tail recursion 2 = 13.72 seconds
    if n == 1: return x
    return factorial2(n-1, n*x)
#--------------------------------------------------------------------Chapter 4--

def factorial3(n):        # non-Tail recursion = 11.88 seconds
    if n == 1: return 1
    return factorial3(n-1)*n
#--------------------------------------------------------------------Chapter 4--

def factorial4(n):        # Iteration = 5.51 seconds
    t = 1
    for n in range(1,n+1):
        t = t*n
    return t
#--------------------------------------------------------------------Chapter 4--

def factorial5(n):        # Tail recursion with look-up table = 12.36 seconds
    if n <=11:
        return [0,1,2,3,24, 120, 720, 5040, 40320,362880, 3628800, 39916800][n]
    return n*factorial5(n-1)
#--------------------------------------------------------------------Chapter 4--

def factorialA(n):
    return (n>1) and (n*factorialA(n-1)) or 1
#--------------------------------------------------------------------Chapter 4--

def factorialB(n, x = 1):
    return (n>1) and factorialB(n-1, n*x) or x
#--------------------------------------------------------------------Chapter 4--

def fibIII(n): # 1.61 seconds. (Remember, fibA took 7.45 seconds.)
    def mul(A, B): # multiply two 2x2 matrices
        a, b, c, d = A
        e, f, g, h = B
        return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h
    A = [1,1,1,0]         # = Fibonacci matrix. We will generate A, A^2, A^4, A^8, A^16,
                          #   etc., some of which can be combined to produce matrix X.
    X = [1,0,0,1]         # = identity  matrix, which will later contains the answer:
    s = str(bin(n))[2:]   #   x[1] = fibIII(n). The str(bin(n))[2:] will change fibIII
    s = s[::-1]           #   number to a binary string--e.g., n = 12 --> Ã¢â‚¬Ëœ1100Ã¢â‚¬â„¢.
    for n in range(len(s)): # The s[::-1]will reverse digits in a binary string.
        if s[n] == '1':
            X = mul(X, A) # Matrix X accumulates some of the powers of matrix A--
        A = mul(A, A)     # e.g., X = A^12 = A^4 + A^8.
    return X[1]
#--------------------------------------------------------------------Chapter 4--

def fibII(n): # 2.10 seconds
    A = [1,1,1,0]         # = Fibonacci matrix.

    X = [1,0,0,1]         # = identity  matrix.
    s = str(bin(n))[2:]   # Change fibII number to a binary string--e.g., n = 12 --> 1100.
    s = s[::-1]           # Reverse digits in binary string--e.g., 1100 --> 0011.
    for n in range(len(s)):
        if s[n] == '1':
           X = X[0]*A[0] + X[1]*A[2], X[0]*A[1] + X[1]*A[3], X[2]*A[0] + \
               X[3]*A[2], X[2]*A[1] + X[3]*A[3]
        A = A[0]*A[0] + A[1]*A[2], A[0]*A[1] + A[1]*A[3], A[2]*A[0] + \
            A[3]*A[2], A[2]*A[1] + A[3]*A[3]
    return X[1]
#--------------------------------------------------------------------Chapter 4--

def fibI(n): # 1.37 seconds.
    a,b,c,d = 1,1,1,0   # = Fibonacci matrix.
    e,f,g,h = 1,0,0,1   # = identity  matrix.
    s = str(bin(n))[2:] # = base 2 representation of n--e.g., if n = 12, then s= "1100".
    r = s[::-1]          # = reversed version of s--e.g.,  if s = "1100", then r= "0011".
    for n in range(len(r)):
        if r[n] == '1':
           e,f,g,h = a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h       # = X*Y (2x2 matrix mult).
        a,b,c,d = a*a + b*c, a*b + b*d, c*a + d*c, c*b + d*d  # = Y*Y (2x2 matrix mult).
    return f
#--------------------------------------------------------------------Chapter 4--

def fibJJ(n): # 3158.00 seconds
    if n < 3:
        return 1

    if (n%2) == 0:
        k = n//2
        return fibJJ(k)*(2*fibJJ(k+1)-fibJJ(k))

    k = (n-1)//2
    return fibJJ(k+1)*fibJJ(k+1) + fibJJ(k)*fibJJ(k)
#--------------------------------------------------------------------Chapter 4--

def fibJ(n): # 5.00 seconds
    if n < 18:
        return [0,1,1,2,3,5,8,13,21,34,55,89,
                144,233,377,610,987,1597,][n]
    if (n%2) == 0:
        k = n//2
        f = fibJ(k)
        g = fibJ(k+1)
        return f*(2*g-f) # = fibJ(k)*(2*fibJ(k+1)-fibJ(k))
    k = (n-1)//2
    f = fibJ(k)
    g = fibJ(k+1)
    return g*g + f*f # = fibJ(k+1)*fibJ(k+1) + fibJ(k)*fibJ(k)
#--------------------------------------------------------------------Chapter 4--

def fibK(n, dict = {}): # 1.19 seconds
    if n < 18:
        return [0,1,1,2,3,5,8,13,21,34,55,89,
                144,233,377,610,987,1597,][n]

    if (n%2) == 0:
        k = n//2
        if k not in dict:
             dict[k] = fibK(k, dict)
        A = dict[k]
        if (k+1) not in dict:
              dict[k+1] = fibK(k+1, dict)
        B = dict[k+1]
        return 2*A*B-A*A
    else:
        k = (n-1)//2
        if (k+1) not in dict:
                dict[k+1] = fibK(k+1, dict)
        A = dict[k+1]
        if k not in dict:
             dict[k] = fibK(k, dict)
        B = dict[k]
        return A*A + B*B
#--------------------------------------------------------------------Chapter 4--

def fibL(n): # 0.63 seconds [0.46 seconds with the look-up table.]
    if n == 0:
        return (0, 1)
##    if n < 18: # Optional base case look-up table.
##        return [(0,1),(1,1),(1,2),(2,3),(3,5),(5,8),(8,13),(13,21),(21,34),(34,55),
##                (55,89),(89,144),(144,233),(233,377),(377,610),(610,987),(987,1597),
##                (1597,2584),][n]
    else:
        a, b = fibL(n // 2)    # a = fibL(2*k); b = fibL(2*k+1).
        c = a*(2*b - a)        # fibL(2*k  ) = fibL(k)*(2*fibL(k+1) - fibL(k))
        d = a*a + b*b          # fibL(2*k+1) = fibL(k+1)^2 + fibL(k)^2
        if (n%2) == 0:
            return (c, d)      # return fibL(k), fibL(k+1)
        else:
            return (d, c + d)  # return fibL(k), fibL(k+1)
#====================================<MAIN>=====================================

def main():
   print(fibH(25))
   print(fibHH(25))
   print(f(25))
   print(factorial1(17))
   print(factorial2(17))
   print(factorial3(17))
   print(factorial4(17))
   print(factorial5(17))
   print(factorialA(17))
   print(factorialB(17))
   print(fibIII(25))
   print(fibII(25))
   print(fibI(25))
   print(fibJJ(25))
   print(fibJ(25))
   print(fibK(25))
   print(fibL(25))
#--------------------------------------------------------------------Chapter 4--
if __name__ == '__main__':
    from time import clock; START_TIME = clock();main(); print('\n   '+'- '*12);
    print('   PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
