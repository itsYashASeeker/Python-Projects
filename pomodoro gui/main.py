import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
check = " "


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps -= 1


def skip_break():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reset_to_work()
    if (reps-1) % 2 == 0:
        reps += 1


# ---------------------------- Break TO Work------------------------------- #
def reset_to_work():
    global check
    check += "✅"
    timer_label.config(text="WORK", fg=GREEN)
    start_button.config(text="Work!")
    end_button.config(text="Reset", command=reset, width=6)
    check_label.config(text=check)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mech():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(short_break_sec)
    else:
        start_button.config(text="Work!")
        end_button.config(text="Reset", command=reset, width=6)
        timer_label.config(text="WORK", fg="GREEN")
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if (reps - 1) % 2 == 0:
            if reps % 7 == 0:
                timer_label.config(text="Long Break", fg=PINK)
            else:
                timer_label.config(text="Break", fg=PINK)
            start_button.config(text="Break")
            end_button.config(text="Skip Break", command=skip_break, width=8)
        if reps % 2 == 0:
            reset_to_work()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(row=1, column=1)

# label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg="green", bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = Label(fg="green")
check_label.grid(row=2, column=1)

# buttons
start_button = Button(text="Work!", height=2, width=6, command=timer_mech)
start_button.grid(row=2, column=0)

end_button = Button(text="RESET", height=2, width=6, command=reset)
end_button.grid(row=2, column=2)

window.mainloop()
