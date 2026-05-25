import math

def replace_non_perfect_squares(numbers):
    replaced_non_perfect_squares = []

    for element in range(len(numbers)):
        square_root = int(math.sqrt(numbers[element]))

        if square_root * square_root == numbers[element]:
            replaced_non_perfect_squares.append(numbers[element])
        else:
            replaced_non_perfect_squares.append(-1)

    return replaced_non_perfect_squares
