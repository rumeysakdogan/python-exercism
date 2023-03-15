def equilateral(sides):
    """ Checks if given triangle is equilateral or not.

    : param sides: list(int) - each side of triangle
    :return: bool -true if all sides are equal
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a == b and b == c:
                return True
            return False
        return False
    return False


def isosceles(sides):
    """ Checks if given triangle is isosceles or not.

    : param sides: list(int) - each side of triangle
    :return: bool - true if only two sides equal
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if equilateral(sides):
                return True
            if not equilateral(sides) and a == b or b == c or a == c:
                return True
            return False
        return False
    return False


def scalene(sides):
    """ Checks if given triangle is scalene or not.

    : param sides: list(int) - each side of triangle
    :return: bool - true if all sides are different 
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if not equilateral(sides) and not isosceles(sides):
                return True
            return False
        return False
    return False
