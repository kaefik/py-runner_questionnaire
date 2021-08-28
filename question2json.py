"""
сохраняет вопросы которые вводит пользователь в файл бесед/анкеты json
"""

"""
{
  'question': "текст вопроса",
  'answer': {
    'type': тип_ответа,
    'list_answer': список_возможных_ответов
  }
}
"""

import json

AllTypeAnswer = {"1": "int", "2": "float", "3": "string", "4": "list", "5": "url"}


def generate_question(TypeAnswer):
    """
    генерация одного вопроса
    """

    var_question = input("Введите имя переменной для вопроса: ")
    s_question = input("Введите вопрос: ")

    print("\nВыберите тип ответа: ")
    num = 1
    for k, i in TypeAnswer.items():
        print(f"{k} - {i}")

    flag_exit = True
    while flag_exit:
        try:
            s_type_answer = input("Введите число ответа: ")
            print("Вы выбрали тип: ", TypeAnswer[s_type_answer])
            flag_exit = False
        except KeyError:
            print("Введите корректный номер типа. Попробуйте ещё раз.")

    if TypeAnswer[s_type_answer] != 'list':
        quest_anketa = {
            'var': var_question,
            'question': s_question,
            'answer': {
                'type': TypeAnswer[s_type_answer]
            }
        }
    else:

        # блок ввода возможных ответов
        list_answer = []
        print("\nНачало блока списка возможных ответов")
        flag_exit = True
        n_answer = 1
        while flag_exit:
            s_answer = input(f"Введите {n_answer} ответ (для выхода введите exit): ")
            if s_answer == 'exit':
                print("Завершен выход из блока возможных ответов")
                flag_exit = False
            else:
                list_answer.append(s_answer)
                n_answer = n_answer + 1

        quest_anketa = {
            'var': var_question,
            'question': s_question,
            'answer': {
                'type': TypeAnswer[s_type_answer],
                'list_answer': list_answer
            }
        }
    return quest_anketa


def generate_conversation(TypeAnswer):
    """
    генерации бесед
    """
    flag_exit = True
    n_question = 1
    all_questions = []
    while flag_exit:
        print(f"Введите {n_question} блок беседы/анкеты -------------------------------")
        current_question = generate_question(TypeAnswer)
        all_questions.append(current_question)
        n_question = n_question + 1
        block_question = input("Продолжим процесс наполнения бесед? Если хотите выйти наберите exit:")
        if block_question == "exit":
            print("Процесс наполнения завершён.")
            flag_exit = False

        print("------------------------------------------------------------------------\n")
    return all_questions


if __name__ == "__main__":
    questions = generate_conversation(AllTypeAnswer)
    # конвертируем в JSON:
    y = json.dumps(questions, ensure_ascii=False)
    # в результате получаем строк JSON:
    print(y)

    with open("example.json", "w") as f:
        f.write(y)
