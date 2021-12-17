#pyClicker2.py
#Filip Rokita
#www.filiprokita.com



#import
import tkinter as tk
from tkinter import messagebox
import time
import pyautogui
import keyboard



#def
def prework():
    pyautogui.PAUSE = 0
    global start; start = startVar.get()
    global stop; stop = stopVar.get()
    global cps; cps = cpsVar.get()
    if len(start) == 1 and len(stop) == 1 and cps >= 1:
        startE['state'] = tk.DISABLED
        stopE['state'] = tk.DISABLED
        cpsE['state'] = tk.DISABLED
        confirmB['state'] = tk.DISABLED
        work()
    else: 
        messagebox.showerror(title='pyClicker2 - ERROR', message='Input appropriate Start/Stop buttons and CPS that greater or equal to 1!')


def work():
    while True:
        root.update()
        if keyboard.is_pressed(start) == True:
            while True:
                pyautogui.click()
                time.sleep(1/cps)
                if keyboard.is_pressed(stop) == True:
                    break



#main
root = tk.Tk()
root.title('pyClicker2')
root.geometry('300x300')
root.resizable(False, False)


startVar = tk.StringVar()
stopVar = tk.StringVar()
cpsVar = tk.IntVar()


startL = tk.Label(root, text='Start Button'); startL.pack()
startE = tk.Entry(root, textvariable=startVar); startE.pack()

stopL = tk.Label(root, text='Stop Button'); stopL.pack()
stopE = tk.Entry(root, textvariable=stopVar); stopE.pack()

cpsL = tk.Label(root, text='CPS'); cpsL.pack()
cpsE = tk.Entry(root, textvariable=cpsVar); cpsE.pack()

confirmB = tk.Button(root, text='Confirm', command=prework); confirmB.pack(pady=10)

authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()


root.mainloop()