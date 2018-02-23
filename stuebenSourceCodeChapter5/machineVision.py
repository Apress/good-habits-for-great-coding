"""+---------------------------------------------------------------------------+
   |                 MACHINE (COMPUTER) VISION  Ver. 5.1                       |
   |             GAUSSING SMOOTHING AND THE CANNY TRANSFORM                    |
   |                  by M. Stueben (February 13, 2013)                        |
   |                                                                           |
   |                                                                           |
   | REFERENCES:                                                               |
   |    1. E.R. Davies, Machine Vision, 3rd. Ed. (Elsevier (Morgan Kaufmann,   |
   |       2005)), Chapter 5.                                                  |
   |    2. Lawrence O'Gorman, Michael J. Sammon, and Michael Seul, Practical   |
   |       Algorithms for                                                      |
   |       Image Analysis, 2nd Ed., (Cambridge, 2008).                         |
   |    3. Algorithms for Image Processing and Computer Vision, 2nd Ed.        |
   |       (Wiley, 2011).                                                      |
   |    4. Wikipedia, Sobel operator, Canny edge detector, Edge detection.     |
   +---------------------------------------------------------------------------+

   Machine Vision sounds more like an engineering problem than an AI problem.
   And there is much engineering in Machine Vision (lenses, binocular vision,
   wiring, synchronized motors, etc). Nevertheless, the computer must be able to
   recognize in some meaningful sense what it sees. That is where AI programming
   comes in. Our goal in this assignment is to download a complicated real-
   life image, and have the computer detect its edges.

      Why edge-detection? When someone with poor vision takes off his or her
   glasses, they say "Everything is blurry. I can't see anything." When we look
   at printing or cursive script, we are looking at edges. Edge detection is the
   first step in seeing visually.


STEP 1. (DOWNLOAD, SAVE, AND PRINT A PPM IMAGE FILE IN BOTH COLOR AND GREY-
   SCALE). Below, there are explicit directions on how to do this. If you open a
   PPM file of type P3 in a text editor you will see something like the
   following.

       P3
       # lena.ppm
       512 512
       255
       225 137 125 225 137 127 224 137 128 224 135 127 226 136 125 223 131
       118 229 137 126 225 135 124 229 141 127 225 137 125 226 136 127 226
       134 123 218 129 113 227 139 119 224 135 119 218 129 111 221 132 114
       219 132 112 223 138 118 223 138 117 220 129 108 223 131 108 221 129
      ...

  [Note well: these numbers like 225, 137, etc, come out of a Python file as
  strings: '225, '137'.]

      The P3 denotes both color and ASCII--i.e., text, not unreadable binary,
   and is the type of file REQUIRED for this program. The second line is a
   comment for the reader of the image file. It is usually the name of the file.
   The next two numbers are the rectangular width and the height of the file in
   pixels (picture elements). The final number is the maximum brightness value.

      In some PPM files the initial file information (the first four lines
   above) is placed all in one or two lines. Consequently, you MUST open a PPM
   file in a text editor and visually inspect how it is set up in order to know
   how to read past the initial information and begin reading the actual pixel
   information.

      Why are we working with a PPM image file format? There are several
   different formats for saving image data in files. A RASTER (aka non-scalable)
   graphics image or graphics file (aka bitmap *.BMP image or bitmap file) is a
   data structure representing a rectangular grid of pixels. The pixel infor-
   mation can represent a black-and-white, gray-scale, or colors. Because the
   pixel information takes up so much space, compression algorithms are usually
   necessary to store graphics files. JPEG (Joint Photographic Experts Group,
   used in most digital cameras) and GIF (Graphical Interchange format, used in
   web graphics and animations) are two common compression algorithms. By the
   way, PPM stands for Portable Pixel forMat.

      The other kind of graphics image file is the VECTOR type. This is a
   connect-the-dots type of file, where lines are represented by vectors. The
   images are represented by mathematics, not individual pixels. Thus, a vector
   image can scale (like a font in a word processor), but a raster image cannot
   scale. Vector graphics are ideal for rendering images that can be naturally
   described with mathematical curves and lines. But most real-life images must
   use raster formats.

      The P3 PPM image file format is an UNCOMPRESSED file format, and is easy
   to work with, which is why we are using it. THE PPM format comes in six
   types: P1, P2, P3, P4, P5, P6. The first three, P1, P2, and P3, are ASCII
   text. The other three P4, P5, and P6 are unreadable binary. P3 and P6 are
   color formats. P2 and P5 are grey-scale formats. And P1 and P4 are for black-
   and-white (no grays). Note that the term "black-and-white" is sometimes used
   to mean gray-scale, and consequently is context dependent.

       In a P3 type file, starting with the pixel information, every three
   numbers represent a red-green-blue color mixture for a particular pixel. Also
   note that THE NUMBERS IN PYTHON FILES ARE READ IN AS STRINGS separated by
   spaces--e.g., '225' '137' '125', not 225 137 125. To runb this program you
   need a PPM file on your computer. I use one (included with this source code)
   called lena_rgb_p3.ppm, a famous 1972 picture of the model Lenna. See
   "Lenna" in Wikipedia.

   WARNING TO WINDOWS USERS. If you use a backslash in a file name, it must be a
   double backslash. Why? Because in Python the backslash indicates the
   beginning of an escape sequence--e.g., '\n' = newline, '\t' = tab, etc. To
   compound the trap, the single backslash will work fine only if the letter
   following it is not one of the allowed escape code letters. Play safe in
   Windows, ALWAYS use a double backslash in Python file references.

      Once we have read through the first four lines of our PPM file (use the
   Python readline, not read), we read the entire rest of the file (use read,
   not readline) into one super-long string type called nums.
   Read your file like this:
                                nums = file1.read().split()
                                file1.close()

      We need to extract the numbers from the num string and stuff them into a
   HUGE list called image, and combine every three consecutive integer into one
   number. The formula for combining is given below. The formula is based on
   human biological sensitivity to light--e.g., we are more sensitive to green
   than to red and blue. Here is some of my code using the huge list (nums):

def extractTheImageGrayScaleNumbersFromFile(GRAY_SCALE_NUMBERS_FILE_NAME = \
    'f:\\grayScale.ppm'):
    file1    = open(GRAY_SCALE_NUMBERS_FILE_NAME, 'r')
    nums = file1.read().split()
    file1.close()
    image = []
    for elt in nums:
        image.append( int(elt) )
    printElapsedTime ('Extracted gray-scale nums from file')
    return image

       The numbers must first be changed into strings separated by spaces when
    inserted into their own file. This is data the computer will later analyze.
    Here is the code I used:

            file1 = open ('grayscale.ppm', 'w')
            for elt in image:
                file1.write (str(elt) + ' ')
            file1.close()

       Open the grayscale file and read the first ten numbers back to the
    console window as integers. This confirms our success so far. But what we
    really want to see is the (now gray-scale) image.

       Print the file to the screen so that we can ACTUALLY VIEW THE IMAGE.
    Here is the magic code, which needs to be a class type. The call to the
    class follows the code (Below, x is a dummy variable--e.g., the syntax
    requires that some variable must be there to compile, but the variable is
    never actually used).

      A NOTE ON MAGIC CODE: It is a mistake to insist on understanding every
    tool you use. Thus, you will sometimes use theorems that you can't prove, or
    functions that you do not understand. To take the time and effort to under-
    stand all of our basic tools will leave most of us with too little time to
    apply them to the problems we need to solve--with the use of these tools.
    Occasionally, we come to suspect one of our tools is not doing precisely
    what we thought it did. That is one of the rare times we must stop to
    understand the tool.

====================================================================================================
class ImageFrame:
    def __init__(self, image):
        self.img = PhotoImage(width = WIDTH, height = HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num = image[row*WIDTH + col]
                if COLORFLAG == True:
                   kolor ='#%02x%02x%02x' % (num[0], num[1], num[2]) # = color
                else:
                   kolor ='#%02x%02x%02x' % (num, num, num)          # = gray-scale
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElapsedTime ('displayed image')
       -------------------------------------------------------------------------

def printElapsedTime (msg = 'time'):
    length = 30
    msg = msg [:length]
    tab = '.'*(length-len(msg)) # <-- msg length truncated at 30 chars
    print('--' + msg.upper() + tab + ' ', end = '')
    time = round(clock() - START, 1) # START is global constant.
    print( '%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
           ' sec', sep = '')
       -------------------------------------------------------------------------

 def main()
     ...
     x  = ImageFrame(listOfImageNumbers)
     ... # To run only the first few lines, comment out all but the final line.
         # Don't use exit().
    root.mainloop()
================================================================================

      Our ultimate goal is a computer program to detect and outline the edges in
   our graphics image. This is the beginning of a crude machine vision. You are
   now ready to do some smoothing on the integers in your gray-scale file. Why
   smooth? Smoothing is a way to eliminate fly specks.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

ASSIGNMENT 2 (SMOOTHING WITH THE GAUSSIAN MASK). We want to open the file, read
   it in as a list (called image) of integers (not strings), and print, say the
   first ten integers, to the screen. This will confirm that we have the correct
   data. We will then modify the gray-scale numbers (smooth the image), save
   those numbers in a new list (called image2), and reprint the smoothed image.
   What helped me in this program is to smooth the image four times, not just
   once, before I finally saved the numbers back into a file.

                                    -==THE GAUSSIAN BLUR==-
    part of our image grid centered
          on the number 229                    the 3x3 Gaussian smoothing mask
        +-----+-----+-----+---                        +-----+-----+-----+
        | 225 | 137 | 125 |                           |  1  |  2  |  1  |
        +-----+-----+-----+---                   1    +-----+-----+-----+
        | 118 | 229 | 137 |                     --- * |  2  |  4  |  2  |
        +-----+-----+-----+---                   16   +-----+-----+-----+
        | 134 | 123 | 218 |                           |  1  |  2  |  1  |
        +-----+-----+-----+---                        +-----+-----+-----+
        |     |     |     |

       We use the mask to revise the old number 229, and place it into a new
    grid. We do this for every number (except for the numbers associated with
    the four edges in the original image) in the old grid (the list called
    image) to produce a new revised grid (the list called image2). Again, every
    new number we place in the new grid is calculated by placing the same 3x3
    smoothing mask over the number in the corresponding place in the old grid,
    adding up corresponding multiples, and dividing by 16 (the sum of the
    numbers in the mask). In our example, the numbers 225, 137, 125, 118, and
    134 are the same in both grids, because these numbers are on the edge of the
    old grid. However, in the position occupied by 229 in the old grid, we find
    this number in the new grid:
               1/16 x [(1x225 + 2x137 + 1x125) +
                       (2x118 + 4x229 + 2x137) +
                       (1x134 + 2x123 + 1x218)] = 165.5 rounded to 166.

      Below, notice how we change a pixel position Mat[row][col] into a list
    position and vice versa:

                     pixel(row, col)  -->  image[row*WIDTH + col]

                                          and

                     image[index]     -->  pixel (index//WIDTH, index%WIDTH)


      The global constant WIDTH is the horizontal size of the file in pixels.
    HEIGHT is the vertical size of the file in pixels. Remember that these two
    numbers are in the first few lines of the file.

    image2 = [0] * WIDTH * HEIGHT
    for row in range (1, HEIGHT-1):
        for col in range (1, WIDTH-1):
            image2 [row*WIDTH + col] = ...

      Note Well: You do NOT want to modify the old grid (image). Instead, you
    want to create a new grid (image2), and then rename it as image. Also
    round() is built-in to the main module and does not need to be imported.

      We SAVE the smoothed (or repeatedly smoothed) grid numbers to a file.
    Thus, in the next section, we start with the smoothed numbers, and do not
    have to recreate them. This makes the program MUCH FASTER.
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

ASSIGNMENT 3 (SOBEL MASKS). This time we are accessing the smoothed gray-scale
   file we wrote last time. We can consider the gray-scale numbers to be an
   intensity grid. Imagine that each number represents the height of a building
   in a city of skyscrapers. We calculate the difference in heights x) for every
   two buildings that are adjacent and in a west-east line. Then we calculate
   the difference in heights (y) for every two building that are adjacent and in
   a north-south line (y). We could call these two numbers (analogous to partial
   derivatives) the two-dimensional GRADIENT VECTOR of each building. Then we
   can combine the two numbers into a MAGNITUDE sqrt(x*x+y*y). This magnitude is
   sometimes approximated to |x| + |y|, which is faster to compute than
   sqrt(x*x + y*y). But we will use the actual magnitude in this program. If we
   followed the descriptions in this paragraph, we would use the following two
   masks.

            +-----+-----+-----+                             +-----+-----+-----+
            |  0  |  1  |  0  |                             |  0  |  0  |  0  |
            +-----+-----+-----+                             +-----+-----+-----+
       My = |  0  | -1  |  0  |                        Mx = |  0  | -1  |  1  |
            +-----+-----+-----+                             +-----+-----+-----+
            |  0  |  0  |  0  |                             |  0  |  0  |  0  |
            +-----+-----+-----+                             +-----+-----+-----+

      But in fact, other masks seem to produce better effects. The following are
   the two famous Sobel (edge-detecting) templates, that are used in this
   program.

            +-----+-----+-----+                             +-----+-----+-----+
            |  1  |  2  |  1  |                             | -1  |  0  |  1  |
            +-----+-----+-----+                             +-----+-----+-----+
       Sy = |  0  |  0  |  0  |                        Sx = | -2  |  0  |  2  |
            +-----+-----+-----+                             +-----+-----+-----+
            | -1  | -2  | -1  |                             | -1  |  0  |  1  |
            +-----+-----+-----+                             +-----+-----+-----+

      The new center number Gy is derived from placing the Sy mask over the
   image grid and doing the multiplying and adding to produce Gy. BTW G stands
   for gradient, a ratio, a pure number with no units. Gx is derived analagously.

                        from math import sqrt
                        M =  sqrt(Gx*Gx + Gy*Gy) # = vector MAGNITUDE.
                        D =  theta(Gx, Gy)       # = vector DIRECTION.

      Note: theta(Gx, Gy) indicates the APPROXIMATE angle of the line (not ray)
   by an integer: 0, 1, 2, and 3, where 0 = horizontal line, 1 = 45 degree line,
   2 = 90 degree line, and 3 = 135 degree line. What about 180 degrees? That is
   considered horizontal (0). Negative 90 degrees is also 90 degrees, etc.
   Whenever you need an arctangent function, you almost always need atan2(y,x)
   NOT atan(y/x). Important: The y number comes before the x number, and don't
   forget the import line: from math import atan2.

      Keep in mind this data set of magnitudes is no longer an image (gray-
   scale numbers). Some of the magnitude numbers are larger than the maximum
   allowed intensity (255 in this assignment). We need to use these numbers for
   the next of the program. Nevertheless, I wanted to see the weird picture
   anyway. So I wrote and ran this code which normalizes the magnitude numbers
   to a range of 0 to 255:

            def normalize(image, intensity = 255):
                m = max(image)
                printElapsedTime ('normalizing')
                return [int(x*intensity/m) for x in image]
            #---------------------------------------------
            def main():
                ...
            #---Print Sobel normalized magnitudes
                mags = normalize([x[0] for x in image])
                x = ImageFrame(mags)
                ...

  SUGGESTED DATA TYPE: The original image variable was a simple list that
  contained only integers (gray-scale values). Now the image variable is a list
  of lists. Each sub-list has five integers:

   The image array: [ [?,?,?,?,?], [?,?,?,?,?], ... ]
                       0 1 2 3 4    0 1 2 3 4

    0) Sobel magnitude
    1) Sobel angle approximation, theta = 0, 1, 2, or 3.
    2) 1 = "structural edge";  0 = "NOT a structural edge."
    3) 1 = "been here before"; 0 = "NOT been here before." (for recursion)
    4) 1 = "to be printed";    0 = "NOT to be printed."
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

PART 4 (CANNY TRANSFORM). The Canny method of edge detection requires four
   steps: STEP 1 is an initial smoothing process of an image (we already did
   this). STEP 2 is a transformation (Sobel here) to obtain MAGNITUDES and
   ANGLES (the previous assignment). In STEP 3 we look at every point and the
   two pixels on each side of it in the direction (and opposite direction) of
   its angle approximation (0, 1, 2, and 3). If the center cell is a maximum of
   the three cells (use ">", not ">="), then it is considered a structural edge
   point (as opposed to a boundary edge point, in  which we are not interested).
   See figures below.

            +-----+-----+-----+
            |  ?  |  2  |  2  |   EXAMPLE. Assume direction = 1 (45 deg. or 225
            +-----+-----+-----+   deg.) Therefore, we compare 2 and -1 to the
            |  ?  |  3  |  ?  |   center number, 3. Is it a structural edge
            +-----+-----+-----+   point? Yes, because 3 > 2 and 3 > -1.
            | -1  |  ?  |  ?  |
            +-----+-----+-----+

      You need to mark the pixels that are structural edges. This is the third
   number in our little lists (1 = an edge, 0 = not an edge). We set cell[2] =
   1. We could print the structural edge pixels at this point (all with
   intensity of 255 on a black background, or all of intensity of 0 on a white
   background). But we can do more.

   Step 4), the final step) is called DOUBLE THRESHOLDING. In this step we
   choose two MAGNITUDE (not pixel intensity) thresholds: LOW and HIGH. Set HIGH
   to some value in the magnitudes. Your choice depends on the image. Set LOW
   somewhat lower (experiment). Then examine every cell in the image.

   1) If the cell is NOT a structural edge point (cell[2] = 0), then ignore it
      and continue on.

   2) If the cell is a structural edge point (cell[2] = 1) and cell[0] > HIGH,
      then set cell[4] = 1. This means we will eventually print this point as an
      edge. Note well: at this point, some structural edge points are not marked
      for printing, because their magnitudes are too low.

   3) However, for each cell in step 2 (cell[4] = 1), we need to run a recursive
      routine that looks at its four neighbors (NSEW). If any of these neighbors
      are edge points (cell[2] = 1) and cell[0] > LOW, then cell[4] = 1 and
      cell[3] = 1, and the function recursively calls the neighbors of and
      changed cell. We need to mark cells as previously visited, cell[3] = 1, so
      that we never recurse over the same cell again. This is sometimes
      described as flood fill.  Here is the beginning of my recursive function:

        def fixCellAt(M, row, col): # <-- RECURSION

        #---base case
            if M[(row)*WIDTH + col][3] == 1: return
            M[   (row)*WIDTH + col][3] =  1 # marked as "been here before".

        #---fix above
           if (row > 0  and M[(row-1)*WIDTH + col][2] == 1
                        and M[(row-1)*WIDTH + col][0] > LOW):
              M[(row-1)*WIDTH + col][3] = 1 # marked as "been here before".
              M[(row-1)*WIDTH + col][4] = 1 # marked "to be printed".
              fixCellAt(M, row-1, col)

      Above, the parentheses allow a single instruction to be broken into
      several lines.

      Finally, print out only the pixels that have been determined to be
   structural edge points (cell[4] == 1) and marked to be printed (cell[3] = 1).
   Print these edge points as white on a black background, or vice-versa. The
   program run time is about 14-15 seconds on my laptop (I5 processor).  But if
   the smoothed data is opened first, then the program takes about 6-7 seconds
   to run. Moral save the smoothed data in a file.

      Below is the is my program. I hope ti makes some sense to the reader.
"""
#################################<BEGIN PROGRAM>################################
#==<BEGIN ImageFrame CLASS>======================================MachineVision==
class ImageFrame:
    def __init__(self, image):
        self.img = PhotoImage(width = WIDTH, height = HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num = image[row*WIDTH + col]
                if COLORFLAG == True:
                   kolor ='#%02x%02x%02x' % (num[0], num[1], num[2]) # = color
                else:
                   kolor ='#%02x%02x%02x' % (num, num, num)       # = gray-scale
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElapsedTime ('displayed image')
#==<END OF ImageFrame CLASS>=====================================MachineVision==

def confirmP3fileType(file1):
    stng = file1.readline().strip()#Read 1st line, print it, and then ignore it.
    print('--First line of file reads:', stng)
    if stng[0]+stng[1] != 'P3':
        print('+===================================================+')
        print('| ERROR: This file is NOT of type P3.               |')
        print('|        The first line of the file is shown below. |')
        print('+===================================================+')
        print ('-->', stng)
        file1.close()
        exit()
#----------------------------------------------------------------MachineVision--

def printElapsedTime (msg = 'time'):
    length = 30
    msg = msg [:length]
    tab = '.'*(length-len(msg)) # <-- msg length truncated at 30 chars
    print('--' + msg.upper() + tab + ' ', end = '')
    time = round(clock() - START, 1) # START is global constant.
    print( '%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
           ' sec', sep = '')
#----------------------------------------------------------------MachineVision--

def readFileNumbersIntoString(file1):
    nums = file1.read().split() # = a list of strings, each separated by a space
    file1.close()
    if len(nums)%3 != 0:
        print('---WARNING: Size of file(', len(nums) ,') % 3 != 0')
        exit()
    return nums
#----------------------------------------------------------------MachineVision--

def convertStringRGSsToGrayIntegersOrColorTuples(nums):
    image = []
    if COLORFLAG == True:
       for pos in range(0, len(nums), 3):
           RGB = ( int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]) )
           image.append(RGB) # a tuple of three integers
    else:
       for pos in range(0, len(nums), 3):
           RGB = ( int(nums[pos+0]), int(nums[pos+1]),int(nums[pos+2]) )
          # Below a single gray integer is appended.
           image.append( int (0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]) )
    return image
