from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import math
import webbrowser

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        current_time = tk.Label(self, text=time.strftime('%I:%M:%S %p'), font=('Times', 25, 'bold'))
        current_time.place(x=150, y=10)

        current_date = tk.Label(self, text=time.strftime('%d.%m.%Y'), font=('Times', 20, 'bold'))
        current_date.place(x=175, y=50)

        # *************** Buttons *************** #
        button1 = tk.Button(self, text='Alarm Clock', width=9, bg='#5499C7', activebackground='#7FB3D5', font=('verdana', 10, 'bold'), bd=3, relief=RAISED,
                            command=lambda: controller.show_frame(AlarmClock))
        button1.place(x=50, y=110)

        button2 = tk.Button(self, text='Countdown', width=9, bg='#5499C7', activebackground='#7FB3D5', font=('verdana', 10, 'bold'), bd=3, relief=RAISED,
                            command=lambda: controller.show_frame(Countdown))
        button2.place(x=150, y=110)

        button3 = tk.Button(self, text='Stopwatch', width=9, bg='#5499C7', activebackground='#7FB3D5', font=('verdana', 10, 'bold'), bd=3, relief=RAISED,
                            command=lambda: controller.show_frame(Stopwatch))
        button3.place(x=250, y=110)

        button4 = tk.Button(self, text='Exit', width=9, bg='#C0392B', activebackground='#D98880', font=('verdana', 10, 'bold'), bd=3, relief=RAISED,
                            command=lambda: Exit(self))
        button4.place(x=350, y=110)


class AlarmClock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text='Alarm Clock', font=('Cambria', 20, 'bold'), relief=FLAT, width=20).place(x=90)

        current_time = tk.Label(self, font=('times', 16, 'bold'))
        current_time.place(x=190, y=40)

        hour_label = tk.Label(self, text='Hours:', font=('open sans', 10, 'bold'))
        hour_label.place(x=10, y=70)
        hour_entry = Entry(self, width=8)
        hour_entry.place(x=65, y=75)

        minute_label = tk.Label(self, text='Minutes:', font=('open sans', 10, 'bold'))
        minute_label.place(x=130, y=70)
        minute_entry = Entry(self, width=8)
        minute_entry.place(x=200, y=75)

        second_label = tk.Label(self, text='Seconds:', font=('open sans', 10, 'bold'))
        second_label.place(x=260, y=70)
        second_entry = Entry(self, width=8)
        second_entry.place(x=330, y=75)

        ampm_label = tk.Label(self, text='AM/PM:', font=('open sans', 10, 'bold'))
        ampm_label.place(x=390, y=70)
        ampm_entry = Entry(self, width=5)
        ampm_entry.place(x=455, y=75)

        tk.Label(self, text='Monday', font=('open sans', 10, 'bold')).place(x=5, y=100)
        tk.Label(self, text='Tuesday', font=('open sans', 10, 'bold')).place(x=70, y=100)
        tk.Label(self, text='Wednesday', font=('open sans', 10, 'bold')).place(x=140, y=100)
        tk.Label(self, text='Thursday', font=('open sans', 10, 'bold')).place(x=230, y=100)
        tk.Label(self, text='Friday', font=('open sans', 10, 'bold')).place(x=305, y=100)
        tk.Label(self, text='Saturday', font=('open sans', 10, 'bold')).place(x=360, y=100)
        tk.Label(self, text='Sunday', font=('open sans', 10, 'bold')).place(x=435, y=100)

        monday_box = tk.Checkbutton(self)
        monday_box.place(x=25, y=120)

        tuesday_box = tk.Checkbutton(self)
        tuesday_box.place(x=90, y=120)

        wednesday_box = tk.Checkbutton(self)
        wednesday_box.place(x=170, y=120)

        thursday_box = tk.Checkbutton(self)
        thursday_box.place(x=255, y=120)

        friday_box = tk.Checkbutton(self)
        friday_box.place(x=315, y=120)

        saturday_box = tk.Checkbutton(self)
        saturday_box.place(x=380, y=120)

        sunday_box = tk.Checkbutton(self)
        sunday_box.place(x=450, y=120)

        alarm_btn = tk.Button(self, text='Set Alarm', font=('verdana', 10, 'bold'), bg='#28B463', activebackground='#82E0AA', bd=3, relief=RAISED, command=lambda: set_alarm())
        alarm_btn.place(x=210, y=150)

        def tick():
            global time_label
            time_label = time.strftime('%I:%M:%S %p')
            current_time.config(text=time_label)
            current_time.after(200, tick)

        def alarm(set_time):
            while True:
                time.sleep(1)
                if time.strftime('%I:%M:%S %p') == set_time:
                    webbrowser.open_new('https://www.youtube.com/watch?v=iNpXCzaWW1s')
                    break

        def set_alarm():
            hr = hour_entry.get()
            min = minute_entry.get()
            sec = second_entry.get()
            ampm = ampm_entry.get().upper()
            if hr == '' or min == '' or sec == '' or ampm == '':
                messagebox.showerror('ERROR', 'All field are required !')
            else:
                set_time = '{}:{}:{} {}'.format(hr, min, sec, ampm)
                alarm(set_time)

        tk.Button(self, text="Clock", font=('verdana', 10, 'bold'), width=9, bd=3, bg='#5499C7', activebackground='#7FB3D5', relief=RAISED, command=lambda: controller.show_frame(MainWindow)).place(y=150)
        tk.Button(self, text="Exit", font=('verdana', 10, 'bold'), width=9, bg='#C0392B', activebackground='#D98880', bd=3, relief=RAISED, command=lambda: Exit(self)).place(x=407, y=150)
        tick()

