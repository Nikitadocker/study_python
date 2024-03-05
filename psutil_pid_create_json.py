import psutil
import json
import re
import os
from modules.is_num_prime import is_num_prime

process_list = []

for process in psutil.process_iter(["pid", "name"]):
    process_name = process.info["name"]  # получаем столбец с именами процессов
    process_number = process.info["pid"]  # получаем столбец с номерами процессов

    dict_in_file = {"Process Name": process_name, "Process ID": process_number}
    
    process_filter = os.environ.get('PROCESS_FILTER')
    reg_process_name = re.search(r"{0}".format(process_filter), process_name)
    if reg_process_name:

        if process_number == 1:
            dict_in_file["Is Prime"] = False
        elif process_number == 2 or process_number == 3:
            dict_in_file["Is Prime"] = True
        else:
            process_after_check_prime = is_num_prime(process_number)
            dict_in_file["Is Prime"] = process_after_check_prime

        process_list.append(dict_in_file)

with open("process_output.json", "w") as file:
    json.dump(process_list, file)
