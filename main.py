import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Sistema de planilhas")

frame = tkinter.Frame(window)
frame.pack()

frame_info_aluno = tkinter.LabelFrame(frame, text="Informações do aluno")
frame_info_aluno.grid(row=0, column=0, padx=10, pady=10)

label_nome = tkinter.Label(frame_info_aluno, text="Nome:")
label_nome.grid(row=0, column=0)
label_idade = tkinter.Label(frame_info_aluno, text="Idade:")
label_idade.grid(row=0, column=1)

nome_entry = tkinter.Entry(frame_info_aluno)
nome_entry.grid(row=1, column=0)
idade_entry = tkinter.Entry(frame_info_aluno)
idade_entry.grid(row=1, column=1)

curso_label = tkinter.Label(frame_info_aluno, text="Curso:")
curso_label.grid(row=2, column=0)
curso_select = ttk.Combobox(frame_info_aluno, state="readonly", values=["ADS", "Administração", "Multimídia", "Elétrica"])
curso_select.set("Selecionar")
curso_select.grid(row=3, column=0)

window.mainloop()