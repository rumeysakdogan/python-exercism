def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum_of_factors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_factors += i

    if number < 1:
        raise ValueError(
            "Classification is only possible for positive integers.")

    if number == sum_of_factors:
        return "perfect"
    elif number < sum_of_factors:
        return "abundant"
    else:
        return "deficient"