#----------------------------------------------------------------MachineVision--

def printTitleAndSizeOfImageInPixels(image):
    print('         ==<RUN TIME INFORMATION>==')
    if len(image) != WIDTH * HEIGHT:
        print('--ERROR: Stated file size not equal to number of pixels')
        print ('file length:', len(image))
        print ('width:', WIDTH, 'height:', HEIGHT)
        exit()
    print('--NUMBER OF PIXELS.............. ', len(image))
    printElapsedTime ('image extracted from file')
#----------------------------------------------------------------MachineVision--

def readPixelColorsFromImageFile(IMAGE_FILE_NAME):
    imageFile     = open(IMAGE_FILE_NAME, 'r')
    confirmP3fileType(imageFile)
    nums  = readFileNumbersIntoString(imageFile)

    image = convertStringRGSsToGrayIntegersOrColorTuples(nums)
    printTitleAndSizeOfImageInPixels(image)
    return image
#----------------------------------------------------------------MachineVision--

def smoothImageCellWithNeighborCells(row, col, image):
    return (image[(row-1)*WIDTH + (col-1)]+
          2*image[(row-1)*WIDTH + (col  )]+  image[(row-1)*WIDTH+(col+1)] +
          2*image[(row  )*WIDTH + (col-1)]+
          4*image[(row  )*WIDTH + (col  )]+2*image[(row  )*WIDTH+(col+1)] +
            image[(row+1)*WIDTH + (col-1)]+
          2*image[(row+1)*WIDTH + (col  )]+  image[(row+1)*WIDTH+(col+1)])//16
