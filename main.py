from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(bg_image, image=ready)

    timer_label.config(text="Ready...", fg=GREEN)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(bg_image, image=take_easy)
        timer_label.config(text="Rest...", fg=GREEN)

    else:
        count_down(work_sec)
        canvas.itemconfig(bg_image, image=hard_work_image)
        timer_label.config(text="WORK TIME!!!", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_sec = count % 60
    count_min = math.floor(count / 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        global reps
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_mark.config(text=marks)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=10, pady=5, bg=YELLOW)

timer_label = Label(text="Ready...", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=1920, height=1080, bg=YELLOW, highlightthickness=0)

take_easy = PhotoImage(file="thumb-1920-1201190.png")
hard_work_image = PhotoImage(file="thumb-1920-1196683.png")
ready = PhotoImage(file="thumb-1920-1201187.png")

bg_image = canvas.create_image(960, 540, image=ready)

timer_text = canvas.create_text(960, 540, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

check_mark = Label(text="", bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
