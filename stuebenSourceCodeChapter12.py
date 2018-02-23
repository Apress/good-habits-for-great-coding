"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 12             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 12 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
# Method 1 (ugh!)
def indx(array, target): # 11 lines
    if array == []:
        return -1
    n = 0
    found = -1
    length = len(array)
    while n != length:
        if array[n] == target:
            found = n
            break
        n += 1
    return found
#-------------------------------------------------------------------Chapter 12--
def indx(array, target): # 3 lines
    for n in range(len(array)):
        if array[n] == target: return n
    return -1
#-------------------------------------------------------------------Chapter 12--
def indx(array, target): # 4 lines
    try:
       return array.index(target)
    except:
       return -1
#-------------------------------------------------------------------Chapter 12--

def userChoice():
    msg = ''
    pr = """
Enter u for push.
Enter o for pop.
Enter v for view.
Enter q for quit (or push the enter key).

Enter choice: """
    while True:
        try:
           choice = input(msg+pr).strip()[0].lower()
        except:
           return 'q'
        if choice not in 'uovq':
            msg = 'ERROR: "' + choice +'" is an invalid choice. Try again.\n'
        else:
            return choice
#-------------------------------------------------------------------Chapter 12--

def doIt(a,b,c):
    if a == 1:
        if b == 1:
            if c == 1:
                print ('abc')
            else:
                print('ab')
        else:
            print('a')
    else:
        print('-')
#-------------------------------------------------------------------Chapter 12--
def doIt(a,b,c):
    if a != 1:
        print('- '); return
    if b != 1:
        print('a '); return
    if c != 1:
        print('ab'); return
    print('abc')
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 1 (22 lines).
    if a == 1:
       if b == 1:
          if c == 1:
             print ('abc')
          else:
             print ('ab-')
       else:
          if c == 1:
             print('a-c')
          else:
             print('a--')
    else:
       if b == 1:
          if c == 1:
              print ('-bc')
          else:
              print('-b-')
       else:
          if c == 1:
             print('--c')
          else:
             print ('---')
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 2 (8 lines).
    if a == 1 and b == 1 and c == 1: print('abc')
    if a == 1 and b == 1 and c == 0: print('ab-')
    if a == 1 and b == 0 and c == 1: print('a-c')
    if a == 0 and b == 1 and c == 1: print('-bc')
    if a == 0 and b == 0 and c == 1: print('--c')
    if a == 0 and b == 1 and c == 0: print('-b-')
    if a == 1 and b == 0 and c == 0: print('a--')
    if a == 0 and b == 0 and c == 0: print('---')
#-------------------------------------------------------------------Chapter 12--

#---Block 3 (8 simpler lines)
    if (a,b,c) == (1,1,1): print('abc')
    if (a,b,c) == (1,1,0): print('ab-')
    if (a,b,c) == (1,0,1): print('a-c')
    if (a,b,c) == (1,0,0): print('a--')
    if (a,b,c) == (0,1,1): print('-bc')
    if (a,b,c) == (0,1,0): print('-b-')
    if (a,b,c) == (0,0,1): print('--c')
    if (a,b,c) == (0,0,0): print('---')
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 1 (again).
    if inStock(item):
       if name in customerList:
          if price-1 < payment <= price:
             print ('abc')
          else:
             print ('ab-')
       else:
          if price-1 < payment <= price:
             print('a-c')
          else:
             print('a--')
    else:
       if name in customerList:
          if price-1 < payment <= price:
              print ('-bc')
          else:
              print('-b-')
       else:
          if price-1 < payment <= price:
             print('--c')
          else:
             print ('---')
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 2 (again).
    if (    inStock(item) and
            name in customerList and
            price-1 < payment <= price):  print('abc')
    if (    inStock(item) and
            name in customerList and
        not(price-1 < payment <= price)): print('ab-')
    if (    inStock(item) and
        not name in customerList and
            price-1 < payment <= price):  print('a-c')
    if (    inStock(item) and
        not name in customerList and
        not(price-1 < payment <= price)): print('a--')
    if (not inStock(item) and
            name in customerList and
            price-1 < payment <= price):  print('-bc')
    if (not inStock(item) and
            name in customerList and
        not(price-1 < payment <= price)): print('-b-')
    if (not inStock(item) and
        not name in customerList and
            price-1 < payment <= price):  print('--c')
    if (not inStock(item) and
        not name in customerList and
        not(price-1 < payment <= price)): print('---')
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 1 (13 lines).
    if a == 1:
       if b == 1:
          if c == 1:
             print(doIt())
          else:
             print ('error 3')
             return
       else:
          print('error 2')
          return
    else:
       print('error 1')
       return

#-------------------------------------------------------------------Chapter 12--

#---Block 3 (6 lines)
    (item, payment, name) = (0,0,0)
    msg = ['-', '-', '-']
    if inStock(item):              msg[0] = 'a'
    if name in customerList:       msg[1] = 'b'
    if price-1 < payment <= price: msg[2] = 'c'
    print (''.join(msg))
#-------------------------------------------------------------------Chapter 12--

#---BLOCK 2 (4 lines).
    if a != 1:                      print ('error 1'); return
    if a == 1 and b !=1:            print ('error 2'); return
    if a == 1 and b ==1 and c != 1: print ('error 3'); return
    print (doIt())
#====================================<MAIN>=====================================

def main():
    array = [0,1,2,3,4,5,7,8,9,]
    print(indx(array, -1))
    print(indx(array, 5))
    print(indx(array, 6))
    print(indx(array, 10))
    print(userChoice())
#-------------------------------------------------------------------Chapter 12--
if __name__ == '__main__':
   from sys import setrecursionlimit; setrecursionlimit(100)
   from time import clock; START_TIME = clock(); main(); print('~-'*16)
   print('PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')
#  import winsound; winsound.Beep(1500,500) # Frequency, milliseconds
################################<END OF PROGRAM>################################
