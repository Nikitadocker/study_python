import subprocess
import json
import math


def check_prime(number_to_check):
    if number_to_check == 2 or number_to_check == 3:
        check_result = "Prime"

    else:
        check_result = "Not Prime and Composite"
        initial_devider = 2
        final_devider = math.isqrt(number_to_check)  # final_devider = 1
        deviders = range(initial_devider, final_devider + 1)  # deviders = [2]
        for current_devider in deviders:
            if number_to_check % current_devider == 0:
                check_result = "Composite"
                break
            else:
                check_result = "Prime"

    return check_result


result = subprocess.run(["ps", "aux", "--no-headers"], capture_output=True, text=True)


final_result = []
for line in result.stdout.splitlines():
    # Разделить строку по пробелам
    fields = line.split()
    # Извлечь PID из второго столбца
    pid = fields[1]

    # Извлечь NAME PID из десятого столбца
    name_pid = fields[10]

    pids = {}

    pids["Process Number"] = int(pid)
    
    pids["Processs Name"] = name_pid
    
    result_check = check_prime(int(pid))

    if result_check == "Prime":

        result_check = True
    else:
        result_check = False

    pids["Is Prime"] = result_check

    result_check_is_composite = check_prime(int(pid))

    if result_check_is_composite == "Composite":

        result_check_is_composite = True
    else:
        result_check_is_composite = False

    pids["Is Composite"] = result_check_is_composite

    final_result.append(pids)


with open("output_pids.json", "w") as file:
    json.dump(final_result, file)