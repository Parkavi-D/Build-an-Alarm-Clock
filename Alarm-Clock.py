#                                        *Welcome to DataFlair Alarm Clock*


#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound



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
            winsound.PlaySound("sound.wav",winsound.SND_LOOP)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
clock.config(bg="blue")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="#618006",font=("georgia",12,"bold")).place(x=90,y=150)
addTime = Label(clock,text = "Hour  Min   Sec",fg="red",font=("georgia",15)).place(x = 220,y = 10  )
setYourAlarm = Label(clock,text = "When to wake you up",fg="white",bg="#618006",font=("georgia",10,"bold")).place(x=10, y=50)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "white",width = 5).place( x = 220,y = 50)
minTime= Entry(clock,textvariable = min,bg = "white",width = 5).place(x=280,y=50)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 5).place(x=335,y=50)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",bg="white",width = 10,font=("georgia",12),command = actual_time).place(x =160,y=100)

clock.mainloop()
#Execution of the window.

