def is_armstrong_number(number):
    """ Checks if a number is Armstrong or not.

    @param number: int - takes an integer
    @return : bool - returns True if number 
    equals to sum of its each digit to 
    the power of number of digits.
    """
    num_as_str = str(number)
    num_of_digits = len(num_as_str)
    sum_of_digits = 0

    for i in num_as_str:
        sum_of_digits += int(i) ** num_of_digits

    return True if sum_of_digits == number else False
