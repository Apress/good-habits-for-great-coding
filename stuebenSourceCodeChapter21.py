"""    +-------------------------------=-------------------------------+
       |                 STUEBEN'S SOURCE CODE: CHAPTER 21             |
       |                               by                              |
       |                  M. Stueben (November 27, 2017)               |
       +-------------------------------=-------------------------------+

NOTE: The following programs and functions are from Chapter 21 of
      "Good Habits for Writing Code."
"""
###############################<START OF PROGRAM>###############################
"""+===================-========-========-========-========-===================+
   ||               DYNAMIC PROGRAMMING (shortest route problem)              ||
   ||                    by M. Stueben (October 8, 2017)                      ||
   ||                                                                         ||
   || Description: This program contains three functions (fa, fb, and fc)     ||
   ||              which each determine the next node to move to in proceeding||
   ||              by the shortest path to goal node 9. Then each of these    ||
   ||              functions is used to find the shortest route and its       ||
   ||              distance from node 1 to node 9.                            ||
   ||                                                                         ||
   || Reference:   Eric V. Denardo, Dynamic Programming (Dover, 2003),        ||
   ||              pages 6-19.                                                ||
   || Language:    Python Ver. 3.4                                            ||
   || Graphics:    None                                                       ||
   +===================-========-========-========-========-===================+
"""
#############################<BEGINING OF PROGRAM>##############################
#=====================<GLOBAL CONSTANTS and GLOBAL IMPORTS>=====================
graph = {1:[(1,2),  (2,3)],  # Each neighbor node moves us towards goal node 9.
         2:[(12,5), (6,4)],  # (d,n) = (distance to next node, next node)
         3:[(3,4), (4,6)],
         4:[(4,5), (15,7),(7,8),(3,6)],
         5:[(7,7)],
         6:[(7,8), (15,9)],
         7:[(3,9)],
         8:[(10,9)],
         9:[(0,0)], }
count = 0                    # Counts the number of recursive calls.

# DATA SET 4
w = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,]
v = [12, 2,11, 1, 9,10, 4,15, 6, 7, 8,14, 3, 5, 9,]
C = 25           # Answer: max value = 59 weights = [8, 6, 5, 3, 2, 1]

#-------------------------------------------------------------------Chapter 21--

def printResults(distance, path, func):
    print('--', func.__name__ ,'min path:', path)
    print('   distance =', distance, 'recursive calls =', count)
#-------------------------------------------------------------------Chapter 21--

def fb(node):                # Recursion with NO memoization.
    global count; count  += 1
    if node == 9: return 0
    shortest =  min([dist + fb(neighbor) for (dist, neighbor) in graph[node]])
    return shortest          # = shortest distance from current node to goal node.
#-------------------------------------------------------------------Chapter 21--

def fc(node, dict = {}):     # Recursion with memoization.
    global count; count += 1;
    if node == 9: return 0
    data = []                # data = [(dist to goal, neighbor),...]

    for (dist, neighbor) in graph[node]:
        if neighbor in dict:
            data.append((dist + dict[neighbor], neighbor))
        else:
            neighborsDistToGoal = fc(neighbor, dict)
            data.append((dist + neighborsDistToGoal, neighbor))
            dict[neighbor] = neighborsDistToGoal

    shortest = min(data)[0]
    return shortest # = shortest distance from current node to the goal node.
#-------------------------------------------------------------------Chapter 21--

def fa (node):
    data = ['-',0,0,0,0,0,0,0,0,0,] # = distances of each node to goal node (9).
    for n in range (8, 0, -1):
        data[n] = min([dist + data[neighbor] for (dist, neighbor) in graph[n]])
    return data[node]
#-------------------------------------------------------------------Chapter 21--

def determineMinimumPathAndDistance(func, node):
    global count; count = 0
    minimumPath         = [node]
    shortestDistance    = 0

    while node != 9:
        (_, dist, node)  = min([(dist + func(neighbor), dist, neighbor)
                               for (dist, neighbor) in graph[node]])
        minimumPath.append(node)
        shortestDistance += dist
    return shortestDistance, minimumPath
#-------------------------------------------------------------------Chapter 21--

