import math


def is_num_prime(number_to_check):
    check_result = None
    if number_to_check == 2 or number_to_check == 3:
        check_result = True
    elif number_to_check == 1 or number_to_check == 0:
        check_result = False
    else:
        initial_divider = 2
        final_divider = math.isqrt(number_to_check)
        dividers = range(initial_divider, final_divider + 1)
        for current_divider in dividers:
            if number_to_check % current_divider == 0:
                check_result = False
                break
            else:
                check_result = True
    return check_result
