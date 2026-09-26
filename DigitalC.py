from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    mon = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_Sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=mon)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200,date_time)
    

clock = Tk()
clock.title("Shubham DIgital Clock")
clock.geometry("600x300")
clock.config(bg="grey")

# ****** HOURS ******

lab_hr = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_hr.place(x=40,y=10,height=110,width=100)
lab_hr_Text = Label(clock,text="Hour",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_hr_Text.place(x=40,y=130,height=30,width=100)

# ****** MINUTES *******

lab_min = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_min.place(x=180,y=10,height=110,width=100)
lab_min_Text = Label(clock,text="Min",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_min_Text.place(x=180,y=130,height=30,width=100)

# ****** SECOND *****

lab_Sec = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_Sec.place(x=320,y=10,height=110,width=100)
lab_Sec_Text = Label(clock,text="Sec",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_Sec_Text.place(x=320,y=130,height=30,width=100)

# ***** AM/PM *****

lab_am = Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="red",fg="white")

lab_am.place(x=460,y=10,height=110,width=100)
lab_am_Text = Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_am_Text.place(x=460,y=130,height=30,width=100)

# **** Date ******

lab_date = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_date.place(x=40,y=170,height=90,width=100)
lab_date_Text = Label(clock,text="Date",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_date_Text.place(x=40,y=265,height=30,width=100)

# ***** month *******
lab_mon = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_mon.place(x=320,y=170,height=90,width=100)
lab_mon_Text = Label(clock,text="month",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_mon_Text.place(x=320,y=265,height=30,width=100)


# ****** year ******

lab_year = Label(clock,text="00",font=("Time New Roman",60,"bold"),bg="red",fg="white")

lab_year.place(x=460,y=170,height=90,width=100)
lab_year_Text = Label(clock,text="Year",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_year_Text.place(x=460,y=265,height=30,width=100)

# ****** Day ******

lab_day = Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")

lab_day.place(x=180,y=170,height=90,width=100)
lab_day_Text = Label(clock,text="Day",font=("Time New Roman",20,"bold"),bg="red",fg="white")

lab_day_Text.place(x=180,y=265,height=30,width=100)
date_time()
clock.mainloop()