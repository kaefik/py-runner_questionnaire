"""
GUI для создания json-бесед
"""

import tkinter as tk
from enum import Enum
from typing import List


class Types(Enum):
    """
    доступные типы для типов переменных
    """
    int = "int"
    float = "float"
    string = "string"
    list = "list"
    url = "url"


class Question:
    """
    единица вопроса
    """

    def __init__(self, question: str = "", variable: str = "", types: Types = Types.int,
                 list_answer: List[str] = []) -> None:
        self.question = question
        self.variable = variable
        self.types = types
        self.list_answer = list_answer

    def to_dict(self):
        """
        {
          'question': "текст вопроса",
          'answer': {
            'type': тип_ответа,
            'list_answer': список_возможных_ответов
          }
        }
        """
        if self.list_answer:
            result = {
                "question": self.question,
                "answer": {
                    "type": self.types,
                    "list_answer": self.list_answer
                }

            }
        else:
            result = {
                "question": self.question,
                "answer": {
                    "type": self.types
                }

            }
        return result


class Answer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x200")
        self.answer = tk.StringVar()
        self.label = tk.Label(self, text="Добавление ответа")
        self.entryAnswer = tk.Entry(self, width=40, textvariable=self.answer)
        self.button = tk.Button(self, text="Закрыть", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.entryAnswer.pack()
        self.button.pack(pady=5, ipadx=2, ipady=2)

    def open(self):
        self.grab_set()
        self.wait_window()
        text_answer = self.answer.get()
        return text_answer


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.question: List[Question] = []  # список всех вопросов

        self.title("Generator for json-conversation")
        self.geometry("500x400")

        labelQuestion = tk.Label(self, text="Question")
        labelVariable = tk.Label(self, text="Variable")
        self.entryQuestion = tk.Entry(self, width=40)
        self.entryVariable = tk.Entry(self, width=40)

        self.widgetQuestion = zip(labelQuestion, self.entryQuestion)
        self.widgetVariable = zip(labelVariable, self.entryVariable)

        # self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Add",
                                command=self.add_question)
        self.close = tk.Button(self, text="Close",
                               command=self.quit)

        labelQuestion.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.entryQuestion.grid(row=0, column=1, padx=10, pady=5)

        labelVariable.grid(row=1, column=0, padx=10, sticky=tk.W)
        self.entryVariable.grid(row=1, column=1, padx=10, pady=5)

        # вывод типов данных
        labelTypes = tk.Label(self, text="Type variable")
        labelTypes.grid(row=4, column=0, padx=10, sticky=tk.W)

        TYPES = []
        for t in Types:
            TYPES.append((t.name, t.name))

        self.var_types = tk.StringVar()
        self.var_types.set("int")
        self.buttons = [self.create_radio(c) for c in TYPES]

        self.widgetTypes = zip(labelTypes, self.buttons)

        num_row = 0
        for button in self.buttons:
            button.grid(row=6 + num_row, column=1, sticky=tk.W, padx=10, pady=10)
            num_row += 1

        # вывод кнопок
        self.submit.grid(row=20, column=1, sticky=tk.W,
                         padx=10, pady=10)
        self.close.grid(row=20, column=1, sticky=tk.E, padx=10, pady=10)

    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self, text=text, value=value, variable=self.var_types)

    def add_question(self):
        """
        добавляем вопросы
        """

        types_question = self.var_types.get()

        list_answer = []  # TODO: сделать получения вариантов ответов
        if types_question == Types.list.value:
            # здесь нужно запускать диалоговые окна для получения вариантов ответов
            self.open_window()
            pass

        question = Question(question=self.entryQuestion.get(),
                            variable=self.entryVariable,
                            types=types_question, list_answer=list_answer)

        print(question.to_dict())

    def print_option(self):
        print(self.var.get())

    def open_window(self):
        answer = Answer(self)
        print(answer.open())


if __name__ == "__main__":
    app = App()
    app.mainloop()
