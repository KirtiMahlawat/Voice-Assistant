import tkinter
from tkinter.ttk import *
#Creating the main window 
wn = tkinter.Tk() 
wn.title("DataFlair Voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='Welcome to meet the Voice Assistant by DataFlair', bg='LightBlue1',
      fg='black', font=('Courier', 15)).place(x=50, y=10)
#Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray',font=('Courier', 15),command=callVoiceAssistant).place(x=290, y=100)
showCommand=StringVar()
cmdLabel=Label(wn, textvariable=showCommand, bg='LightBlue1',
      fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)
#Runs the window till it is closed
wn.mainloop()