def memoize(function):
    from sys  import setrecursionlimit; setrecursionlimit(100) # default = 1000
    dict = {}
    def wrapper(num):
       if num not in dict:
          dict[num] = function(num)
       return dict[num]
    wrapper.__name__ = function.__name__ # In case we need the function's name.
    return wrapper
#-------------------------------------------------------------------Chapter 21--

@memoize
def fb(node):              # Recursion with NO memoization.
    global count; count  += 1
    if node == 9: return 0
    shortest =  min([dist + fb(neighbor) for (dist, neighbor) in graph[node]])
    return shortest        # = shortest distance from current node to goal node.
#-------------------------------------------------------------------Chapter 21--

#---1. Returns distance only (form a).
def f(n): # ITERATIVE, bottom-up, memoization.
    ff = [0,0,0,0,0,0,0,0,0,0,]
    for i in range(1, n+1):
        ff[i] = min([(ff[j]+d) for (d,j) in graph[i]])
    return ff[n] # = dist. from node n down to node 1.
#--------------------------------------------------------------------------------

#---2. Returns distance only (form b).
def f(n): # RECURSIVE, top-down, no memoization.
    if n == 1: return 0
    return min([ d+f(neighbor) for (d, neighbor) in graph[n] ]) # Bellman equation
#-------------------------------------------------------------------Chapter 21--

#---3. Returns distance only (form c).
def f(n): # RECURSIVE, top-down, memoization.
    dist = []
    for (d, neighbor) in graph[n]:
        if neighbor not in f.dict: f.dict[neighbor] = f(neighbor)
        dist.append( d + f.dict[neighbor] )
    return min(dist)
f.dict = {0:0, 1:0} # A global dictionary makes the code easier to understand.
#-------------------------------------------------------------------Chapter 21--

def knapsackI(w,v,C): # Iterative: returns max value.
#---Special case (impossible).
    if w == []:
        return (0, [])

#---Append zero weights and values to make the top row and left col zeros.
    w = [0]+w
    v = [0]+v

#---Set matrix size.
    rowMax = len(w)
    colMax = C + 1

#---Create empty matrix, filled with zeros. Note: Because of w[0] = 0 and
#   v[0] = 0, the top row and left col are complete as zeros.
    M = [[0 for j in range(colMax)] # j = col index.
            for i in range(rowMax)] # i = row index.

#This is what we have so far:
#                      0  1  2  3  4  5  6  7  8 <--capacities of the knapsack (j)
#                    +--------------------------
#       i = 0th item | 0  0  0  0  0  0  0  0  0
#       i = 1st item | 0  0  0  0  0  0  0  0  0
#  M =  i = 2nd item | 0  0  0  0  0  0  0  0  0
#       i = 3rd item | 0  0  0  0  0  0  0  0  0
#       i = 4th item | 0  0  0  0  0  0  0  0  0

#---Fill the matrix with values from the bottom-up, starting at 1.
    for i in range(1,rowMax):
        for j in range(1,colMax):
            if w[i] > j:              # Case 1: weight exceeds capacity C.
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = max(  M[i-1][j],  v[i]+M[i-1][j-w[i]]  ) # cases 2 & 3


#---Select the answer (lower-right corner) and return it.
    return M[rowMax-1][colMax-1]
#-------------------------------------------------------------------Chapter 21--

def knapsackR(i,j,w,v): # RECURSIVE, NO MEMOIZATION (returns max value only)
#---Special case.
    if w == []:
       return (0)

#---Append zero weights.
    if w[0] != 0 or v[0] != 0:
        w = [0] + w
        v = [0] + v
        i += 1

#---Base cases.
    if i == 0 or j == 0:
        return 0 # base cases

#---Recursive cases.
    if w[i] > j:
        return knapsackR(i-1,j,w,v)
    return max(knapsackR(i-1,j,w,v), v[i] + knapsackR(i-1,j-w[i],w,v))

# The call: print('Maximum value =', knapsackR(len(w)-1, C, w, v))
#-------------------------------------------------------------------Chapter 21--

def knapsackRR(w,v,C): # RECURSIVE, NO MEMOIZATION (returns max value only)
#---Special case.
    if w == []:
       return (0)

#---Append zero weights, if necessary.
    if w[0] != 0 or v[0] != 0:
        w = [0] + w
        v = [0] + v
