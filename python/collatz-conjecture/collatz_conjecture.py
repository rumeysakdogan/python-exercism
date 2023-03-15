def steps(number):
    """
    This function calculates number of steps to
    be performed to reach 1. If number is even,
    next number will be n / 2. If number is odd, 
    following number will be 3 * n + 1.

    @param number: int - takes an integer
    @return : int - number of steps to reach 1
    """
    count = 0
    reach_one = False

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return 0

    while not reach_one:
        if number % 2 == 0:
            number = number / 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1

        if number == 1:
            reach_one = True

    return count
