def is_bouncy(number):
    """Return True if number is bouncy, otherwise return False.

    :param number: a positive integer number
    """
    increasing = False
    decreasing = False

    last_number = number % 10
    number = number // 10

    while number > 0:
        next_number = number % 10
        number = number // 10
        if next_number < last_number:
            increasing = True
        elif next_number > last_number:
            decreasing = True

        last_number = next_number

        if decreasing and increasing:
            return True

    return False


def find_least_bouncy_number():
    """Return least number for which the proportion of bouncy numbers is exactly 99%."""
    current_number = 99
    bouncies = 0
    percentage = 0.0
    while percentage < 99.0:
        current_number += 1
        if is_bouncy(current_number):
            bouncies += 1
            percentage = bouncies * 100 / current_number
    return current_number, percentage
