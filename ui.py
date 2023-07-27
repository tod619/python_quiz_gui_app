from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.mainloop()
