import psutil
import json
import math
import re


def check_prime(number_to_check):

    initial_devider = 2
    final_devider = math.isqrt(number_to_check)  # final_devider = 1
    deviders = range(initial_devider, final_devider + 1)  # deviders = [2]
    check_result = True
    for current_devider in deviders:
        if number_to_check % current_devider == 0:
            check_result = False
            break
        else:
            check_result = True

    return check_result


process_list = []

for process in psutil.process_iter(["pid", "name"]):
    process_name = process.info["name"]  # получаем столбец с именами процессов
    process_number = process.info["pid"]  # получаем столбец с номерами процессов
    reg_process_name = re.search(r"skype", process_name)
    if reg_process_name:
        dict_in_file = {}
        dict_in_file["Process Name"] = process_name
        dict_in_file["Process Number"] = process_number
        process_after_check_prime = check_prime(process_number)
        dict_in_file["Is Prime"] = process_after_check_prime
        dict_in_file["Is Composite"] = not process_after_check_prime
        process_list.append(dict_in_file)


with open("process_output.json", "w") as file:
    json.dump(process_list, file)
