"""Function that checks if a given year is leap year"""


def leap_year(year):
    """Checks if given year is a leap year

    :param year: int - given year
    :return: bool - True if given year is leap year
    """

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
