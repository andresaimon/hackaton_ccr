from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Include")
menu_inicial['bg'] = "blue"

#menu_inicial.resizable(True,True)

#definir a geometry
menu_inicial.geometry("1100x700")


bt1 = Button(menu_inicial, text = "Cadastro de colaborador", font = "Verdana 15", bd = 3, relief = "raised")


bt2 = Button(menu_inicial)
bt2['text'] = "Cadastro de empresa"
bt2['font'] = "Verdana 15"
bt2['bd'] = 3
bt2['relief'] = "raised"


label1 = Label(menu_inicial,
text = "Include",
font = "Verdana 12")

label2 = Label(menu_inicial,
text = "Conecte o seu colaborador a cursos voltados para progressão de carreira dentro da sua empresa!",
font = "Verdana 12")

label1.grid(row = 0, columnspan = 3, sticky = 'we')
label2.grid(row = 1, columnspan = 3, sticky = 'we')

bt1.grid(row = 2, column = 0)
bt2.grid(row = 2, column = 2)



frame_login = Frame(menu_inicial)


Label(frame_login, text = "Login colaborador:").grid(row = 0, column = 0)
Label(frame_login, text = "Senha:").grid(row = 1, column = 0)

text_usuario = Entry(frame_login).grid(row = 0, column = 1)
text_senha = Entry(frame_login).grid(row = 1, column = 1)

cmd_login = Button(frame_login, text = "Login").grid(row = 1, column = 2)

Label(frame_login, text = "Login empresa:").grid(row = 2, column = 0)
Label(frame_login, text = "Senha:").grid(row = 3, column = 0)

text_usuario = Entry(frame_login).grid(row = 2, column = 1)
text_senha = Entry(frame_login).grid(row = 3, column = 1)

cmd_login = Button(frame_login, text = "Login").grid(row = 3, column = 2)

frame_login.grid(row = 3, column = 1)



menu_inicial.mainloop()