#   ------------------------------------------------------
    def f(i,j): # <-- Helper function. Remember this trick.
#------Base cases.
       if i == 0 or j == 0:
           return 0 # base cases

#------Recursive cases.
       if w[i] > j:
           return f(i-1,j)

       return max(f(i-1,j), v[i] + f(i-1,j-w[i]))
#      ---------------------------------------------------
#---Call the recursive function with lower-left indices of the implicit matrix.
    return(f(len(w)-1,C))
# The call: print('Maximum value =', knapsackRR(w,v,C)
#-------------------------------------------------------------------Chapter 21--

def knapsackII(w,v,C): # Iterative: returns both max value and list of weights.
#---Special case:
    if w == []:
        return (0, [])

#---Append zero weights and values, then when the "empty" matrix is created,
#          the top row and left column are correct as zeros.
    w = [0]+w
    v = [0]+v

#---Set matrix size.
    rowMax = len(w)
    colMax = C + 1

#---Create empty matrix with top row and left col correct as zeros.
    M = [[0 for j in range(colMax)] # j = col index.
            for i in range(rowMax)] # i = row index.

#---Fill the matrix with values from the bottom-up.
    for i in range(rowMax):
        for j in range(colMax):
            if w[i] > j:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = max(  M[i-1][j],  v[i]+M[i-1][j-w[i]]  )
    maxValue = M[rowMax-1][colMax-1]

#---Backtrack through matrix to find weights to give the maxValue. Without the
#   w[0] = 0 (and v[0] = 0), this code would ignore the first weight. The
#   final value if i-1 (= -1) in M[i-1][j] would refer to the last row of M,
#   instead of the first row.

    i = rowMax-1
    j = colMax-1                      # i,j is the lower-right corner of M.
    bestWeights = w[1:]               # Ignore the 0th weight element.
    wPtr = len(bestWeights)-1         # wPtr is a pointer to the weight
                                      #   currently under consideration.

    for n in range(len(bestWeights)):
        if M[i-1][j] < M[i][j]:
           j -= bestWeights[wPtr]     # Keep this weight.
        else:
           bestWeights.pop(wPtr)      # Remove a weight from bestWeights list.
        wPtr -= 1
        i    -= 1
    return maxValue, bestWeights
#-------------------------------------------------------------------Chapter 21--

def knapsackRR(w,v,C): # Recursive: returns both max value and list of weights.
                       # Uses a dictionary (dict) for memoization.

#---This function recursively finds the max value while building a dictionary.
    def f(i,j, dict): # <-- Helper function
        if i == 0 or j == 0:
           return 0 # Base cases
        if w[i] > j:
            if (i,j) not in dict:
               dict[i,j] = f(i-1,j, dict)
            return dict[i,j]

        if (i-1,j) not in dict:
           dict[i-1,j] = f(i-1,j, dict)
        a = dict[i-1,j]

        if (i-1,j-w[i]) not in dict:
           dict[i-1,j-w[i]] = f(i-1,j-w[i], dict)
        b = v[i] + dict[i-1,j-w[i]]

        dict[i,j] = max(a,b)
        return dict[i,j]
#    ---------------------<End of helper function>--------------------------

#---Special case:
    if w == []:
        return (0, [])

#---Having w[0] = 0 and v[0] = 0 simplifies the code.
    if w[0] != 0 or v[0] != 0:
        w = [0] + w
        v = [0] + v

#---Make (i,j) the lower right-hand corner of table.
    i = len(w)-1
    j = C

#---Set up dictionary base cases (top row and left column).
    dict = {}
    for ii in range(i+1):
        dict[(ii,0)] = 0 # <-- Necessary (Omitting this was my 3-day mistake.)
    for jj in range(j+1):
        dict[(0,jj)] = 0 # <-- Necessary (Omitting this was my 3-day mistake.)

#---Find max value.
    maxValue = f(i,j, dict)

#---Backtrack through dictionary to find best weights.
    bestWeights = w[1:]                 # Ignore the 0th weight.
    wPtr = len(bestWeights)-1           # = weight pointer
    for n in range(len(bestWeights)):
        if (dict[(i-1, j)] < dict[(i,j)]):
           j -= bestWeights[wPtr]
        else:
           bestWeights.pop(wPtr)   # Remove a weight from bestWeights.
        wPtr -= 1
        i    -= 1
    return maxValue, bestWeights
