import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import serial


class Index():

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Control Car")
        self.createWides()
        self.blue = serial.Serial("COM7", 9600)

    def createWides(self):
        # label frame
        infor_lab = ttk.LabelFrame(self.app, text="Information")
        infor_lab.grid(column=0, row=0)
        star_lab = ttk.LabelFrame(self.app, text="Start and Stop")
        star_lab.grid(column=0, row=1)
        control_lab = ttk.LabelFrame(self.app, text="Control ")
        control_lab.grid(column=0, row=2)
        speed_lab = ttk.LabelFrame(self.app, text="Speed Control ")
        speed_lab.grid(column=0, row=3)

        def start_click():
            Car_Status.configure(text="Car status: \n Car is starting!")
            # self.blue.open()
            self.blue.write(b"s")

        def stop_click():
            Car_Status.configure(text="Car status: \n Car is stopping!")
            self.blue.write(b"e")
            # self.blue.close()

        def up_click():
            Car_Status.configure(text="Car status: \n Car goes straigth!")
            self.blue.write(b"u")

        def left_click():
            Car_Status.configure(text="Car status: \n Car turns left!")
            self.blue.write(b"l")

        def right_click():
            Car_Status.configure(text="Car status: \n Car turns right!")
            self.blue.write(b"r")

        def down_click():
            Car_Status.configure(text="Car status: \n Car turn back!")
            self.blue.write(b"d")

        # gadget inside
        TITLE_INDEX = ttk.Label(infor_lab, text="Car Control version 1503201")
        TITLE_INDEX.grid(column=0, row=0)
        Author_Infor = ttk.Label(infor_lab, text="Author: Quoc Viet Luong")
        Author_Infor.grid(column=0, row=1)

        Start_Button = ttk.Button(star_lab, text="Start", command=start_click)
        Start_Button.grid(column=0, row=0)
        Stop_Button = ttk.Button(star_lab, text="Stop", command=stop_click)
        Stop_Button.grid(column=1, row=0)

        Up_Button = ttk.Button(control_lab, text="Up", command=up_click)
        Up_Button.grid(column=0, columnspan=2, row=0)
        Left_Button = ttk.Button(control_lab, text="Left", command=left_click)
        Left_Button.grid(column=0, row=1)
        Right_Button = ttk.Button(
            control_lab, text="Right", command=right_click)
        Right_Button.grid(column=1, row=1)
        Down_Button = ttk.Button(control_lab, text="Down", command=down_click)
        Down_Button.grid(column=0, columnspan=2, row=2)
        Car_Speed = ttk.Spinbox(speed_lab, from_=0, to=200)
        Car_Speed.grid(column=0, columnspan=2, row=0)

        Car_Status = ttk.Label(speed_lab, text="Car status: \n Connected")
        Car_Status.grid(column=0, columnspan=2, row=1)


main = Index()
main.app.mainloop()