#----------------------------------------------------------------MachineVision--

def smoothTheImage(image, NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 0):
    count = NUMBER_OF_TIMES_TO_SMOOTH_IMAGE
    if count < 1 or type(count) != int:
        print('--No smoothing (number =', count, ')')
        return image
    print('--Repeat smoothing process', count, 'times.')
    smoothedImage = [0] *(512 * 512)
    for n in range(count):
        for row in range (1, HEIGHT-1):
            for col in range (1, WIDTH-1):
                smoothedImage [row*WIDTH + col] = \
                              smoothImageCellWithNeighborCells(row, col, image)
        image = smoothedImage[:]
        printElapsedTime ('smoothed image '+ str(n))
    return image
#----------------------------------------------------------------MachineVision--
def calculateTheTwoSobelGradients(image, row, col):
     Gy = (image[(row-1)*WIDTH + (col-1)] +
         2*image[(row-1)*WIDTH + (col  )] +   image[(row-1)*WIDTH+ (col+1)] +
         0*image[(row  )*WIDTH + (col-1)] +
         0*image[(row  )*WIDTH + (col  )] + 0*image[(row  )*WIDTH+ (col+1)] -
           image[(row+1)*WIDTH + (col-1)] -
         2*image[(row+1)*WIDTH + (col  )] -   image[(row+1)*WIDTH+ (col+1)])

     Gx = (-1*image[(row-1)*WIDTH + (col-1)] +
            0*image[(row-1)*WIDTH + (col  )] +   image[(row-1)*WIDTH+ (col+1)] -
            2*image[(row  )*WIDTH + (col-1)] +
            0*image[(row  )*WIDTH + (col  )] + 2*image[(row  )*WIDTH+ (col+1)] -
              image[(row+1)*WIDTH + (col-1)] -
            0*image[(row+1)*WIDTH + (col  )] +   image[(row+1)*WIDTH+ (col+1)])
     return Gy, Gx
