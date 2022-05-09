from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

after_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(after_timer)
    timer.reset()
    canvas.itemconfig(timer_text, text='00:00')



# ---------------------------- TIMER MECHANISM ------------------------------- #
class Timer:
    def __init__(self, work_min, short_break_min, long_break_min, n_work_interactions):
        self._time_sequence = []
        for i in range(n_work_interactions):
            self._time_sequence.append(work_min * 60)
            self._time_sequence.append(short_break_min * 60) if i != n_work_interactions - 1 \
                else self._time_sequence.append(long_break_min * 60)
        self._stage = 0

    def get_next_interaction_time(self):
        if self._stage == len(self._time_sequence):
            return 0
        result = self._time_sequence[self._stage]
        self._stage += 1
        return result

    def reset(self):
        self._stage = 0

    def count_down(self, count):
        min = int(count / 60)
        seg = count % 60

        if count >= 0:
            return f'{min}:{seg}'
        elif self._stage != len(self._time_sequence):
            count_down(self.get_next_interaction_time())


def start_timer():
    count_down(timer.get_next_interaction_time())

# timer = Timer(WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, 4)
timer = Timer(1, 1, 1, 2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=timer.count_down(count))
    global after_timer
    after_timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)

# Labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # (100,112) is the center of the canvas
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