#-------------------------------------------------------------------Chapter 21--

def runKnapsackTests(runs = 10):
    print('Wait. Now running tests.')
    from random import randint, random
    for n in range(runs):
        if n % 100 == 0: print('.', end = '') # crude animation for time.
        arrayLength = randint( 0, 30)
        sm          = randint( 1, 20)   # sm = smallest possible value in array.
        lg          = randint(20, 40)   # lg = largest  possible value in array.
        w           = list({randint(sm,lg) for j in range(arrayLength)})
        C           = int(random() * sum(w))
        v           = [randint(1,40) for j in range(len(w))]
        ans1 = knapsackII(w,v,C)
        ans2 = knapsackRR(w,v,C)
        if ans1 != ans2:
           print('\n==FAILED!: w =', w, 'v =', v, 'C =', C )
           print('Iterative results =', ans1)
           print('Recursive results =', ans2)
           return
    print('\nPassed', runs, 'tests.')
#-------------------------------------------------------------------Chapter 21--

def noise():
    import winsound
    winsound.Beep(1500,500) # Frequency, milliseconds
    winsound.MessageBeep()
    soundfile =  'c:/windows/media/chimes.wav'
    soundfile =  'c:/windows/media/tada.wav'
    soundfile =  'c:/windows/media/Alarm10.wav' # 01 to 10
    soundfile =  'c:/windows/media/Ring01.wav'  # 01 to 10
    winsound.PlaySound(soundfile, winsound.SND_FILENAME)
#-------------------------------------------------------------------Chapter 21--

def f(n): # recursive only
#---base case
    if n == 1:
       return 1

#---recursive cases (n >= 2).
    total = 0
    for k in range(1, n):
        total += f(k)*f(n-k)
    return total
#-------------------------------------------------------------------Chapter 21--

def f(n, ff = [0, 1]): # recursive with memoization
#---base case
    if n == 1:
       return 1

#---recursive cases (n >= 2).
    total = 0
    for k in range(1, n):
        if n-k >= len(ff):
            ff.append(f(n-k))
        total += ff[k]*ff[n-k]
    return total
#-------------------------------------------------------------------Chapter 21--

def f(n): # iterative
    ff = [0, 1]
    for i in range(2, n+1):
        total = 0
        for k in range(1, i):
           total += ff[k]*ff[i-k]
        ff.append(total)
    return ff[n]
#-------------------------------------------------------------------Chapter 21--

def f(M): # Recursive chain matrix multiplication with NO MEMOIZATION
#    Example:
#    M = [(0, 'A',4,3), (0, 'B',3,2,),  (0, 'C',2,5,), (0, 'D',5,3,)]
#         (0 = value (multiplications), 'A' = expression, 4 = rows, 3 = cols)
#    answer = 'expr = (AB)(CD) value = 78'

    n = len(M)      # = 4 in the example above.
    if n == 1:      # A trivial, but necessary, base case.
        return M[0] # M[0] = (0, 'A',4,3) in the example above.

    if n == 2:  # This base case combines two previously computed expressions.
                # Almost all of the function’s work is done here, because the
                # magic line (for n > 2) repeatedly calls this base case.
       value = M[0][0]+M[1][0]+M[0][2]*M[0][3]*M[1][3]
       key = '(' + M[0][1] + M[1][1] + ')' # Insert parentheses = (AB) in ex. above.
       rows = M[0][2]
       col  = M[1][3]
       return (value, key, rows, col)

    if n > 2:  # Recursive case.
        best = []
        for k in range(1,n):
             best.append(  f([ f(M[:k]), f(M[k:]) ])  ) # The magic line.
    return min(best) # min evaluates on the first component of each tuple.
#-------------------------------------------------------------------Chapter 21--

def f(M, dict = {}): # Recursive chain matrix multiplication with memoization.
    n = len(M)
    if n == 1:
        return M[0]
    if n == 2:
       key = '('+ M[0][1]+'x'+M[1][1]+')'
       if key not in dict:
           result = M[0][0]+M[1][0]+M[0][2]*M[0][3]*M[1][3], \
                   '('+M[0][1]+'x'+M[1][1]+')',   M[0][2],   M[1][3],
           dict[key] = result
       return (dict[key])
    if n > 2:
        best = []
        for k in range(1,n):
             best.append(  f([ f(M[:k], dict), f(M[k:], dict) ], dict) )
    return min(best)
