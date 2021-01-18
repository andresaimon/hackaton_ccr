from tkinter import *

cursos = Tk()
cursos.title("Include")
cursos['bg'] = "blue"

cursos.geometry("1100x700")
     
canvas = Canvas(width=300, height=300, bg='blue')
canvas.grid(row = 0, column = 0)          
     
canvas.create_oval(10, 10, 200, 200, width=2, fill='white')
     
widget = Label(canvas, text='Posição X', fg='yellow', bg='black')
widget.grid(row = 0, column = 0)

canvas.create_window(100, 100, window=widget) 


frame_especialidades = Frame(cursos)
b3 = Button(frame_especialidades, text = "Realizar curso 1", command = 'Redirecionar para curso 1')
b4 = Button(frame_especialidades, text = "Realizar curso 2", command = 'Redirecionar para curso 2')
b5 = Button(frame_especialidades, text = "Realizar curso 3", command = 'Redirecionar para curso 3')
b6 = Button(frame_especialidades, text = "Realizar curso 4", command = 'Redirecionar para curso 4')

b3.grid(row = 0, column = 0)
b4.grid(row = 1, column = 0)
b5.grid(row = 2, column = 0)
b6.grid(row = 3, column = 0)

frame_especialidades.grid(row = 1, column = 0)


cursos.mainloop()