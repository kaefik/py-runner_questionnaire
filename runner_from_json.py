"""
плеер (runner) файла бесед из файлов json
"""

import json

from utils.i_utils import validate_url

types_answer_message = {"int": "число", "string": "строка",
                        "float": "число с плавающей точкой", "list": "список ответов", "url": "урл"}


def runner(all_question, command_exit="exit"):
    """
    запуск беседы используя сценарий из json
    param: all_question - вопросы
           command_exit - команды прерывания из беседы
    return: словарь ответов на вопросы
    """
    result_data = {}

    for num in range(len(all_question)):
        question = all_question[num]
        var_question = question["var"]
        print(f"Ответьте на {num + 1} вопрос:-----------------------------")
        print(question["question"])
        type_answer = question["answer"]["type"]
        print(f"Ответ должен быть {types_answer_message[type_answer]}")

        if type_answer == "list":
            list_answer = question["answer"]["list_answer"]
            print("Нужно выбрать цифрой ответ из списка:")
            for i in range(len(list_answer)):
                print(f"{i + 1} - {list_answer[i]}")

        print(f"Для выхода введите команду: {command_exit}")
        answer = input(">> ")

        if answer == command_exit:
            return None



        if type_answer == "int":
            while not all(x.isdigit() for x in answer):
                print("Нужно ввести число. Попробуйте ещё раз.")
                answer = input(">> ")
            result_data[var_question] = int(answer)

        if type_answer == "float":
            flag_exit = True
            while flag_exit:
                try:
                    num_answer = float(answer)
                    flag_exit = False
                except ValueError:
                    print("Нужно ввести число. Попробуйте ещё раз.")
                    answer = input(">> ")
            result_data[var_question] = num_answer

        if type_answer == "list":
            flag_exit = True
            while flag_exit:
                try:
                    num_answer = int(answer)
                    print(num_answer)
                    if (num_answer <= 0) or (num_answer > len(list_answer)):
                        print("Нужно выбрать номер варианта ответа.")
                        answer = input(">> ")
                    else:
                        flag_exit = False
                except ValueError:
                    print("Нужно выбрать номер варианта ответа.")
                    answer = input(">> ")
                    # flag_exit = True
            result_data[var_question] = list_answer[num_answer - 1]

        if type_answer == "string":
            flag_exit = True
            while flag_exit:
                if answer.strip() == "":
                    print("Нужно чтобы строка была не пустой. Попробуйте еще раз.")
                    answer = input(">> ")
                else:
                    flag_exit = False
            result_data[var_question] = answer

        if type_answer == "url":
            flag_exit = True
            while flag_exit:
                if not validate_url(answer):
                    print("Введите урл сайта. Попробуйте еще раз.")
                    answer = input(">> ")
                else:
                    flag_exit = False
            result_data[var_question] = answer

        print("-------------------------------------------------------\n")

    return result_data


if __name__ == "__main__":
    with open("example.json") as f:
        all_question_json = f.read()

    all_question1 = json.loads(all_question_json)

    res = runner(all_question1)

    print(res)
