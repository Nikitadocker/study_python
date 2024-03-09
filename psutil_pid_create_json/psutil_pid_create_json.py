import psutil
import json
import re
import os
import subprocess
from modules.is_num_prime import is_num_prime

process_list = []

get_method = os.environ.get("GET_METHOD")
if get_method == "subprocess":
    subprocess_work = subprocess.run(
        ["ps", "aux", "--no-headers"], capture_output=True, text=True
    )
    all_process = subprocess_work.stdout.splitlines()

if get_method == "psutil":
    all_process = psutil.process_iter(["pid", "name"])


for process in all_process:
    if get_method == "psutil":

        process_name = process.info["name"]  # получаем столбец с именами процессов
        process_number = process.info["pid"]  # получаем столбец с номерами процессов

    if get_method == "subprocess":

        fields = process.split()
        process_name = fields[10]
        process_number = fields[1]

    dict_in_file = {"Process Name": process_name, "Process ID": process_number}

    process_filter = os.environ.get("PROCESS_FILTER")

    reg_process_name = re.search(r"{0}".format(process_filter), process_name)
    if reg_process_name:

        if process_number == 1:
            dict_in_file["Is Prime"] = False
        elif process_number == 2 or process_number == 3:
            dict_in_file["Is Prime"] = True
        else:
            process_after_check_prime = is_num_prime(int(process_number))
            dict_in_file["Is Prime"] = process_after_check_prime

        process_list.append(dict_in_file)

with open("/data/process_output.json", "w") as file:
    json.dump(process_list, file)

