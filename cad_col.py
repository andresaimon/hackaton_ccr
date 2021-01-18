from tkinter import *

cadcol = Tk()
cadcol.title("Include")
cadcol['bg'] = "blue"


#definir a geometry
cadcol.geometry("1100x700")



#widgets:
label1 = Label(cadcol,
text = "Cadastro de colaborador",
font = "Verdana 12")


frame_dados = Frame(cadcol)
frame_cargos = Frame(cadcol)
frame_especialidades = Frame(cadcol)


label_nome = Label(frame_dados, text = "Nome:")
label_cpf = Label(frame_dados, text = "CPF:")
label_endereço = Label(frame_dados, text = "Endereço:")
label_telefone = Label(frame_dados, text = "Telefone:")
label_email = Label(frame_dados, text = "E-mail:")
b1 = Button(frame_dados, text = "Cadastrar", command = 'cadastrar')

label_empresa = Label(frame_cargos, text = "Empresa:")
label_cargo1 = Label(frame_cargos, text = "Cargo")
b2 = Button(frame_cargos, text = "Cadastrar", command = 'cadastrar')

label_especialidade1 = Label(frame_especialidades, text = "Especialidade 1:")
label_especialidade2 = Label(frame_especialidades, text = "Especialidade 2:")
label_especialidade3 = Label(frame_especialidades, text = "Especialidade 3:")
label_especialidade4 = Label(frame_especialidades, text = "Especialidade 4:")
b3 = Button(frame_especialidades, text = "Cadastrar", command = 'cadastrar')

text_nome = Entry(frame_dados)
text_cpf = Entry(frame_dados)
text_endereço = Entry(frame_dados)
text_telefone = Entry(frame_dados)
text_email = Entry(frame_dados)

text_empresa = Entry(frame_cargos)
text_cargo1 = Entry(frame_cargos)

text_especialidade1 = Entry(frame_especialidades)
text_especialidade2 = Entry(frame_especialidades)
text_especialidade3 = Entry(frame_especialidades)
text_especialidade4 = Entry(frame_especialidades)


#layout:
label_nome.grid(row = 0, column = 0)
label_cpf.grid(row = 1, column = 0)
label_endereço.grid(row = 2, column = 0)
label_telefone.grid(row = 3, column = 0)
label_email.grid(row = 4, column = 0)
b1.grid(row = 5, column = 1)

label_empresa.grid(row = 0, column = 0)
label_cargo1.grid(row = 1, column = 0)
b2.grid(row = 2, column = 1)

label_especialidade1.grid(row = 0, column = 0)
label_especialidade2.grid(row = 1, column = 0)
label_especialidade3.grid(row = 2, column = 0)
label_especialidade4.grid(row = 3, column = 0)
b3.grid(row = 4, column = 1)

text_nome.grid(row = 0, column = 1)
text_cpf.grid(row = 1, column = 1)
text_endereço.grid(row = 2, column = 1)
text_telefone.grid(row = 3, column = 1)
text_email.grid(row = 4, column = 1)

text_empresa.grid(row = 0, column = 1)
text_cargo1.grid(row = 1, column = 1)

text_especialidade1.grid(row = 0, column = 1)
text_especialidade2.grid(row = 1, column = 1)
text_especialidade3.grid(row = 2, column = 1)
text_especialidade4.grid(row = 3, column = 1)


label1.grid(row = 0, column = 1)

frame_dados.grid(row = 1, column = 0)
frame_cargos.grid(row = 1, column = 1)
frame_especialidades.grid(row = 1, column = 2)

#cadastro de usuário:
Label(cadcol, text = "Nome de usuário:").grid(row = 2, column = 0)
Label(cadcol, text = "Senha:").grid(row = 3, column = 0)

text_usuario = Entry(cadcol).grid(row = 2, column = 1)
text_senha = Entry(cadcol).grid(row = 3, column = 1)

cmd_login = Button(cadcol, text = "Cadastro").grid(row = 4, column = 1)


cadcol.mainloop()

