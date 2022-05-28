import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white",
                                         font=("Arial", 12, "normal"), highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_button_image, highlightthickness=0,
                                          command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_button_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_button_image, highlightthickness=0,
                                           command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer):
        self.true_button.config(state=tkinter.DISABLED)
        self.false_button.config(state=tkinter.DISABLED)
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.true_button.config(state=tkinter.NORMAL)
            self.false_button.config(state=tkinter.NORMAL)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.destroy()
            self.false_button.destroy()
