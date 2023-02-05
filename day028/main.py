from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#58d68d"
ORANGE = "#ffbe33"
PINK = "#ec7063"
RED = "#e7305b"
YELLOW = "#f7f5dd"
BLUE = "#1597E5"
PURPLE = "#7676EE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None
count_min = 0
count_sec = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global checkmark
    reps = 0
    checkmark = ""

    window.after_cancel(timer)
    status_label.config(text=" Reset ", fg="red")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text=checkmark)
    pause_button.config(text="Pause", command=pause)

    start_button['state'] = NORMAL
    pause_button['state'] = DISABLED

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    reps += 1

    if reps % 8 == 0:
        status_label.config(text="Chill! ", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        status_label.config(text="Break! ", fg=ORANGE)
        count_down(short_break_sec)
    else:
        status_label.config(text="Work...", fg=GREEN)
        count_down(work_sec)

    start_button['state'] = DISABLED
    reset_button['state'] = NORMAL
    pause_button['state'] = NORMAL

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global checkmark
    global count_min
    global count_sec

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)
        if reps > 8:
            window.after_cancel(timer)
            status_label.config(text="Done:) ", fg=PURPLE)
            canvas.itemconfig(timer_text, text="00:00")
            start_button['state'] = DISABLED
            pause_button['state'] = DISABLED

# ---------------------------- PAUSE / RESUME ------------------------------- #
def pause():
    global current_status_label
    global current_status_label_color

    current_status_label = status_label.cget("text")
    current_status_label_color = status_label.cget("fg")
    window.after_cancel(timer)
    pause_button.config(text="Resume", command=resume)
    status_label.config(text="Paused ", fg=BLUE)

def resume():
    pause_button.config(text="Pause", command=pause)
    saved_data = count_min * 60 + int(count_sec)
    count_down(saved_data)
    status_label.config(text=current_status_label, fg=current_status_label_color)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string="Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

status_label = Label(text=" Timer ", fg="black", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
status_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", bg="white", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
start_button['state'] = NORMAL

reset_button = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button['state'] = DISABLED

pause_button = Button(text="Pause", bg="white", font=(FONT_NAME, 10, "bold"), command=pause)
pause_button.grid(column=1, row=4)
pause_button['state'] = DISABLED

window.mainloop()