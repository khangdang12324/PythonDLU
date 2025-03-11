inputList = [4,7,11,13,18,20]
#creating a list with square values of only the even numbers
squareList = [var**2 for var in inputList if var%2==0]
print(squareList)
#creating even square list for a range of numbers
squarelist1 = [s**2 for s in range(10)if s%2 == 0]
print(squarelist1)