import subprocess
import json
import math


def check_prime(number_to_check):

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

    if int(pid) == 1:
        pids["Is Prime"] = False
        pids["Is Composite"] = False
    elif int(pid) == 2 or int(pid) == 3:

        pids["Is Prime"] = True
        pids["Is Composite"] = False
    else:

        result_check = check_prime(int(pid))
        pids["Is Prime"] = result_check
        pids["Is Composite"] = not result_check

    final_result.append(pids)


with open("output_pids.json", "w") as file:
    json.dump(final_result, file)
