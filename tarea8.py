from tkinter import ttk
from Arduino import Arduino
from tkinter import *

# Arduino Setup
board = Arduino("115200", port="COM3")
board.pinMode(11, "OUTPUT")
board.pinMode(10, "OUTPUT")
board.pinMode(9, "OUTPUT")


def updateLedUno(val):
    fv = float(val)
    board.analogWrite(11, int(fv))


def updateLedDos(val):
    fv = float(val)
    board.analogWrite(10, int(fv))


def updateLedTres(val):
    fv = float(val)
    board.analogWrite(9, int(fv))


def OFuno():
    state = str(scale1.cget('state'))
    if state == "normal":
        scale1.config(state=DISABLED)
        board.analogWrite(11, 0)
    else:
        scale1.config(state=NORMAL)
        fv = float(scale1.get())
        board.analogWrite(11, int(fv))

def OFdos():
    state = str(scale2.cget('state'))
    if state == "normal":
        scale2.config(state=DISABLED)
        board.analogWrite(10, 0)
    else:
        scale2.config(state=NORMAL)
        fv = float(scale2.get())
        board.analogWrite(10, int(fv))


def OFtres():
    state = str(scale3.cget('state'))
    if state == "normal":
        scale3.config(state=DISABLED)
        board.analogWrite(9, 0)
    else:
        scale3.config(state=NORMAL)
        fv = float(scale3.get())
        board.analogWrite(9, int(fv))


window = Tk()
window.title("Led Controller")
window.geometry('400x350')
window.resizable(False, False)
btn1 = Button(window, text="LED 1", command=OFuno)
btn1.place(x=20, y=30, width=100, height=25)
btn2 = Button(window, text="LED 2", command=OFdos)
btn2.place(x=150, y=30, width=100, height=25)
btn3 = Button(window, text="LED 3", command=OFtres)
btn3.place(x=280, y=30, width=100, height=25)
scale1 = ttk.Scale(window, from_=0, to=255, orient='vertical', command=updateLedUno)
scale1.place(x=50, y=70, width=50, height=200)
scale2 = ttk.Scale(window, from_=0, to=255, orient='vertical', command=updateLedDos)
scale2.place(x=180, y=70, width=50, height=200)
scale3 = ttk.Scale(window, from_=0, to=255, orient='vertical', command=updateLedTres)
scale3.place(x=310, y=70, width=50, height=200)
window.mainloop()
