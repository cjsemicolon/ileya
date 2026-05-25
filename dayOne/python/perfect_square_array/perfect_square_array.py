import math
def return_perfect_squares(numbers):

    perfectSquares = [];

    index = 0;

    for element in numbers: 

        squareRoot = int(math.sqrt(element));

        if squareRoot * squareRoot == element: 

            perfectSquares.append(element)

            index+=1;    

    return perfectSquares;

  
