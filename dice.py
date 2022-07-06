from santitools.math import random
import tkinter
import pyttsx3

MAX, MIN = 6, 1

def rn():
    rnLabel.config(text = random(MAX, MIN))
    pyttsx3.speak(rnLabel.cget('text'))

root = tkinter.Tk()
rnLabel = tkinter.Label(root, text = str(random(MAX, MIN)), font = ('calibri', 40, 'bold'), background = 'blue', foreground = 'white')
rnButton = tkinter.Button(root, text = 'Generar', command = rn)

root.title('Dado electrónico')
root.geometry('300x100')
rnLabel.pack()
rnButton.pack()
root.mainloop()
