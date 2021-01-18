from tkinter import *


cademp = Tk()
cademp.title("Include")
cademp['bg'] = "blue"


#definir a geometry
cademp.geometry("1100x700")



#widgets:
label1 = Label(cademp,
text = "Cadastro de empresa",
font = "Verdana 12")


frame_dados = Frame(cademp)
frame_cargos = Frame(cademp)
frame_especialidades = Frame(cademp)


label_nome = Label(frame_dados, text = "Nome:")
label_cnpj = Label(frame_dados, text = "CNPJ:")
label_endereço = Label(frame_dados, text = "Endereço:")
label_telefone = Label(frame_dados, text = "Telefone:")
label_email = Label(frame_dados, text = "E-mail:")
b1 = Button(frame_dados, text = "Cadastrar", command = 'cadastrar')

label_cargo1 = Label(frame_cargos, text = "Cargo 1:")
label_cargo2 = Label(frame_cargos, text = "Cargo 2:")
label_cargo3 = Label(frame_cargos, text = "Cargo 3:")
label_cargo4 = Label(frame_cargos, text = "Cargo 4:")
b2 = Button(frame_cargos, text = "Cadastrar", command = 'cadastrar')

label_especialidade1 = Label(frame_especialidades, text = "Especialidade 1:")
label_especialidade2 = Label(frame_especialidades, text = "Especialidade 2:")
label_especialidade3 = Label(frame_especialidades, text = "Especialidade 3:")
label_especialidade4 = Label(frame_especialidades, text = "Especialidade 4:")
b3 = Button(frame_especialidades, text = "Relacionar a cargo 1", command = 'Relacionar a cargo 1')
b4 = Button(frame_especialidades, text = "Relacionar a cargo 2", command = 'Relacionar a cargo 2')
b5 = Button(frame_especialidades, text = "Relacionar a cargo 3", command = 'Relacionar a cargo 3')
b6 = Button(frame_especialidades, text = "Relacionar a cargo 4", command = 'Relacionar a cargo 4')

text_nome = Entry(frame_dados)
text_cnpj = Entry(frame_dados)
text_endereço = Entry(frame_dados)
text_telefone = Entry(frame_dados)
text_email = Entry(frame_dados)

text_cargo1 = Entry(frame_cargos)
text_cargo2 = Entry(frame_cargos)
text_cargo3 = Entry(frame_cargos)
text_cargo4 = Entry(frame_cargos)

text_especialidade1 = Entry(frame_especialidades)
text_especialidade2 = Entry(frame_especialidades)
text_especialidade3 = Entry(frame_especialidades)
text_especialidade4 = Entry(frame_especialidades)


#layout:
label_nome.grid(row = 0, column = 0)
label_cnpj.grid(row = 1, column = 0)
label_endereço.grid(row = 2, column = 0)
label_telefone.grid(row = 3, column = 0)
label_email.grid(row = 4, column = 0)
b1.grid(row = 5, column = 1)

label_cargo1.grid(row = 0, column = 0)
label_cargo2.grid(row = 1, column = 0)
label_cargo3.grid(row = 2, column = 0)
label_cargo4.grid(row = 3, column = 0)
b2.grid(row = 4, column = 1)

label_especialidade1.grid(row = 0, column = 0)
label_especialidade2.grid(row = 1, column = 0)
label_especialidade3.grid(row = 2, column = 0)
label_especialidade4.grid(row = 3, column = 0)
b3.grid(row = 0, column = 2)
b4.grid(row = 1, column = 2)
b5.grid(row = 2, column = 2)
b6.grid(row = 3, column = 2)

text_nome.grid(row = 0, column = 1)
text_cnpj.grid(row = 1, column = 1)
text_endereço.grid(row = 2, column = 1)
text_telefone.grid(row = 3, column = 1)
text_email.grid(row = 4, column = 1)

text_cargo1.grid(row = 0, column = 1)
text_cargo2.grid(row = 1, column = 1)
text_cargo3.grid(row = 2, column = 1)
text_cargo4.grid(row = 3, column = 1)

text_especialidade1.grid(row = 0, column = 1)
text_especialidade2.grid(row = 1, column = 1)
text_especialidade3.grid(row = 2, column = 1)
text_especialidade4.grid(row = 3, column = 1)


label1.grid(row = 0, column = 1)

frame_dados.grid(row = 1, column = 0)
frame_cargos.grid(row = 1, column = 1)
frame_especialidades.grid(row = 1, column = 2)

#cadastro de usuário:
Label(cademp, text = "Nome de usuário:").grid(row = 2, column = 0)
Label(cademp, text = "Senha:").grid(row = 3, column = 0)

text_usuario = Entry(cademp).grid(row = 2, column = 1)
text_senha = Entry(cademp).grid(row = 3, column = 1)

cmd_login = Button(cademp, text = "Cadastro").grid(row = 4, column = 1)


cademp.mainloop()