#----------------------------------------------------------------MachineVision--

def sobelTransformation(image): # pixel[0 = magnitude, and 1 = direction, 0,0,0]
    gradIntensity = []
    for row in range (0, HEIGHT):
        for col in range (0, WIDTH):
            if row == 0 or row == HEIGHT-1 or col == 0 or col == WIDTH-1:
               gradIntensity.append([0,0,0,0,0, 0])
               continue
            Gy, Gx = calculateTheTwoSobelGradients(image, row, col)
            from math import sqrt
            mag    = int(sqrt(Gx*Gx + Gy*Gy))
            angle  = theta1(Gy, Gx)
            angle2 = theta2(Gy, Gx)
            gradIntensity.append([mag, angle, 0, 0, 0, angle2])
    printElapsedTime ('sobel transformation complete')
    return gradIntensity
#----------------------------------------------------------------MachineVision--

def normalize(image, intensity = 255):
    m = max(image)
    printElapsedTime ('normalizing')
    return [int(x*intensity/m) for x in image]
#----------------------------------------------------------------MachineVision--

def theta1(Gy, Gx):
    from math import atan2, pi
    t = atan2(Gy, Gx) + (Gy < 0) * pi       #  t is positive: 0 <= t < 180 deg.
    if  t <= 0.3927 or 2.7489 < t: return 0 #  t is below  22.5 deg or
                                            #  t > (135+22.5) deg.
    if  t <= 1.1781: return 1               #  t is below  45 + 22.5 deg.
    if  t <= 1.9635: return 2               #  t is below  90 + 22.5 deg.
    if  t <= 2.7489: return 3               #  t is below 135 + 22.5 deg.
    exit('ERROR: Bad t value:'+str(t))      #  Error catch
