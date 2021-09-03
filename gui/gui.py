"""
GUI для создания json-бесед
"""

import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generator for json-conversation")
        self.geometry("500x400")

        labelQuestion = tk.Label(self, text="Question")
        labelVariable = tk.Label(self, text="Variable")
        entryQuestion = tk.Entry(self, width=40)
        entryVariable = tk.Entry(self, width=40)

        self.widgetQuestion = zip(labelQuestion, entryQuestion)
        self.widgetVariable = zip(labelVariable, entryVariable)

        # self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Add",
                                command=self.print_info)
        self.close = tk.Button(self, text="Close",
                               command=self.quit)

        labelQuestion.grid(row=0, column=0, padx=10, sticky=tk.W)
        entryQuestion.grid(row=0, column=1, padx=10, pady=5)

        labelVariable.grid(row=1, column=0, padx=10, sticky=tk.W)
        entryVariable.grid(row=1, column=1, padx=10, pady=5)

        # вывод типов данных
        labelTypes = tk.Label(self, text="Type variable")
        labelTypes.grid(row=4, column=0, padx=10, sticky=tk.W)

        TYPES = [("Int", "int"), ("Float", "float"), ("String", "string"), ("List", "list"), ("Url", "url")]
        self.var = tk.StringVar()
        self.var.set("int")
        self.buttons = [self.create_radio(c) for c in TYPES]
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
        return tk.Radiobutton(self, text=text, value=value,
                              command=self.print_option,
                              variable=self.var)

    def print_info(self):
        # for label, entry in self.widgets:
        #     print("{} = {}".format(label.cget("text"), entry.get()))
        # print(self.var.get())
        pass

    def print_option(self):
        print(self.var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