#-------------------------------------------------------------------Chapter 21--

def f(matrices): # Iterative using memoization
#---Check data format.
    for m in matrices:
        assert len(m) == 4 #  example: m = (0, 'A', 4, 3)
        assert m[0]   == 0
        assert 65 <= ord(m[1]) <= 90
        assert type(m[2]) == type(m[3]) == int
    for n in range(len(matrices)-1):
        assert matrices[n][3] == matrices[n+1][2]

#---Calculate the number of matrices
    limit = len(matrices)

#   HELPER FUNCTION
    def insertInDict (A,B,dict):
       # Example: if A = (0, 'A', 4, 3) and B = (0, 'B', 3, 2), then
       # key = 'AB' and result = (24, '(AB)', 4, 2)
       key        = A[1]+B[1]
       value      = A[0]+B[0]+A[2]*A[3]*B[3]
       expression = '('+A[1]+B[1]+')'
       result     = value, expression, A[2], B[3]
       dict[key]  = result

#   HELPER FUNCTION
    def dictKey(Lst):
        # Example: Lst =[(0, 'B', 3, 2), (0, 'C', 2, 5)] returns key = 'BC'.
        key = ''
        for x in Lst:
            key += ''.join(x[1])
        return key

#   HELPER FUNCTION
    def mult (key1, key2, dict):
        # This function multiplies two matrix expressions (denoted by their
        # keys) and puts the result in the dictionary with a new key.
        newKey = key1 + key2
        A = dict[key1]
        B = dict[key2]
        value  = A[0]+B[0]+A[2]*A[3]*B[3]
        expression = '('+A[1]+B[1]+')'
        # Below, we tack on the newKey with the result and return both.
        result = value, expression, A[2], B[3], newKey
        return result

#---Create empty dictionary.
    dict = {}

#---Insert singles into dictionary--e.g., (0, 'A', 4, 3) with a key of 'A'
    for n in range(0,limit):
           key = matrices[n][1]
           dict[key] = matrices[n]

#---insert the rest (doubles, triples, quads, etc.) into dictionary.
#   This is a complicated function/algorithm with FOUR loops.
    for i in range(2,limit+1):       # i = len(Lst)
        for j in range(0,limit-i+1): # Lst below starts at position j.
               Lst = [matrices[j+n] for n in range(0, i)]
#              Example: Lst = [(0, 'A', 4, 3), (0, 'B', 3, 2), (0, 'C', 2, 5)]
               candidates = []
             # Strategy: Split any Lst into two consecutive parts. (This can be
             #           done several ways.) Then multiply the two parts and
             #           place the result in the candidates list. Then only the
             #           candidate with the least value goes into the dictionary

               for k in range(1,len(Lst)):
                   key1 = dictKey(Lst[:k]) # = left  part of Lst.
                   key2 = dictKey(Lst[k:]) # = right part of Lst.
                   candidates.append(mult(key1, key2, dict))
               best = min(candidates)
               dict[best[4]] = best[:-1] # The key is at the end (index 4).
    printDictionary(dict)

#---Return dictionary value with key equal to all matrix letters.
    finalKey = ''
    for tuple in matrices:
        finalKey += tuple[1]
    return dict[finalKey]
#=====================================<MAIN>====================================

def main():
    for func in (fb, fc, fa):
        distance, path = determineMinimumPathAndDistance(func, node=1)
        printResults(distance, path, func)

    print('knapsackI  maximum value =', knapsackI(w,v,C))
    print('knapsackR  maximum value =', knapsackR(len(w)-1, C, w, v))
    print('knapsackRR maximum value =', knapsackRR(w,v,C))
    print('knapsackII maximum value =', knapsackII(w,v,C))
    runKnapsackTests(runs = 10)
    noise()
    print(f(6))
#-------------------------------------------------------------------Chapter 21--
if __name__ == '__main__':
   from time import clock; START_TIME = clock();
   main(); print('- '*16);
   print('Program run time:%6.2f'%(clock()-START_TIME), 'seconds.')
#################################<END OF PROGRAM>###############################