#----------------------------------------------------------------MachineVision--

def theta2(Gy, Gx):
    from math import atan2, pi
    return atan2(Gy, Gx)
#----------------------------------------------------------------MachineVision--

def TwoNeighborsOfCell(image, row, col, cell):
    if cell[1] == 0:
       leftNeighbor  = image[(row  )*WIDTH + (col-1)][0] # left neighbor  is to the left.
       rightNeighbor = image[(row  )*WIDTH + (col+1)][0] # right neighbor is to the right.
    if cell[1] == 1:
       leftNeighbor  = image[(row+1)*WIDTH + (col-1)][0] # left neighbor is up    45 deg.
       rightNeighbor = image[(row-1)*WIDTH + (col+1)][0] # left neighbor is down 225 deg.
    if cell[1] == 2:
       leftNeighbor  = image[(row-1)*WIDTH + (col  )][0] # left neighbor is directly up.
       rightNeighbor = image[(row+1)*WIDTH + (col  )][0] # right neighbor is directly down.
    if cell[1] == 3:
       leftNeighbor  = image[(row-1)*WIDTH + (col-1)][0] # left  neighbor is up  135 deg.
       rightNeighbor = image[(row+1)*WIDTH + (col+1)][0] # right neighbor is down 45 deg.
    return leftNeighbor, rightNeighbor
