from tkinter import Tk, Label, Button, mainloop
from santitools.time import Date
from pyttsx3 import speak
from asyncio import run
from sys import exit

def getTime(): return Date().getTime(12)

# creating tkinter window
string, root = getTime(), Tk()
root.title('Reloj parlante')
  
# This function is used to display time on the label
def time():
    string = getTime()
    lbl.config(text = string)
    lbl.after(1, time)

def spk():
	string = getTime()
	async def _spk():
		speak(f'La hora es {string}. ')
	run(
		_spk()
	)
	string = getTime()
def quit():
	async def spk():
		speak('Adiós. ')
	run(
		spk()
	)
	root.destroy()
	exit()
  
# Styling the label widget so that the clock will look more attractive
lbl, exitbtn, speakbtn = Label(root, font = ('calibri', 40, 'bold'), background = 'purple', foreground = 'white'), Button(root, text = 'Salir', command = quit, foreground = 'red'), Button(root, text = 'Hablar', command = spk, foreground = 'blue')

lbl.pack(anchor = 'center')
exitbtn.pack(anchor = 'ne', side = 'left')
speakbtn.pack(anchor = 'ne', side = 'left')
time()
mainloop()