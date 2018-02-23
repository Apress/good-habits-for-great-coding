"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 15             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 15 of
      "Good Habits for Writing Code."
"""
"""+==================+========-========*========-========+==================+
   ||                        The Multiplying Program                        ||
   ||                    by M. Stueben (November 27, 2017)                  ||
   ||                                                                       ||
   ||   Description: See printDirections().                                 ||
   ||   Language:    Python Ver. 3.4.                                       ||
   ||   Graphics:    None                                                   ||
   ||   References:  Cem Kaner, Jack Falk, Hung Quoc Nguyen, Testing        ||
   ||                Computer Software, 2nd Ed. (John Wiley, 1999),         ||
   ||                pages 1-7.                                             ||
   +==================+========-========*========-========+==================+
"""
###############################<START OF PROGRAM>###############################

def printDirections():
    print('+----------------------------------------------------------+')
    print('|             == THE MULTIPLICATION PROGRAM ==             |')
    print('|           by M. Stueben (Ver. 1.0, August 2017)          |')
    print('|DIRECTIONS:                                               |')
    print('|  1. Enter a first number, followed by an asterisk (*),   |')
    print('|     followed by a second number. Examples:               |')
    print('|     5280 * 3.14, (-27 + 6) * (1/3), sqrt(100) * log(10). |')
    print('|  2. Push enter to see the output.                        |')
    print('|OPTIONS:                                                  |')
    print('|  3. Enter X to exit the program.                         |')
    print('|  4. Enter P to change the precision (default = 2) of any |')
    print('|     float output.                                        |')
    print("|  5. To enter, say 21 in base 19, type int('21',19).      |")
    print('|     Special case: 0X12 and 0x12 both are 18 in base 10.  |')
    print('|  6. The user will be requested to re-enter any bad input.|')
    print('+----------------------------------------------------------+')
    print('\n RESULTS:')
#------------------------------------------------------The multiplying program--

def requestPrecisionFromUser():
    msg ='Choose the decimal precision of your answer (from 0 to 17):'
    while True:
        data = input (msg)
        ch = data.strip()
        if ch in {'X', 'x'}:
           print (' Goodbye.')
           return
        try:
           precision = int(data)
           if (precision < 0)or(precision> 17)or(type(precision) != int):
              raise Error
        except:
           msg = 'Bad input. Choose a non-negative integer (0 to 17).'
           continue
        return precision
#------------------------------------------------------The multiplying program--

def requestAndMultiplyTwoNumbers():
#---Initialize.
    from math import sqrt, log, log10
    precision      = 2
    problemCounter = 0
    errorMsg       = ''

    while True:
        msg = errorMsg \
              + 'Enter expression * expression, P (precision), or X (exit).'
        data = input(msg) # Dialog box

#-------Check for 'X or x'.
        ch = data.strip()
        if ch in {'X', 'x'}:
            print (' Goodbye.')
            return

#-------Check for 'P or p.
        if ch in {'P', 'p'}:
            precision = requestPrecisionFromUser()
            errorMsg = ''
            continue

#-------Attempt to calculate an answer.
        try:
            answer = eval(data)
            if not isinstance(answer,(int, float)): raise exception
            errorMsg = ''
        except:
            errorMsg = '============== BAD INPUT ==============\n'\
                     + 'You entered -->   ' + data +'.\n'
            continue

#-------Print the answer.
#       Sample output: "1. 1.23 * 4.56 = 5.61 [decimal precision = 2.]"
        problemCounter += 1
        if type(answer) == float:
           print('    ', str(problemCounter) + '. ', data, ' = ' , \
                 round(answer, precision), \
                 ' [decimal precision = ', precision, '.]', sep ='')
        else:
           print('   ', str(problemCounter) + '.', data, '=', answer)
#=====================================<MAIN>====================================

def main():
    printDirections()
    requestAndMultiplyTwoNumbers()
#=====================<GLOBAL CONSTANTS and GLOBAL IMPORTS>=====================
if __name__ == '__main__':
     from time import clock; START_TIME = clock(); main(); print('- '*12);
     print('RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.');
################################<END OF PROGRAM>################################