#----------------------------------------------------------------MachineVision--
def indicationOfStructuralEdgePoint(image, row, col, cell):
    leftNeighbor, rightNeighbor = TwoNeighborsOfCell(image, row, col, cell)
    if cell[0] > leftNeighbor and cell[0] > rightNeighbor:
       return 1
    return 0
#----------------------------------------------------------------MachineVision--

def cannyTransform(image): # pixel[2] = 1 if edge, else  pixel[2] = 0.
    for row in range (1, HEIGHT-1):
        for col in range (1, WIDTH-1):
            cell = image[(row)*WIDTH + (col)]
            cell[2] = indicationOfStructuralEdgePoint(image, row, col, cell)
    printElapsedTime ('canny')
    return image
#----------------------------------------------------------------MachineVision--

def fixCellAt(M, row, col): # <-- RECURSION
#---base case
    if M[(row)*WIDTH + col][3] == 1: return
    M[   (row)*WIDTH + col][3] =  1 # marked as "been here before".

#---fix above
    if (row > 0  and M[(row-1)*WIDTH + col][2] == 1
                 and M[(row-1)*WIDTH + col][0] > LOW):
       M[(row-1)*WIDTH + col][4] = 1 # marked "to be printed".
       fixCellAt(M, row-1, col)

#---fix below
    if (row < HEIGHT-1 and M[(row+1)*WIDTH + col][2] == 1
                       and M[(row+1)*WIDTH + col][0] > LOW):
       M[(row+1)*WIDTH + col][4] = 1 # marked "to be printed".
       fixCellAt(M, row+1, col)

