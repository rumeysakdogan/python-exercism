def convert(number):
    """Converts a number into a string that contains
      raindrop sounds corresponding to certain potential
      factors. A factor is a number that evenly 
      divides into another number, leaving no remainder.

    Args:
        number (int): 
    """
    result = ""
    factors = [3, 5, 7]

    for i in factors:
        if number % i == 0:
            if i == 3:
                result += "Pling"
            elif i == 5:
                result += "Plang"
            elif i == 7:
                result += "Plong"

    return result if result != "" else str(number)
