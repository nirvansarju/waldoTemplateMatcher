# Nirvan Sarju
# Student No. 500889908

def grayscale(picture): 
  #Standard grayscale function using luminance
  for x in range(0,getWidth(picture)):
    for y in range(0,getHeight(picture)):
      px = getPixel(picture,x,y)
      pxRed = getRed(px)
      pxGreen = getGreen(px)
      pxBlue = getBlue(px)
      lumin = (pxRed+pxGreen+pxBlue)/3
      setColor(px,makeColor(lumin,lumin,lumin))
  
def getTemplateSum(template):
  # templateSum is declared global so that it can be used in compareOne without having to be calcultated multiple times 
  # when compareAll is called
  global templateSum 
  templateSum = 0
  for x in range(getWidth(template)):
    for y in range(getHeight(template)):
      px = getPixel(template,x,y)
      pxRed = getRed(px)   
      templateSum = templateSum+pxRed 
     
def compareOne(template,searchImage,x1,y1):
  imageSum = 0
  # For each specified x and y, check values inside the range of the area of the template
  for x in range(x1,x1+getWidth(template)):
    for y in range(y1,y1+getHeight(template)):
      p = getPixel(searchImage,x,y)
      pRed = getRed(p)  
      imageSum = imageSum+pRed   
  # Calculate the difference between the template and image sum to find the minimum change
  diff = templateSum - imageSum
  diff = abs(diff)
  return diff
  
  
def compareAll(template,searchImage):
  # maxWidth and maxHeight are constructed such that the function does not check pixels that are out of the bounds of the searchImage
  maxWidth = getWidth(searchImage)-(getWidth(template)-1)
  maxHeight = getHeight(searchImage)-(getHeight(template)-1)
  W = getWidth(searchImage)
  H = getHeight(searchImage)  
  global matrix 
  matrix = [[100000000000 for i in range(W)] for j in range(H)]  
  for x in range(0,maxWidth):
    for y in range(0,maxHeight): 
      matrix[x][y] = compareOne(template,searchImage,x,y)
  return matrix
  
def find2Dmin(matrix):
  minRow = 0
  minCol = 0
  minimum = 100000000000
  #for each row and column in the matrix, iterate through the rows and columns to find the minimum value 
  for row, r in enumerate(matrix):
    for col, c in enumerate(r):
      if c < minimum:
        minimum = c
        minRow = row
        minCol = col
  return (minRow,minCol)
        
def displayMatch(searchImage,x1,y1,w1,h1,color):
  for p in getPixels(searchImage):
    x = getX(p)
    y = getY(p)
    #set the bounds of the box below:
    if x <= x1 and x > x1-3 and y > y1 and y < y1+h1:
      setColor(p,color)
    if x <= x1+w1 and x > x1+w1-3 and y > y1 and y < y1+h1:
      setColor(p,color)
    if y <= y1 and y > y1-3 and x > x1-3 and x <= x1+w1:
      setColor(p,color)
    if y <= y1+h1 and y > y1+h1-3 and x > x1-3 and x <= x1+w1:
      setColor(p,color)
      
def findWaldo(targetJPG,searchJPG):
  grayscale(targetJPG)
  grayscale(searchJPG)
  getTemplateSum(targetJPG)
  W = getWidth(targetJPG)
  H = getHeight(targetJPG)
  coords = find2Dmin(compareAll(targetJPG,searchJPG))
  displayMatch(searchJPG,coords[0],coords[1]+17,W,H,red)
  show(searchJPG)
  
      