from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):

        self.new_ques = quiz
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzier")

        self.score = Label(text="Score : 0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, width=280, text="Hello", font=(24))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right, highlightthickness=0, bg=THEME_COLOR, command=self.right1)
        self.right_button.grid(column=0, row=3)
        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, bg=THEME_COLOR, command=self.wrogn1)
        self.false_button.grid(column=1, row=3)
        self.next_q()
        self.window.mainloop()

    def next_q(self):
        self.canvas.config(bg="white")
        if self.new_ques.still_has_questions():
            self.score.config(text=f"Score : {self.new_ques.score}")
            question = self.new_ques.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="Game Over")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right1(self):
        self.give_feedback(self.new_ques.check_answer("True"))

    def wrogn1(self):
        self.give_feedback(self.new_ques.check_answer("False"))

    def give_feedback(self, right1):
        if right1:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_q)
