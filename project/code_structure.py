# TODO: Stage 1 - Indentation Essentials
# 
# Instructions:
# 1. Fix the indentation in check_grade() function (if/elif/else blocks)
# 2. Fix the indentation in print_numbers() function (for loop)
# 3. Fix the indentation in countdown() function (while loop)
# 4. Complete the is_even() function by adding the if/else logic with correct indentation


def check_grade(score):
    """
    Return a grade based on the score.
    Should return "A" for score >= 90, "B" for >= 80, "C" for >= 70, "F" otherwise.
    """
    # TODO: Fix the indentation errors in the if/elif/else blocks below
    if score >= 90:
    return "A"
    elif score >= 80:
    return "B"
    elif score >= 70:
    return "C"
    else:
    return "F"


def print_numbers(n):
    """
    Print numbers from 1 to n (inclusive).
    """
    # TODO: Fix the indentation error in the for loop below
    for i in range(1, n + 1):
    print(i)


def countdown(start):
    """
    Print a countdown from start to 1, then print "Blast off!".
    """
    # TODO: Fix the indentation errors in the while loop below
    num = start
    while num > 0:
    print(num)
    num = num - 1
    print("Blast off!")


def is_even(number):
    """
    Return True if number is even, False otherwise.
    A number is even if it is divisible by 2 (number % 2 == 0).
    """
    # TODO: Complete this function by adding if/else logic with correct indentation
    # Hint: Check if number % 2 == 0, return True if yes, False otherwise
    pass

