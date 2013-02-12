import math

maxNum = 101
sumOfSquare = 0
squareOfSum = 0

for i in range(1, maxNum):
    sumOfSquare = pow(i, 2) + sumOfSquare
for i in range(1, maxNum):
    squareOfSum = i + squareOfSum
    
squareOfSum = pow(squareOfSum, 2)
print squareOfSum
print sumOfSquare
print (squareOfSum - sumOfSquare)