#---fix left
    if (col > 0  and M[(row)*WIDTH + col-1][2] == 1
                 and M[(row)*WIDTH + col-1][0] > LOW):
       M[(row)*WIDTH + col-1][4] = 1 # marked "to be printed".
       fixCellAt(M, row, col-1)

#---fix right
    if (col < WIDTH-1 and M[(row)*WIDTH + col+1][2] == 1
                      and M[(row)*WIDTH + col+1][2] > LOW):
       M[(row)*WIDTH + col+1][4] = 1 # marked "to be printed".
       fixCellAt(M, row, col+1)
#----------------------------------------------------------------MachineVision--

def doubleThresholdImageListsInToGrayScaleValues(imageLists):
    for row in range (0, HEIGHT):
        for col in range (0, WIDTH):
            cell = imageLists[(row)*WIDTH + (col)]
            if cell[2] == 0 or cell[0] < HIGH: # ignore non-edge cells
               continue
            cell[4] = 1 # marked "to be printed".
            fixCellAt(imageLists, row, col)
    printElapsedTime ('doubleThreshold')
    image = [255 if x[4] == 1 else 0 for x in imageLists]
    return image
#----------------------------------------------------------------MachineVision--

def displayImageInWindow(image):
    global x # This line is necessary.
    x = ImageFrame(image)
