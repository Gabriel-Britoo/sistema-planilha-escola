import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class SistemaAlunos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Alunos")
        self.root.geometry("700x500")

        self.df = pd.DataFrame(columns=["Nome", "Idade", "Curso", "Nota"])

        self.criar_interface()

    def criar_interface(self):
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nome:").grid(row=0, column=0)
        tk.Label(frame_form, text="Idade:").grid(row=0, column=2)
        tk.Label(frame_form, text="Curso:").grid(row=1, column=0)
        tk.Label(frame_form, text="Nota Final:").grid(row=1, column=2)

        self.entry_nome = tk.Entry(frame_form)
        self.entry_idade = tk.Entry(frame_form)
        self.entry_curso = tk.Entry(frame_form)
        self.entry_nota = tk.Entry(frame_form)

        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        self.entry_idade.grid(row=0, column=3, padx=5, pady=5)
        self.entry_curso.grid(row=1, column=1, padx=5, pady=5)
        self.entry_nota.grid(row=1, column=3, padx=5, pady=5)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Cadastrar", command=self.cadastrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botoes, text="Exibir Todos", command=self.exibir).grid(row=0, column=1, padx=5)
        tk.Button(frame_botoes, text="Filtrar por Média", command=self.filtrar).grid(row=0, column=2, padx=5)
        tk.Button(frame_botoes, text="Salvar CSV", command=self.salvar_csv).grid(row=0, column=3, padx=5)
        tk.Button(frame_botoes, text="Carregar CSV", command=self.carregar_csv).grid(row=0, column=4, padx=5)
        tk.Button(frame_botoes, text="Exportar Relatório", command=self.exportar_csv).grid(row=0, column=5, padx=5)

        self.tabela = ttk.Treeview(self.root, columns=["Nome", "Idade", "Curso", "Nota"], show="headings")
        for col in ["Nome", "Idade", "Curso", "Nota"]:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=120)
        self.tabela.pack(expand=True, fill="both", pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        curso = self.entry_curso.get()
        nota = self.entry_nota.get()

        if not nome or not idade or not curso or not nota:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        try:
            idade = int(idade)
            nota = float(nota)
        except ValueError:
            messagebox.showerror("Erro", "Idade e Nota devem ser numéricas!")
            return

        novo_aluno = {"Nome": nome, "Idade": idade, "Curso": curso, "Nota": nota}
        self.df = pd.concat([self.df, pd.DataFrame([novo_aluno])], ignore_index=True)

        self.limpar_campos()
        self.exibir()

    def exibir(self, dados=None):
        for i in self.tabela.get_children():
            self.tabela.delete(i)

        dados = dados if dados is not None else self.df
        for _, row in dados.iterrows():
            self.tabela.insert("", "end", values=row.tolist())

    def filtrar(self):
        media = tk.simpledialog.askfloat("Filtrar", "Mostrar alunos com nota acima de:")
        if media is None:
            return

        filtrado = self.df[self.df["Nota"] > media]
        self.exibir(filtrado)
        self.dados_filtrados = filtrado

    def salvar_csv(self):
        caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if caminho:
            self.df.to_csv(caminho, index=False)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    def carregar_csv(self):
        caminho = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if caminho:
            self.df = pd.read_csv(caminho)
            self.exibir()
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")

    def exportar_csv(self):
        if not hasattr(self, "dados_filtrados") or self.dados_filtrados.empty:
            messagebox.showwarning("Aviso", "Nenhum dado filtrado para exportar.")
            return

        caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if caminho:
            self.dados_filtrados.to_csv(caminho, index=False)
            messagebox.showinfo("Sucesso", "Relatório exportado com sucesso!")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_curso.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAlunos(root)
    root.mainloop()