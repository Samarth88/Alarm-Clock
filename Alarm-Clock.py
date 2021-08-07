#                                        *Alarm Clock*

#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound


def hello():
   messagebox.showinfo("Times Up", "Wake Up!")


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            hello()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.iconbitmap(r"C:\Users\SAMARTH\Desktop\alarm\logo.ico")
clock.geometry("400x200")
Label(clock,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(clock,text="Enter Time: ",font=("Helvetica 10 ")).pack()
Label(clock,text="(24 Hour format) ",font=("Helvetica 8 ")).pack()
Label(clock,text = " Hour      Min            Sec",font=("Helvetica 10")).place(x = 110, y = 97)
#setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=120)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=120)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=120)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =160,y=150)

clock.mainloop()
#Execution of the window.

