from tkinter import *

plan = Tk()
plan.title("Include")
plan['bg'] = "blue"

plan.geometry("1100x700")
     
canvas = Canvas(width=300, height=300, bg='blue')
canvas.grid(row = 0, column = 0)          
     
canvas.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget = Label(canvas, text='Posição X', fg='yellow', bg='black')
widget.grid(row = 0, column = 0)

canvas.create_window(100, 100, window=widget)  





canvas2 = Canvas(width=300, height=300, bg='blue')
canvas2.grid(row = 0, column = 1)          
     
canvas2.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget2 = Label(canvas2, text='Posição Y', fg='yellow', bg='black')
widget2.grid(row = 0, column = 1)

canvas2.create_window(100, 100, window=widget2)



canvas3 = Canvas(width=300, height=300, bg='blue')
canvas3.grid(row = 1, column = 0)          
     
canvas3.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget3 = Label(canvas3, text='Posição A', fg='yellow', bg='black')
widget3.grid(row = 1, column = 0)

canvas3.create_window(100, 100, window=widget3)




canvas4 = Canvas(width=300, height=300, bg='blue')
canvas4.grid(row = 1, column = 1)          
     
canvas4.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget4 = Label(canvas4, text='Posição B', fg='yellow', bg='black')
widget4.grid(row = 1, column = 1)

canvas4.create_window(100, 100, window=widget4)



canvas5 = Canvas(width=300, height=300, bg='blue')
canvas5.grid(row = 0, column = 2)          
     
canvas5.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget5 = Label(canvas5, text='Posição Z', fg='yellow', bg='black')
widget5.grid(row = 0, column = 2)

canvas5.create_window(100, 100, window=widget5)




canvas6 = Canvas(width=300, height=300, bg='blue')
canvas6.grid(row = 1, column = 2)          
     
canvas6.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget6 = Label(canvas6, text='Posição C', fg='yellow', bg='black')
widget6.grid(row = 1, column = 2)

canvas6.create_window(100, 100, window=widget6)

plan.mainloop()