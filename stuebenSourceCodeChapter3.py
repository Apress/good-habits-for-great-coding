"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 3              |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 3 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################

#--------------------------------------------------------------------Chapter 3--
def fibA(n):
    if n <= 2: return n
    a = 1
    b = 1
    tmp = 0
    for i in range(n-2):
        tmp = b
        b  += a
        a   = tmp
    return b
#--------------------------------------------------------------------Chapter 3--

def fibC(n, d:dict):
     if n <= 2: return 1
     if n-1 in d: a=d[n-1]
     else: a = fibC(n-1,d)
     if n-2 in d: b = d[n-2]
     else: b = fibC(n-2,d)
     d[n] = a+b
     return a+b
#====================================<MAIN>=====================================

def main():
    print(fibA(25))
    print(fibC(25, {}))
#--------------------------------------------------------------------Chapter 3--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
