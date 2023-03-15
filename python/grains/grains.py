""" Solves grain problem"""


def square(number):
    """ Calculates the number of grains in given square

    :param number: int - number should be between 1 and 64
    :return: int - amount of grains in a gven square 
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """ Calculates the total number of grains on chessboard

    :return: int - total of number grains 
    """
    total_grains = 0
    for i in range(0, 64):
        total_grains += 2 ** i

    return total_grains
