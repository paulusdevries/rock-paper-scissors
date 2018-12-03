from tkinter import *

class Todo(Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("To-do app v1")
        self.geometry("300x400")
        todo1 = Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        self.task_create = Text(self, height=3, bg="white", fg="black")
        self.task_create.pack(side=BOTTOM, fill=X)
        self.task_create.focus_set()
        self.bind("<Return>", self.add_task)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black" }, {"bg": "grey", "fg": "white"}]


    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, END).strip()

        if len(task_text) > 0:
            new_task = Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=TOP, fill=X)

        self.task_create.delete(1.0, END)

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