class Countdown(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def down_count(count):
            seconds = math.floor(count % 60)
            minutes = math.floor((count / 60) % 60)
            hours = math.floor((count / 3600))
            status_label['text'] = "Hours: " + str(hours) + "   Minutes: " + str(minutes) + "   Seconds: " + str(seconds)

            if count >= 0:
                self.after(1000, down_count, count - 1)
            else:
                for x in range(1):
                    webbrowser.open_new('https://www.youtube.com/watch?v=iNpXCzaWW1s')
                    status_label['text'] = "Time is up!"

        def update_button():
            hour, minute, sec = hour_entry.get(), minute_entry.get(), second_entry.get()
            if hour.isdigit() and minute.isdigit() and sec.isdigit():
                time_left = int(hour) * 3600 + int(minute) * 60 + int(sec)
                down_count(time_left)

        hour_label = tk.Label(self, text='Hours:', font=('open sans', 10, 'bold'))
        hour_label.place(x=50, y=70)
        hour_entry = Entry(self, width=8)
        hour_entry.place(x=105, y=75)

        minute_label = tk.Label(self, text='Minutes:', font=('open sans', 10, 'bold'))
        minute_label.place(x=170, y=70)
        minute_entry = Entry(self, width=8)
        minute_entry.place(x=240, y=75)

        second_label = tk.Label(self, text='Seconds:', font=('open sans', 10, 'bold'))
        second_label.place(x=300, y=70)
        second_entry = Entry(self, width=8)
        second_entry.place(x=370, y=75)

        tk.Label(self, text='Countdown', font=('Cambria', 25, 'bold'), relief=FLAT, width=20).place(x=60)

        status_label = tk.Label(self, width=38, bg='pink', font=('open sans', 10, 'bold'), justify=CENTER)
        status_label.place(x=95, y=115)

        start_btn = tk.Button(self, text='Start Timer', font=('verdana', 10, 'bold'), bg='#28B463', activebackground='#82E0AA', width=9, bd=3, relief=RAISED, command=update_button)
        start_btn.place(x=200, y=150)

        tk.Button(self, text="Clock", font=('verdana', 10, 'bold'), width=9, bg='#5499C7', activebackground='#7FB3D5', bd=3, relief=RAISED, command=lambda: controller.show_frame(MainWindow)).place(y=150)
        tk.Button(self, text="Exit", font=('verdana', 10, 'bold'), width=9, bg='#C0392B', activebackground='#D98880', bd=3, relief=RAISED, command=lambda: Exit(self)).place(x=407, y=150)

class Stopwatch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global counter, running
        counter = 66600
        running = False

        def counter_label(status_label):
            def count():
                if running:
                    global counter

                    if counter == 66600:
                        display = "STARTING..."
                    else:
                        tt = datetime.fromtimestamp(counter)
                        string = tt.strftime("%H:%M:%S")
                        display = string

                    status_label['text'] = display
                    status_label.after(1000, count)
                    counter += 1

            count()

        def Start(status_label):
            global running
            running = True
            counter_label(status_label)
            start_btn['state'] = 'disabled'
            stop_btn['state'] = 'normal'
            reset_btn['state'] = 'normal'

        def Stop():
            global running
            start_btn['state'] = 'normal'
            stop_btn['state'] = 'disabled'
            reset_btn['state'] = 'normal'
            running = False

        def Reset(status_label):
            global counter
            counter = 66600

            if running == False:
                reset_btn['state'] = 'disabled'
                status_label['text'] = '00:00:00'

            else:
                status_label['text'] = 'STARTING'

        tk.Label(self, text='Stopwatch', font=('Cambria', 25, 'bold'), relief=FLAT, width=20).place(x=60)

        status_label = tk.Label(self, text='00:00:00', width=38, bg='pink', font=('open sans', 10, 'bold'), justify=CENTER)
        status_label.place(x=95, y=115)

        start_btn = tk.Button(self, text='Start', font=('verdana', 10, 'bold'), bg='#28B463', activebackground='#82E0AA', width=9, bd=3, relief=RAISED, command=lambda: Start(status_label))
        start_btn.place(x=85, y=70)

        stop_btn = tk.Button(self, text='Stop', font=('verdana', 10, 'bold'), bg='#34495E', activebackground='#AEB6BF', state='disabled', width=9, bd=3, relief=RAISED, command=Stop)
        stop_btn.place(x=202, y=70)

        reset_btn = tk.Button(self, text='Reset', font=('verdana', 10, 'bold'), bg='#DC7633', activebackground='#EDBB99', state='disabled', width=9, bd=3, relief=RAISED, command=lambda: Reset(status_label))
        reset_btn.place(x=318, y=70)

        tk.Button(self, text="Clock", font=('verdana', 10, 'bold'), width=9, bg='#5499C7', activebackground='#7FB3D5', bd=3, relief=RAISED, command=lambda: controller.show_frame(MainWindow)).place(y=150)
        tk.Button(self, text="Exit", font=('verdana', 10, 'bold'), width=9, bd=3, bg='#C0392B', activebackground='#D98880', relief=RAISED, command=lambda: Exit(self)).place(x=407, y=150)

class Exit(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Are you sure you want to quit?", font=('open sans', 10, 'bold')).place(x=10, y=10)
        tk.Button(self, text='Yes', font=('verdana', 10, 'bold'), width=9, bg='#E74C3C', activebackground='#F5B7B1', bd=3, relief=RAISED, command=lambda: self.quit()).place(x=20, y=40)
        tk.Button(self, text='No', font=('verdana', 10, 'bold'), width=9, bg='#5DADE2', activebackground='#AED6F1', bd=3, relief=RAISED, command=self.destroy).place(x=120, y=40)
        Exit.minsize(self, width=240, height=1)


class MainClass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.geometry()

        # This is the code that makes it possible to switch
        # between windows in the same frame
        self.frames = {}
        for F in (MainWindow, AlarmClock, Countdown, Stopwatch):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainWindow)

        self.title('KEVIN CLOCK')

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

clock = MainClass()
clock.minsize(width=500, height=180)
clock.minsize(width=500, height=180)
clock.mainloop()