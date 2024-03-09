import json
from modules.is_num_prime import is_num_prime


def prime_sign_to_ru_output(is_prime, number_to_check):
    if is_prime:
        return "простое"
    else:
        if number_to_check == 0 or number_to_check == 1:
            return "ни простое, ни составное"
        return "составное"


if __name__ == "__main__":
    with open("/data/process_output.json", "r") as file_with_processes_data:
        processes_data = json.load(file_with_processes_data)

    errors_found = 0
    for process_data in processes_data:
        process_id = process_data["Process ID"]
        process_name = process_data["Process Name"]

        ru_prime_sign_data_in_file = prime_sign_to_ru_output(
            process_data["Is Prime"], process_id
        )
        ru_prime_sign_data_actual = prime_sign_to_ru_output(
            is_num_prime(process_id), process_id
        )

        if ru_prime_sign_data_in_file != ru_prime_sign_data_actual:
            errors_found += 1

            print(
                "Для {0} процесса найдена ошибка в файла. "
                "Число(PID) {1} на самом деле {2}, "
                "а в файле написано {3}.\n".format(
                    process_name,
                    process_id,
                    ru_prime_sign_data_actual,
                    ru_prime_sign_data_in_file,
                    errors_found,
                )
            )

    if errors_found == 0:
        print("Файл проверен. Ошибок не найдено")
    else:
        print("В файле найдены ошибки: {0} штуки".format(errors_found))
