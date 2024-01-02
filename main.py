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
cur_timer=None
rep=0
click=0
new_text=""
pomodoro_text=""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global cur_timer
    global rep
    window.after_cancel(cur_timer)
    rep=0
    timer.config(text="Timer",fg=GREEN)
    tick.config(text="")
    pomodoro.config(text="")
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep+=1
    if rep%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Break", fg=RED)

    elif rep%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global cur_timer
        cur_timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        global rep
        global new_text
        global pomodoro_text
        if rep%8==0:
            new_text = ""
            pomodoro_text += "🍅 "
            pomodoro.config(text=pomodoro_text)
            tick.config(text=new_text)
        elif rep%2==0:
            new_text += "✔ "
            tick.config(text=new_text)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro timer app")
window.config(bg=YELLOW,pady=50,padx=50)

tomato_image=PhotoImage(file="tomato.png")
canvas=Canvas(width=200, height=224)
canvas.create_image(100,112,image=tomato_image)
canvas.config(bg=YELLOW,highlightthickness=0)
#timer_text
timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,36,"bold"))
canvas.grid(column=1 , row=1)

#Timer Label
timer=Label(text="Timer",font=(FONT_NAME,36,"bold"),bg=YELLOW,highlightthickness=0,fg=GREEN)
timer.grid(column=1 , row=0)
#Start Button
start=Button(text="start",font=(FONT_NAME,12,"normal"),highlightbackground=YELLOW,bg=YELLOW,command=start_timer)
start.grid(column=0 , row=2)
#Reset Button
reset=Button(text="reset",font=(FONT_NAME,12,"normal"),highlightbackground=YELLOW,bg=YELLOW,command=reset_timer)
reset.grid(column=2 , row=2)
#tick
tick=Label(text="",fg=GREEN,font=(FONT_NAME,24,"bold"),bg=YELLOW,highlightthickness=0)
tick.grid(column=1 , row=3)
#pomodoro
pomodoro=Label(text="",font=(FONT_NAME,24,"bold"),bg=YELLOW,highlightthickness=0,fg=RED)
pomodoro.grid(column=1, row=4)

window.mainloop()
