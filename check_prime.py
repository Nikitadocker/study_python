import math


def check_prime(number_to_check):
    if number_to_check == 2 or number_to_check == 3:
        check_result = True
    elif number_to_check == 1:
        check_result = False

    else:
        initial_devider = 2
        final_devider = math.isqrt(number_to_check)  # final_devider = 1
        deviders = range(initial_devider, final_devider + 1)  # deviders = [2]
        for current_devider in deviders:
            if number_to_check % current_devider == 0:
                check_result = False
                break
            else:
                check_result = True

    return check_result