#----------------------------------------------------------------MachineVision--

def saveTheImageGrayScaleNumbersToFile(image, GRAY_SCALE_NUMBERS_FILE_NAME = \
    'f:\\grayScale.ppm'):
    file1 = open (GRAY_SCALE_NUMBERS_FILE_NAME, 'w')
    for elt in image:
        file1.write (str(elt) + ' ' )
    printElapsedTime ('saved file numbers')
    file1.close()
#----------------------------------------------------------------MachineVision--

def extractTheImageGrayScaleNumbersFromFile(GRAY_SCALE_NUMBERS_FILE_NAME = \
    'f:\\grayScale.ppm'):
    file1    = open(GRAY_SCALE_NUMBERS_FILE_NAME, 'r')
    nums = file1.read().split()
    file1.close()
    image = []
    for elt in nums:
        image.append( int(elt) )
    printElapsedTime ('Extracted gray-scale nums from file')
    return image
#----------------------------------------------------------------MachineVision--
def printNormalizedImageLists(imageLists, Flag):
    if not Flag: return
    sobelMagnitudes = normalize([x[0] for x in imageLists])
    displayImageInWindow(sobelMagnitudes, True)
#----------------------------------------------------------------MachineVision--
def convertColorFileToGrayScaleFile():
    image = list(readPixelColorsFromImageFile (IMAGE_FILE_NAME = 'f:\\lena_rgb_p3.ppm'))
    saveTheImageGrayScaleNumbersToFile (image, GRAY_SCALE_NUMBERS_FILE_NAME = 'f:\\grayScale.ppm')
#----------------------------------------------------------------MachineVision--
def extractSmoothAndSaveImage():
    image = extractTheImageGrayScaleNumbersFromFile (GRAY_SCALE_NUMBERS_FILE_NAME =
            'f:\\grayScale.ppm')
    image = smoothTheImage (image, NUMBER_OF_TIMES_TO_SMOOTH_IMAGE)
    saveTheImageGrayScaleNumbersToFile (image, GRAY_SCALE_NUMBERS_FILE_NAME = 'f:\\smoothed.ppm')
#--<IMPORTS>-----------------------------------------------------MachineVision--

from tkinter import *
from time    import clock
from sys import setrecursionlimit
setrecursionlimit(7000) # optional (default = 1000)
#--<GLOBALS>-----------------------------------------------------MachineVision--

root      = Tk()
START     = clock()
WIDTH     = 512   # This value was obtained by looking at the file.
HEIGHT    = 512   # This value was obtained by looking at the file.
COLORFLAG = False # True = color image; False = Gray-scale image
HIGH      =  45   # found by experimenting (45 = best)
LOW       =  10   # found by experimenting (10 = best)
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 6
#======================================= MAIN =======================================MachineVision==
# WARNING: Do NOT use exit(); it will close all windows.

def main():
#   Note well: This program assumes it has access to a PPM-type file of size
#              512x512 named lena_rgb_p3.ppm.
    convertColorFileToGrayScaleFile()
    extractSmoothAndSaveImage()
    image = extractTheImageGrayScaleNumbersFromFile\
            (GRAY_SCALE_NUMBERS_FILE_NAME = 'f:\\smoothed.ppm')
##  displayImageInWindow(image) # Use this display or the one below, not both.

    imageLists = sobelTransformation(image)  # image = [...(mag, angle)...]

    printNormalizedImageLists(imageLists, False)

    imageLists = cannyTransform(imageLists)

    image = doubleThresholdImageListsInToGrayScaleValues(imageLists)

    displayImageInWindow(image)

    root.mainloop()
#----------------------------------------------------------------MachineVision--
if __name__ == '__main__':  main()
