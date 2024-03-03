import json
from check_prime import check_prime

math_eng_ru_translation = {
    False: "Cоставное",
    True: "Простое",
    "1": "ни простое ни составное"
}
with open("process_output.json", "r+") as file:

    file_check = json.load(file)  # <class 'list'>


for key in file_check:

    process_number = key["Process Number"]
    process_name = key["Process Name"]

    result_before_check = key["Is Prime"]
    
     
    

    result_after_check = check_prime(process_number)



    if result_before_check != result_after_check: # True неравно False "
        if process_number == 1:
            result_after_check = "1"
        print(
            "Pid процесс с именем {0} проверен. Найдена ошибка. Число {1} на самом деле {2}, а в файле написано {3}".format(
                process_name, # systemd
                process_number, # 1
                math_eng_ru_translation[result_after_check].lower(), # 1
                math_eng_ru_translation[result_before_check].lower(),  # True в простое
            )
        )
