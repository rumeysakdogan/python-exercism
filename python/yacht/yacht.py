# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    """
    Calculates score according to chosen category

    :params dice: list[int] - stores the outcome of 5 rolled dice
    :return: int - total score
    """

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    total = 0

    for i in dice:
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
        elif i == 4:
            count4 += 1
        elif i == 5:
            count5 += 1
        else:
            count6 += 1

    count_list = [count1, count2, count3, count4, count5, count6]

    for i in dice:
        total += i

    if category == 'ONES':
        return count1
    elif category == 'TWOS':
        return count2 * 2
    elif category == 'THREES':
        return count3 * 3
    elif category == 'FOURS':
        return count4 * 4
    elif category == 'FIVES':
        return count5 * 5
    elif category == 'SIXES':
        return count6 * 6
    elif category == 'FULL_HOUSE':
        three_of_one = False
        two_of_one = False
        for i in count_list:
            if i == 3:
                three_of_one = True
            if i == 2:
                two_of_one = True
        return total if three_of_one and two_of_one else 0
    elif category == 'FOUR_OF_A_KIND':
        four_of_one = False
        position = 0
        for i in count_list:
            if i == 4 or i == 5:
                four_of_one = True
            position += 1
            if four_of_one:
                break
        return position * 4 if four_of_one else 0
    elif category == 'LITTLE_STRAIGHT':
        return 30 if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 else 0
    elif category == 'BIG_STRAIGHT':
        return 30 if count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 == 1 else 0
    elif category == 'CHOICE':
        return total
    elif category == 'YACHT':
        all_same = False
        for i in count_list:
            if i == 5:
                all_same = True
        return 50 if all_same else 0
